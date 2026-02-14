class ClownFish(object):
    pass

nemo = ClownFish()

type(nemo)

isinstance(nemo, ClownFish)

class Animal(object):
    pass

class Vertebrate(Animal):
    pass

class Fish(Vertebrate):
    pass

class ClownFish(Fish):
    pass

class TangFish(Fish):
    pass

nemo = ClownFish()

isinstance(nemo, ClownFish)

# A relação is-a (é-um) é transitiva
isinstance(nemo, Animal)

# Todas as classes têm uma classe pai de Objeto
isinstance(nemo, object)