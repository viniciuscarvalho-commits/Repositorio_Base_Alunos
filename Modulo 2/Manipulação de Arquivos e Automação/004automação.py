import pyautogui
import webbrowser
import time

# Passo1: Abrir o youtube com uma música específica
url = "https://www.youtube.com/watch?v=t79rT_lpTf4"
webbrowser.open(url)

# Passo2: Aguardar o carregamento da página
time.sleep(5) # Ajustar de acordo com a velocidade da internet utilizada

# Passo3: Garantir que o vídeo comece(apertar o espaço para o play)
pyautogui.press("space") # Toca ou passa o vídeo