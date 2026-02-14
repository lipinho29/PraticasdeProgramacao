class Fish(Animal):
    def speak(self): 
        return "Blub"

class ClownFish(Fish):
    pass

class TangFish(Fish):
    pass

dory = TangFish()

"""
A classe TangFish é uma classe filha de Fish, por isso pode acessar speak() da classe Fish.
Esta classe procura primeiro o método de chamada dentro de sua classe e, se não for encontrado, então repete 
a busca por cada nível hierárquico superior.
"""
dory.speak()

nemo = ClownFish()

# ClownFish é uma classe filha de Fish, por isso pode acessar speak() da classe Fish

nemo.speak()

class TangFish(Fish):
    def speak(self):
        return "Hello, I'm a TangFish instance."
    
    dory = TangFish()

# este speak() é da classe TangFish
dory.speak()

"""
Por outro lado, como a classe ClownFish ainda NÃO 
define o speak(), as instâncias de ClownFish ainda estão usando o
speak() da classe pai de Fish.
"""

nemo = ClownFish()
nemo.speak()

# O que acontece quando queremos imprimir a instância nemo?
print(nemo)

#  A declaração print não é fácil de entender, por isso vamos ignorá-la.

class ClownFish(Fish):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return "A ClownFish named "+self.name
    
    nemo = ClownFish('Nemo')

print(nemo)