import pyautogui

# Aguarde alguns segundos para você posicionar o mouse na tela desejada
print("Posicione o mouse na tela...")
pyautogui.sleep(5)

# Obtém as coordenadas do mouse
x, y = pyautogui.position()

# Exibe as coordenadas
print(f"Coordenadas: x={x}, y={y}")