class Animal:
    """
    Родительский класс животных
    """
    alive = True  # живой
    fed = False  # накормленный

    def __init__(self, name):
        self.name = name


class Plant:
    """
    Родительский класс растений
    """
    edible = False  # съедобность

    def __init__(self, name):
        self.name = name


class Mammal(Animal):
    """
    Дочерний класс животных (Млекопитающее)
    """
    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False


class Predator(Animal):
    """
    Дочерний класс животных (Хищник)
    """
    def eat(self, food):
        if isinstance(food, Plant) and food.edible:
            print(f"{self.name} съел {food.name}")
            self.alive = True  # Хищник остается живым, если ест съедобное
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False


class Flower(Plant):
    """
    Дочерний класс растений (Цветок)
    """
    pass  # Цветы по умолчанию не съедобные


class Fruit(Plant):
    """
    Дочерний класс растений (Фрукт)
    """
    edible = True  # Фрукты съедобные


# Создание экземпляров
a1 = Predator('Волк с Уилл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семи цветик')
p2 = Fruit('Заводной апельсин')

# Вывод информации
print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)

# Хищник пытается съесть цветок (не съедобный)
a1.eat(p1)

# Млекопитающее пытается съесть фрукт (съедобный)
a2.eat(p2)

# Вывод состояния после еды
print(a1.alive)
print(a2.fed)
