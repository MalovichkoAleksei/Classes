#-------------------------------------------------------------------------------
# Name:        HomeWork Classes
# Purpose:
#
# Author:      Cherf
#
# Created:     15.11.2018
# Copyright:   (c) Cherf 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class animal:
    hunger_status = 'хочет есть'
    def feed (self):
        print ('feed an animal')
        self.hunger_status = 'не голодный'
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
    def __lt__(self, other):
        return self.weight < other.weight
    def __repr__(self):
        return 'Максимальный вес {}, кг. у {}'.format(self.weight, self.name)
    def __radd__(self, other):
        return other + self.weight

class milk_animal(animal):
    def get_milk():
        print('Доим молоко')

class shave_animal(animal):
    def shave():
        print('Стрижем')

class birds(animal):
    def eggs():
        print('Собираем яйца')

class cow (milk_animal):
    def __init__(self, name, weight):
        super().__init__( name, weight)
    voice = 'Му МУ'

class goats (milk_animal):
    def __init__(self, name, weight):
        super().__init__(name, weight)
    voice = 'Бе БЕ'

class sheep (shave_animal):
    def __init__(self, name, weight):
        super().__init__(name, weight)
    voice = 'Ме Ме'

class chiken (birds):
    def __init__(self, name, weight):
        super().__init__(name, weight)
    voice = 'Ко Ко Ко'

class duck (birds):
    def __init__(self, name, weight):
        super().__init__(name, weight)
    voice = 'Кря Кря'

class goose (birds):
    def __init__(self, name, weight):
        super().__init__(name, weight)
    voice = 'Га Га Га'

goose_1 = goose('Серый', 20)
goose_2 = goose('Белый', 22)
cow = cow('Манька',200)
sheep_1 = sheep('Барашек', 70)
sheep_2 = sheep('Кудрявый', 75)
chiken_1 = chiken('Ко-Ко' , 12)
chiken_2 = chiken('Кукареку' , 13)
goats_1 = goats('Рога', 50)
goats_2 = goats('Копыта', 50)
duck = duck('Кряква', 15)

all_sum = (goose_1,goose_2,cow,sheep_1,sheep_2,chiken_1,chiken_2,goats_1,goats_2 )
x = sum(all_sum)
print('общий вес животных {} кг.'.format(x))
print(max(all_sum))



