from abc import abstractmethod, ABC

class Animal(ABC):
    '''
    We created an abstract class
    '''
    def __init__(self, name: str, height: int, weight: int):
        self._name = name
        self._height = height
        self._weight = weight

    @property
    def name (self):
        return self._name

    @name.setter
    def name (self, name: str):
        if name == "":
            print("Name cannot be empty")
        else:
            self._name = name

    @property
    def height (self):
        return self._height

    @height.setter
    def height (self, height: int):
        if height < 0:
            print("Height cannot be negative")
        else:
            self._height = height

    @property
    def weight (self):
        return self._weight

    @weight.setter
    def weight (self, weight: int):
        if weight < 0:
            print("Weight cannot be negative")
        else:
            self._weight = weight

    @abstractmethod
    def sound (self):
        pass


# Create a dog class that inherits from Animal
class Dog(Animal):
    def __init__(self, name, height, weight):
        super().__init__(name, height, weight)
    '''
    Uncomment the code below to see if the Dog class can be instantiated!
    '''    
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

class Kitty(Animal):
    def __init__(self, name, height, weight, sound):
        super().__init__(name, height, weight)
        self._sound = sound

    @property
    def sound (self):
        return self._sound
    
    @sound.setter
    def sound(self, sound: str):
        self._sound = sound

def speakAnimal(animal: Animal):
    '''
    Try commenting out the @abstractmethod decorator in the Animal class and see what happens
    '''
    print(f'{animal.name} says {animal.sound}')

if __name__ == "__main__":
    print("Instantiating a Kitty object")
    tom = Kitty("Tom", 10, 12, "Meow")
    if tom: # If tom is not None
        print(f'{tom.name} is {tom.height} inches tall and {tom.weight} pounds and says {tom.sound}.')
        print("Notice how we can instantiate a Kitty object? This is because we implemented the abstractmethod. \n")
        print("Instantiating a Dog object")
    
    
    try:
        kaya = Dog("Kaya", 12, 15)
        print(f'{kaya.name} is {kaya.height} inches tall and {kaya.weight} pounds.')
    except Exception as e :
        print("Error occurred when instantiating a Dog object")
        print("Notice how we cannot instantiate a Dog object? This is because we did not implement the abstractmethod")
        print(e)