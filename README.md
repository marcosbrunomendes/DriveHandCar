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
