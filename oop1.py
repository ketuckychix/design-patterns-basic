from abc import abstractmethod
class Animal ():
    def __init__(self, name, height, weight):
        self._name = name
        self._height = height
        self._weight = weight
    

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if name == "":
            print("Name cannot be empty")
        else:
            self._name = name
    
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, height):
        if height < 0:
            print("Height cannot be negative")
        else:
            self._height = height

    @property
    def weight(self):
        return self._weight
    
    @weight.setter
    def weight(self, weight):
        if weight < 0:
            print("Weight cannot be negative")
        else:
            self._weight = weight

    
# Create a dog class that inherits from Animal
class Dog(Animal):
    def __init__(self, name, height, weight, sound):
        super().__init__(name, height, weight)
        self._sound = sound
    
    @property
    def sound(self):
        '''
        Extension of super class; returns the sound of the dog
        '''
        return self._sound
    
    @sound.setter
    def sound(self, sound):
        '''
        Extension of super class; sets the sound of the dog
        '''
        self._sound = sound
        


if __name__ == "__main__":
    kaya = Dog("Kaya", 50, 25, "Woof")
    print(kaya.height)
    print(kaya.weight)
    print(kaya.name)
    print(kaya.sound)
    kaya.name = "Kaya2"
    kaya.sound = "Wow wow"
    print(kaya.name)
    print(kaya.sound)