import numpy as np
import pandas as pd

class Paciente:
    def __init__(self, nome, idade, sexo, peso, altura):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.peso = peso
        self.altura = altura

pacientes = {
    "Paciente 1": Paciente("Ana", 28, "Feminino", 65, 1.70),
    "Paciente 2": Paciente("Bruno", 35, "Masculino", 85, 1.80),
    "Paciente 3": Paciente("Carla", 42, "Feminino", 70, 1.65),
    "Paciente 4": Paciente("Daniel", 50, "Masculino", 90, 1.75),
}

l_pacientes = [p.__dict__ for p in pacientes.values()]

df_pacientes = pd.DataFrame.from_records(l_pacientes, index=pacientes.keys())

df_pacientes['IMC'] = df_pacientes.apply(lambda i: i.peso / i.altura ** 2, axis=1)\

media = np.mean(df_pacientes['IMC'])

abaixodopeso = df_pacientes[df_pacientes['IMC'] < 18.5]
pesonormal = df_pacientes[(df_pacientes['IMC'] >= 18.5) & (df_pacientes['IMC'] <= 24.9)]
sobrepeso = df_pacientes[(df_pacientes['IMC'] > 25.0) & (df_pacientes['IMC'] <= 29.9)]
obesidadegrau1 = df_pacientes[(df_pacientes['IMC'] > 30.0) & (df_pacientes['IMC'] <= 34.9)]
obesidadegrau2 = df_pacientes[(df_pacientes['IMC'] > 35.0) & (df_pacientes['IMC'] <= 39.9)]
obesidadegrau3 = df_pacientes[df_pacientes['IMC'] >= 40.0]

percentualabaixodopeso = (len(abaixodopeso) / len(df_pacientes)) * 100
percentualpesonormal = (len(pesonormal) / len(df_pacientes)) * 100
percentualsobrepeso = (len(sobrepeso) / len(df_pacientes)) * 100
percentualobesidadegrau1 = (len(obesidadegrau1) / len(df_pacientes)) * 100
percentualobesidadegrau2 = (len(obesidadegrau2) / len(df_pacientes)) * 100
percentualobesidadegrau3 = (len(obesidadegrau3) / len(df_pacientes)) * 100

print(df_pacientes)
print()
print('Média do IMC da população:', media)
print()
print('% de Pacientes abaixo do peso:', percentualabaixodopeso)
print('% de Pacientes com peso normal:', percentualpesonormal)
print('% de Pacientes com sobrepeso:', percentualsobrepeso)
print('% de Pacientes com obesidade grau 1:', percentualobesidadegrau1)
print('% de Pacientes com obesidade grau 2:', percentualobesidadegrau2)
print('% de Pacientes com obesidade grau 3:', percentualobesidadegrau3)