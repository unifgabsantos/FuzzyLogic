import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
from skfuzzy import control as ctrl

#Variaveis de Entrada (Antecedent)
calorias = ctrl.Antecedent(np.arange(0, 2001, 5), 'Calorias')
perdaCalorica = ctrl.Antecedent(np.arange(100, 600, 1), 'Perda Calorica')
#Variaveis de saída (Consequent)
Peso = ctrl.Consequent(np.arange(20, 140, 1), 'Peso')

# automf -> Atribuição de categorias automaticamente
calorias.automf(names=["Pouco","Razoável","Bastante"])
Peso.automf(names=["Peso Leve","Peso Médio","Pesado"])
perdaCalorica.automf(names=["Pouco","Razoável","Bastante"])
#Visualizando as variáveis
'''calorias.view()
Peso.view()
perdaCalorica.view()'''
#Criando as regras
regra_1 = ctrl.Rule(calorias['Pouco'] | perdaCalorica['Bastante'],Peso['Peso Leve'])
regra_2 = ctrl.Rule(calorias['Razoável'] | perdaCalorica['Razoável'],Peso['Peso Médio'])
regra_3 = ctrl.Rule(calorias['Bastante'] | perdaCalorica['Pouco'],Peso['Pesado'])

controlador = ctrl.ControlSystem([regra_1, regra_2, regra_3])

#Simulando
CalculoPeso = ctrl.ControlSystemSimulation(controlador)

CalculoPeso.input['Calorias'] = int(input('Calorias: '))

CalculoPeso.input['Perda Calorica'] = int(input('Perda Calorica: '))

CalculoPeso.compute()

valorPeso = CalculoPeso.output['Peso']
print(f"\nPeso: {round(valorPeso,2)}")
calorias.view(sim=CalculoPeso)
Peso.view(sim=CalculoPeso)
plt.show()