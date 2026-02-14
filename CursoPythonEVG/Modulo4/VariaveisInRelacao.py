class Fish(Vertebrate):

    # self.name não é definido na classe Fish, mas é definido na classe ClownFish.
    def __str__(self):
        return "Hello, my name is {}".format(self.name)
    
class ClownFish(Fish):
    def __init__(self, name):
        self.name = name

        nemo = ClownFish("nemo")

# O atributo self.name para __str__() é da classe ClownFish
# mas __str__() é da classe Fish
print(nemo)

"""
ERROR, porque se nemo é um exemplo de classe Fish, 
então NÃO tem o atributo do nome.
"""
nemo = Fish()
print(nemo)

class Fish(Vertebrate):
    def __init__(self, name):
        self.name = name

    # self.name não é definido na classe Fish, mas é definido na classe ClownFish.
    def __str__(self):
        return "Hello, my name is {}".format(self.name)
    
class ClownFish(Fish):
    def __init__(self, name):
        self.name = name

        nemo = ClownFish("Nemo")

# __str__() está acessando o self.name a partir do nível filha
print(nemo)

nemo = Fish("clown_fish")

#  __str__ está acessando o atributo self.name da classe Fish
print(nemo)