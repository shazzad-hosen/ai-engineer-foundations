from abc import ABC, abstractmethod


# abstract class -> only for inheritance purpuses
class Animal(ABC):
    @classmethod
    @abstractmethod
    # abstract method
    def make_sound(self):
        pass


class Lion(Animal):
    def make_sound(self):
        print("Roar!")


class Snake(Animal):
    def make_sound(self):
        print("Shhh..")


lion = Lion()
lion.make_sound()

snake = Snake()
snake.make_sound()
