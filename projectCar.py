"""
Módulo principal para controle do jogo via detecção de mãos.

Este módulo utiliza OpenCV, MediaPipe e um módulo auxiliar para simular 
comandos de teclado com base na detecção de gestos das mãos capturadas pela webcam.
"""

import math
import cv2
import mediapipe as mp
import webbrowser
import time
import keyboardControl as key_controller  # Importa o módulo de controle de teclado com alias

# -----------------------------------------------------------------------------
# Função auxiliar: converte coordenadas normalizadas (0.0 a 1.0) para pixels.
# -----------------------------------------------------------------------------
def norm_coords_to_pixels(norm_x: float, norm_y: float, img_width: int,
                           img_height: int) -> tuple[int, int]:
    """
    Converte coordenadas normalizadas para coordenadas de pixel.

    :param norm_x: Valor normalizado na direção x.
    :param norm_y: Valor normalizado na direção y.
    :param img_width: Largura da imagem em pixels.
    :param img_height: Altura da imagem em pixels.
    :return: Tupla (x, y) com as coordenadas convertidas.
    """
    x_pixel = min(math.floor(norm_x * img_width), img_width - 1)
    y_pixel = min(math.floor(norm_y * img_height), img_height - 1)
    return x_pixel, y_pixel


# -----------------------------------------------------------------------------
# Função principal
# -----------------------------------------------------------------------------
def main() -> None:
    """
    Função principal para inicializar o jogo e processar a detecção das mãos.
    """
    # URL do jogo; o navegador padrão será aberto com esta URL.
    game_url = (
        "https://poki.com/br/g/mr-racer-car-racing?"
        "campaign=20607849513&adgroup=166832396293&extensionid=&targetid=kwd-820520308461"
        "&location=9102328&matchtype=e&network=g&device=c&devicemodel=&creative=712136909435"
        "&keyword=mr%20racer&placement=&target=&gad_source=1&gclid=CjwKCAiAiOa9BhBqEiwABCdG89qARizSUg_8wAL5PYLKF8wSBYu8BWPeKe2AgpLeBrihLxxj3bCjKBoCezQQAvD_BwE"
    )
    webbrowser.open(game_url)
    time.sleep(5)  # Aguarda 5 segundos para o carregamento do jogo

    # Inicializa os módulos do MediaPipe para detecção de mãos
    mp_draw = mp.solutions.drawing_utils
    mp_styles = mp.solutions.drawing_styles
    mp_hands = mp.solutions.hands

    # Inicializa a captura de vídeo pela webcam
    video = cv2.VideoCapture(0)
    if not video.isOpened():
        print("Erro: Webcam não disponível.")
        return

    # Cria e redimensiona a janela para exibição da detecção de mãos
    window_name = 'Detecção de Mãos'
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(window_name, 1280, 720)  # Define a resolução desejada

    # Parâmetros para desenho e lógica dos comandos
    circle_radius = 150   # Raio do círculo central de referência
    min_diff = 65         # Diferença mínima vertical para acionar comandos

    # Inicializa o detector de mãos com parâmetros ajustados
    with mp_hands.Hands(
        model_complexity=0,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5
    ) as hands_detector:
        while video.isOpened():
            ret, frame = video.read()
            if not ret:
                print("Aviso: Quadro vazio, ignorando...")
                continue

            # Converte a imagem para RGB (MediaPipe trabalha com RGB)
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame_rgb.flags.writeable = False
            detection_results = hands_detector.process(frame_rgb)
            frame_rgb.flags.writeable = True
            frame = cv2.cvtColor(frame_rgb, cv2.COLOR_RGB2BGR)
            img_height, img_width, _ = frame.shape

            # Lista para armazenar as coordenadas dos pulsos detectados
            wrist_points: list[tuple[int, int]] = []
            if detection_results.multi_hand_landmarks:
                for hand_landmarks in detection_results.multi_hand_landmarks:
                    # Desenha os pontos e as conexões da mão na imagem
                    mp_draw.draw_landmarks(
                        frame,
                        hand_landmarks,
                        mp_hands.HAND_CONNECTIONS,
                        mp_styles.get_default_hand_landmarks_style(),
                        mp_styles.get_default_hand_connections_style()
                    )
                    # Obtém a posição do pulso
                    wrist = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST]
                    pixel_coord = norm_coords_to_pixels(wrist.x, wrist.y,
                                                        img_width, img_height)
                    wrist_points.append(pixel_coord)

            # Processa comandos se duas mãos forem detectadas
            if len(wrist_points) == 2:
                # Define a mão esquerda e a mão direita com base na posição x
                if wrist_points[0][0] < wrist_points[1][0]:
                    left_wrist, right_wrist = wrist_points[0], wrist_points[1]
                else:
                    left_wrist, right_wrist = wrist_points[1], wrist_points[0]

                # Calcula o ponto central entre os pulsos
                center_x = (left_wrist[0] + right_wrist[0]) / 2
                center_y = (left_wrist[1] + right_wrist[1]) / 2

                # Desenha um círculo central de referência
                cv2.circle(frame, (int(center_x), int(center_y)),
                           circle_radius, (195, 255, 62), thickness=15)

                # Calcula o ângulo da linha que une os pulsos
                delta_x = right_wrist[0] - left_wrist[0]
                delta_y = right_wrist[1] - left_wrist[1]
                angle = math.atan2(delta_y, delta_x)

                # Determina os pontos extremos na linha que cruza o círculo
                point1_x = center_x + circle_radius * math.cos(angle)
                point1_y = center_y + circle_radius * math.sin(angle)
                point2_x = center_x - circle_radius * math.cos(angle)
                point2_y = center_y - circle_radius * math.sin(angle)
                cv2.line(frame, (int(point1_x), int(point1_y)),
                         (int(point2_x), int(point2_y)), (195, 255, 62), 20)

                # Calcula os pontos na linha perpendicular para auxiliar na visualização
                perp_angle = angle + math.pi / 2
                perp_point1_x = center_x + circle_radius * math.cos(perp_angle)
                perp_point1_y = center_y + circle_radius * math.sin(perp_angle)
                perp_point2_x = center_x - circle_radius * math.cos(perp_angle)
                perp_point2_y = center_y - circle_radius * math.sin(perp_angle)

                # Define comandos com base na diferença vertical dos pulsos
                if (left_wrist[1] + min_diff) < right_wrist[1]:
                    print("Virar à direita.")
                    key_controller.release_key('s')
                    key_controller.release_key('a')
                    key_controller.press_key('d')
                    cv2.putText(frame, "Turn right", (50, 50),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                                (0, 255, 0), 2, cv2.LINE_AA)
                    cv2.line(frame, (int(point1_x), int(point1_y)),
                             (int(center_x), int(center_y)),
                             (195, 255, 62), 20)
                elif (right_wrist[1] + min_diff) < left_wrist[1]:
                    print("Virar à esquerda.")
                    key_controller.release_key('s')
                    key_controller.release_key('d')
                    key_controller.press_key('a')
                    cv2.putText(frame, "Turn left", (50, 50),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                                (0, 255, 0), 2, cv2.LINE_AA)
                    cv2.line(frame, (int(perp_point2_x), int(perp_point2_y)),
                             (int(center_x), int(center_y)),
                             (195, 255, 62), 20)
                else:
                    print("Manter em frente.")
                    key_controller.release_key('s')
                    key_controller.release_key('a')
                    key_controller.release_key('d')
                    key_controller.press_key('w')
                    cv2.putText(frame, "Keep straight", (50, 50),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                                (0, 255, 0), 2, cv2.LINE_AA)
                    # Escolhe qual linha perpendicular desenhar com base na posição
                    if perp_point2_y > perp_point1_y:
                        cv2.line(frame, (int(perp_point2_x), int(perp_point2_y)),
                                 (int(center_x), int(center_y)),
                                 (195, 255, 62), 20)
                    else:
                        cv2.line(frame, (int(perp_point1_x), int(perp_point1_y)),
                                 (int(center_x), int(center_y)),
                                 (195, 255, 62), 20)

            # Se apenas um pulso for detectado, simula comando para recuar
            elif len(wrist_points) == 1:
                print("Recuar")
                key_controller.release_key('a')
                key_controller.release_key('d')
                key_controller.release_key('w')
                key_controller.press_key('s')
                cv2.putText(frame, "Keep back", (50, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1.0,
                            (0, 255, 0), 2, cv2.LINE_AA)

            # Exibe a imagem espelhada (visualização tipo selfie)
            cv2.imshow(window_name, cv2.flip(frame, 1))
            if cv2.waitKey(5) & 0xFF == ord('q'):
                break

    video.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
