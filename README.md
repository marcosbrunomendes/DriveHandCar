# DriveHandCar: Controle de Jogo MR RACER com Gestos de Mão 🏎️🖐️

## 📌 Visão Geral

O **DriveHandCar** é um projeto inovador que permite controlar o jogo de corrida **MR RACER - Car Racing** utilizando gestos de mão. Com o suporte da visão computacional e do reconhecimento de gestos, o sistema captura os movimentos das mãos através de uma webcam e os converte em comandos de teclado. Dessa forma, é possível virar à esquerda, à direita, acelerar ou dar ré, proporcionando uma experiência de jogo mais interativa e divertida! 🎮✨

---

## ✨ Recursos Principais

✔️ **Rastreamento de mãos em tempo real** – Utiliza o *MediaPipe Hands* para detectar e rastrear os pontos de referência das mãos com alta precisão.  
✔️ **Reconhecimento de gestos** – Interpreta gestos específicos para definir os comandos do jogo:  
   🔹 Virar à esquerda  
   🔹 Virar à direita  
   🔹 Acelerar (manter a mão à frente)  
   🔹 Dar ré  
✔️ **Simulação de entrada de teclado** – Converte os gestos em comandos de teclado (W, A, S, D) utilizando a biblioteca `pynput`, possibilitando o controle do jogo.  
✔️ **Feedback visual** – Exibe, em tempo real, elementos gráficos (círculos e linhas) que indicam a área de referência e os gestos reconhecidos, facilitando a compreensão das ações.  
✔️ **Facilidade de uso** – Basta posicionar as mãos na frente da webcam para iniciar o controle do jogo.  

---

## 🔧 Requisitos

Para executar o **DriveHandCar**, você precisará dos seguintes requisitos:

✅ **Python:** Recomendado utilizar a versão **3.11.6** ou superior.  
✅ **Bibliotecas Python:**  
   - [opencv-python](https://pypi.org/project/opencv-python/)  
   - [mediapipe](https://pypi.org/project/mediapipe/)  
   - [pynput](https://pypi.org/project/pynput/)  

📌 Instale todas as dependências executando o seguinte comando:

```bash
pip install -r requirements.txt
```

---

## 🗂️ Estrutura do Código

📌 **projectCar.py**  
   - Captura o vídeo da webcam  
   - Processa os gestos das mãos utilizando o MediaPipe  
   - Simula as entradas de teclado para controlar o jogo com base nos gestos  

📌 **keyboardControl.py**  
   - Módulo auxiliar que utiliza `pynput` para simular os comandos do teclado (pressionamento e liberação de teclas)  

---

## 🎮 Como Funciona?

### 1️⃣ Inicialização  
📌 O script principal abre a URL do jogo *MR RACER - Car Racing* no navegador padrão.  
📌 Em seguida, inicia a captura do vídeo da webcam.  

### 2️⃣ Detecção de Gestos  
📌 O sistema detecta os pontos de referência das mãos através do *MediaPipe*, focando na posição do pulso e dedos.  
📌 A posição relativa das mãos determina se o comando será virar à esquerda, virar à direita, acelerar ou dar ré.  

### 3️⃣ Simulação dos Comandos  
📌 Com base na análise dos gestos, o módulo *keyboardControl.py* simula os comandos do teclado (W, A, S, D), que são enviados ao jogo.  
📌 O feedback visual na tela auxilia no entendimento das ações executadas.  

### 4️⃣ Feedback Visual  
📌 Elementos gráficos, como círculos e linhas, são desenhados sobre a imagem capturada para indicar as áreas de controle e os gestos reconhecidos.  
📌 Esse feedback permite ajustes em tempo real para um melhor desempenho do controle.  

### 5️⃣ Encerramento  
📌 O sistema pode ser encerrado a qualquer momento pressionando a tecla **"q"**.  

---

## 🚀 Instalação e Execução

🔹 Clone o repositório:

```bash
git clone https://github.com/marcosbrunomendes/DriveHandCar.git
```

🔹 Acesse o diretório do projeto:

```bash
cd DriveHandCar
```

🔹 Instale as dependências:

```bash
pip install -r requirements.txt
```

🔹 Execute o script principal:

```bash
python projectCar.py
```

---

## 🎯 Dicas Extras

### 🔹 Melhorando a Performance  
✅ Para evitar travamentos, utilize uma câmera externa (*USB*) de boa qualidade.  
✅ No *Windows 11*, algumas câmeras podem ter latência elevada; se necessário, use *DroidCam* ou outra solução para conectar o celular como webcam.  
✅ Caso haja atraso na resposta dos gestos, reduza a resolução da câmera no código.  

### 🔹 Personalizando os Controles  
✅ No arquivo *keyboardControl.py*, você pode modificar as teclas pressionadas para adaptar o sistema a outros jogos.  

### 🔹 Ajustando a Resolução da Janela  
✅ No código *projectCar.py*, a janela que exibe os gestos pode ser redimensionada com:

```python
cv2.namedWindow('Detecção de Mãos', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Detecção de Mãos', 1280, 720)
```

---

🔹 **Autor:** Marcos Bruno Mendes  
🔹 **Repositório:** [GitHub](https://github.com/marcosbrunomendes/DriveHandCar)  

🔥 Divirta-se controlando o *MR RACER* com as mãos! 🚗💨
