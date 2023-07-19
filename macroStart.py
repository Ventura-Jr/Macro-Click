import pyautogui
import time

# Define as coordenadas do ponto onde deseja clicar
x = 500
y = 600

# Define a quantidade de cliques a serem realizados
quantidade_cliques = 10

# Define o intervalo de tempo entre os cliques (em segundos)
intervalo = 8

# Aguarda alguns segundos antes de começar
time.sleep(5)

# Realiza os cliques
for _ in range(quantidade_cliques):
    pyautogui.click(x, y)
    time.sleep(intervalo)