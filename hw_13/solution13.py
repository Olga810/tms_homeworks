from collections.abc import Generator


def fibonacci_generator(n: int) -> Generator[int, None, None]:
    """Генератор, возвращающий первые n чисел Фибоначчи."""
    a: int = 0
    b: int = 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Запрос количества чисел у пользователя
try:
    count: int = int(input("Введите количество чисел Фибоначчи для вывода: "))
    if count <= 0:
        print("Пожалуйста, введите положительное число больше нуля.")
    else:
        # Получение последовательности из генератора и вывод на экран
        fib_sequence: list[int] = list(fibonacci_generator(count))
        print(f"Первые {count} чисел Фибоначчи: {fib_sequence}")
except ValueError:
    print("Ошибка: необходимо ввести целое число.")

from typing import Generator


def cycle_generator():
    """Генератор бесконечной циклической последовательности чисел 1-2-3."""
    while True:
        yield 1
        yield 2
        yield 3
        
def main() -> None:
    # Запрос количества элементов у пользователя
    try:
        count: int = int(input("Введите количество чисел для вывода: "))
        if count <= 0:
            print("Пожалуйста, введите положительное число.")
            return
            
        # Инициализация генератора
        gen: Generator[int, None, None] = cycle_generator()
        
        # Вывод заданного количества чисел
        for _ in range(count):
            print(next(gen), end=" ")
        print()  # Перенос строки в конце
        
    except ValueError:
        print("Ошибка: нужно ввести целое число.")

if __name__ == "__main__":
    main()

from abc import ABC, abstractmethod


# 1. Абстрактный класс Animal
class Animal(ABC):

  @abstractmethod
  def speak(self) -> str:
    pass


# 2. Классы Dog и Cat, наследующие от Animal
class Dog(Animal):

  def speak(self) -> str:
    return "Woof!"


class Cat(Animal):

  def speak(self) -> str:
    return "Meow!"


# 3. Класс AnimalFactory с методом create_animal
class AnimalFactory:

  def create_animal(self, animal_type: str) -> Animal:
    animal_type = animal_type.lower()
    if animal_type == "dog":
      return Dog()
    elif animal_type == "cat":
      return Cat()
    else:
      raise ValueError(f"Неизвестный тип животного: {animal_type}")


# Пример:
factory = AnimalFactory()

dog = factory.create_animal("dog")
print(dog.speak())  

cat = factory.create_animal("cat")
print(cat.speak())  
