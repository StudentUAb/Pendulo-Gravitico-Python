# UC: 21048 - Física Geral 
# Ano 2022/23 - EFOLIO B - Gráfico Pêndulo Gravítico - UAb
#  Aluno: 2100927 - Ivo Baptista 

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math

# Constantes
m = 0.0026  # Masa do pendulo convertido em Kg
L = 1.0  # Comprimento da corda em metros
rho = 1.28;  # Massa específica do ar em kg/m^3
# b = 0.01 # Coeficiente de arrasto aerodinâmico
g = 9.81 # Aceleração da gravidade em m/s^2

# Coeficiente de arrasto aerodinâmico para uma esfera
cd = 0.1 
# Raio do pêndulo
R = 0.3 # convertido em metros

# Área frontal da esfera
A = np.pi * R**2;

# Coeficiente de arrasto aerodinâmico
b =  1/2 * rho * cd * A;

# Valores Iniciais 
theta0 = 0.05  # Ângulo inicial em radianos
w0 = 0.0       # Velocidade angular inicial em radianos/s
t0 = 0.0       # Tempo inicial em segundos
h = 0.1        # Passo de tempo em segundos

# Listas para armazenar resultados em arrays
t = [t0]
theta = [theta0]
w = [w0]
k1x_ = 0
k1v_ = 0
k2x_ = 0
k2v_ = 0
k1x = [k1x_] * len(t)
k1v = [k1v_] * len(t)
k2x = [k2x_] * len(t)
k2v = [k2v_] * len(t)

# Loop do tempo
while t[-1] < 100.0:
    # Cálculo dos valores intermediários
    k1x_ = w[-1]
    k1v_ = -math.copysign(1, w[-1]) * (((b*L)/m) * w[-1]**2) - (g / L) * theta[-1]
    k2x_ = w[-1] + k1v_ * h
    k2v_ = -math.copysign(1, w[-1] + k1v_ * h) * (((b*L)/m )* (w[-1] + k1v_ * h)**2) - (g / L) * (theta[-1] + k1x_ * h)
    
    # Atualização dos valores de θ e w
    theta.append(theta[-1] + ((k1x_ + k2x_) / 2.0)*h)
    w.append(w[-1] + ((k1v_ + k2v_) / 2.0)*h)
    
    # Atualização do tempo
    t.append(t[-1] + h)
    
    # Atualiza novos valores para os arrays k1x, k1v, k2x e k2v
    k1x.append(k1x_)
    k1v.append(k1v_)
    k2x.append(k2x_)
    k2v.append(k2v_)
    
# linha para theta com linha vermelha
plt.plot(t, theta, color='red')

# linha para w com linha azul
plt.plot(t, w, color='blue')

# Adicionar uma legenda
plt.legend(['theta', 'w'])

# Adicionar rótulos de eixo
plt.xlabel('t (s)')
plt.ylabel('theta (rad), w (rad/s)')

# Cria um dataframe das listas t, theta e w
df = pd.DataFrame({'t (s)': t, 'theta (rad)': theta, 'w (rad/s)': w, 'k1x': k1x, 'k1v': k1v, 'k2x': k2x, 'k2v': k2v})

# Mostra as primeiras linhas do dataframe no terminal
print(df.head())

# Salva o dataframe em um arquivo CSV
df.to_csv('tabela_resuldados_heun.csv', index=False)

# Mostra o grafico
plt.show()
