import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
from skfuzzy import control as ctrl

#Variaveis de Entrada (Antecedent)
calorias = ctrl.Antecedent(np.arange(0, 2001, 5), 'Calorias')

#Variaveis de saída (Consequent)
Peso = ctrl.Consequent(np.arange(0, 30, 1), 'Peso')

# automf -> Atribuição de categorias automaticamente
calorias.automf(names=["Pouco","Razoável","Bastante"])
Peso.automf(names=["Peso Leve","Peso Médio","Pesado"])

#Visualizando as variáveis
calorias.view()
Peso.view()

#Criando as regras
regra_1 = ctrl.Rule(calorias['Pouco'], Peso['Peso Leve'])
regra_2 = ctrl.Rule(calorias['Razoável'], Peso['Peso Médio'])
regra_3 = ctrl.Rule(calorias['Bastante'], Peso['Pesado'])

controlador = ctrl.ControlSystem([regra_1, regra_2, regra_3])

#Simulando
CalculoPeso = ctrl.ControlSystemSimulation(controlador)

notacalorias = int(input('Calorias: '))
CalculoPeso.input['Calorias'] = notacalorias
CalculoPeso.compute()

valorPeso = CalculoPeso.output['Peso']
print(f"\nCalorias: {notacalorias}\nPeso: {valorPeso}")
calorias.view(sim=CalculoPeso)
Peso.view(sim=CalculoPeso)
plt.show()