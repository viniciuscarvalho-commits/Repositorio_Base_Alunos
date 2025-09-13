import pyautogui

pyautogui.press("win") # Abrimos o windows
pyautogui.sleep(1) # Aguardamos 1 segundo
pyautogui.write("calculadora") # Comando para abrir a calculadora
pyautogui.press("enter") # Abrir a calculadora
pyautogui.sleep(1)
pyautogui.write("2+9") # Digito a operação
pyautogui.press("enter") # Pressiona enter
