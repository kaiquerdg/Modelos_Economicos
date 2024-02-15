# A função parametros() calcula manualmente o preço e a quantidade de equilíbrio

# Define os parâmetros das funções
def parametros():
  a = float(input("Digite o intercepto da função de demanda: "))
  b = float(input("Digite a inclinação da função de demanda: "))
  c = float(input("Digite o intercepto da função de oferta: "))
  d = float(input("Digite a inclinação da função de oferta: "))

# Calcula o preço e a quantidade de equilíbrio  
  def preco_quantidade():
    preco_equilibrio_manual = (a - c) / (b + d)
    quantidade_equilibrio_manual = (a * d + b * c) / (b + d)
 
# Verifica se os valores dos parâmetros dão um resultado válido  
    if preco_equilibrio_manual > 0 and quantidade_equilibrio_manual > 0:
        return print("O preço de equilíbrio é", preco_equilibrio_manual,
                 "e a quantidade de equilíbrio é", quantidade_equilibrio_manual)
    else:
        return print("Valores inválidos")
  return preco_quantidade()

parametros()

# Utiliza o grid para encontrar o preço e a quantidade de equilíbrio

# Importa os módulos que precisamos
import matplotlib.pyplot as plt
import numpy as np

# Cria os parâmetros
def parametros_grid(): 
   global a, b, c, d
   a = float(input("Digite o intercepto da função de demanda: "))
   b = float(input("Digite a inclinação da função de demanda: "))
   c = float(input("Digite o intercepto da função de oferta: "))
   d = float(input("Digite a inclinação da função de oferta: "))
 
parametros_grid()

# Cria as funções de oferta e demanda
funcao_demanda = lambda p: a - b * p
funcao_oferta = lambda p: c + d * p

# Calcula o excesso de demanda
excesso_demanda = lambda p: abs(funcao_demanda(p) - funcao_oferta(p))

excesso = []
grid = np.linspace(0, 30, 10000)
for preco in grid:
    excesso.append(excesso_demanda(preco))
  
excesso_minimo = np.argmin(excesso)
preco_eq = grid[excesso_minimo]
demanda_eq = funcao_demanda(preco_eq)

print("O preço de equilíbrio é " + str(preco_eq) + "e a quantidade de equilíbrio é " + str(demanda_eq))

# Cria o gráfico das funções
lista_demanda = []
lista_oferta = []

for preco in grid:
    lista_demanda.append(funcao_demanda(preco))
    lista_oferta.append(funcao_oferta(preco))
    
# Linestyle = "dashed"/"dotted" muda o estilo da linha
fig, ax = plt.subplots(dpi = 500) # Nitidez
ax.plot(lista_demanda, grid, label = "Curva de demanda", color = "green") # Linha demanda
ax.plot(lista_oferta, grid, label = "Curva de oferta", color = "blue") # Linha oferta
ax.plot(demanda_eq, preco_eq, markersize = 5,
        marker = "o", color = "black", label = "Equilíbrio") # Ponto de equilíbrio
ax.legend(bbox_to_anchor=(0.001, 1.05, 0.5, 1.2),
          loc=3, fancybox=True, shadow = False, ncol = 3, borderaxespad=0) # Legenda
ax.set_ylim(0, a + 2) # Intervalo y
ax.set_xlim(0, demanda_eq + 2 ) # Intervalo x
plt.show() # Plota o gráfico