# DriveHandCar: Controle de Jogo MR RACER Carro Usando Gestos de Mão

## 📌 Overview

O **DriveHandCar** é um projeto inovador que permite controlar o jogo de corrida **MR RACER - Car Racing** utilizando gestos de mão. Com o apoio da visão computacional e do reconhecimento de gestos, o sistema captura os movimentos das mãos através de uma webcam e os converte em comandos de teclado. Dessa forma, é possível virar à esquerda, à direita, acelerar ou dar ré, tornando a experiência do jogo mais interativa e divertida! 🖐️

---

## ✨ **Features**
✔️ **Rastreamento de mãos em tempo real** – Utiliza o Mediapipe Hands para detectar e rastrear os pontos de referência das mãos com precisão.  
✔️ **Reconhecimento de gestos** – Interpreta gestos específicos para definir os comandos do jogo:  
   🔹 Virar à esquerda  
   🔹 Virar à direita  
   🔹 Acelerar (manter em frente)  
   🔹 Dar ré  
✔️ **Simulação de entrada de teclado** – Converte os gestos em comandos de teclado (W, A, S, D) utilizando o módulo `pynput`, possibilitando o controle do jogo.  
✔️ **Feedback visual** – Exibe, em tempo real, elementos gráficos (círculos e linhas) que indicam a área de referência e os gestos reconhecidos, facilitando a compreensão da ação.  
✔️ **Facilidade de uso** – Basta posicionar as mãos na frente da webcam para iniciar o controle do jogo.  

---

## 🔧 **Requirements**
Para executar o DriveHandCar, você precisará do seguinte:

✅ **Python:** Recomendado utilizar a versão **3.11.6** ou superior.  
✅ **Bibliotecas Python:**  
   - [opencv-python](https://pypi.org/project/opencv-python/)  
   - [mediapipe](https://pypi.org/project/mediapipe/)  
   - [pynput](https://pypi.org/project/pynput/)  

📌 Instale todas as dependências executando:

```bash
pip install -r requirements.txt

🗂️ Code Structure
📌 projectCar.py

Captura o vídeo da webcam;
Processa os gestos das mãos utilizando o MediaPipe;
Simula as entradas de teclado para controlar o jogo com base nos gestos.
📌 keyboardControl.py

Módulo auxiliar que utiliza o pynput para simular os comandos do teclado (pressionamento e liberação de teclas).

🎮 Como Funciona (Dicas)
✅ 1️⃣ Inicialização
📌 O script principal abre a URL do jogo MR RACER - Car Racing no navegador padrão.
📌 Em seguida, inicia a captura do vídeo da webcam.

✅ 2️⃣ Detecção de Gestos
📌 Através do MediaPipe, o sistema detecta os pontos de referência das mãos, focando, por exemplo, na posição do pulso.
📌 A posição relativa dos pulsos determina se o comando será de virar à esquerda, virar à direita, acelerar ou dar ré.

✅ 3️⃣ Simulação dos Comandos
📌 Com base na análise dos gestos, o módulo keyboardControl.py simula os comandos do teclado (W, A, S, D), que são enviados ao jogo.
📌 O feedback visual na tela auxilia no entendimento das ações executadas.

✅ 4️⃣ Feedback Visual
📌 Elementos gráficos, como círculos e linhas, são desenhados sobre a imagem capturada para indicar as áreas de controle e os gestos reconhecidos.
📌 Esse feedback permite ajustes em tempo real para um melhor desempenho do controle.

✅ 5️⃣ Encerramento
📌 O sistema permite encerrar a aplicação a qualquer momento, pressionando a tecla "q".

🚀 Instalação e Execução
🔹 Clone o repositório:
```bash
git clone https://github.com/marcosbrunomendes/DriveHandCar.git

🔹 Navegue até o diretório do projeto:
```bash
cd DriveHandCar

🔹 Instale as dependências:
```bash
pip install -r requirements.txt

🔹 Execute o script principal:
```bash
python projectCar.py

🎯 Dicas Extras
🔹 Melhorando a Performance
✅ Para evitar travamentos, utilize uma câmera externa (USB) de boa qualidade.
✅ No Windows 11, algumas câmeras podem ter latência elevada; se necessário, use o DroidCam ou outra solução para conectar o celular como webcam.
✅ Caso haja atraso na resposta dos gestos, reduza a resolução da câmera no código.

🔹 Personalizando os Controles
✅ No arquivo keyboardControl.py, você pode modificar quais teclas são pressionadas para adaptar o sistema a outros jogos.

🔹 Resolução da Janela de Exibição
✅ No código projectCar.py, a janela que exibe os gestos pode ser redimensionada com:
```python
cv2.namedWindow('Detecção de Mãos', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Detecção de Mãos', 1280, 720)
