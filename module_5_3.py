print()
print('Задача "Нужно больше этажей"')
print('----------')
print()

class House:
    def __init__(self, name: str, number_of_floors: int):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor: int):
        if new_floor > self.number_of_floors or new_floor < 1:
            print('Такого этажа не существует')
        else:
            for i in range(1, new_floor + 1):
                print(i)
        print()

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors == other

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors < other

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors <= other

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors > other

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors >= other

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors != other

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self
        elif isinstance(value, House):
            self.number_of_floors += value.number_of_floors
            return self

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)

    def __sub__(self, other):
        if isinstance(other, int):
            if other >= self.number_of_floors:
                return 'Такого кол-ва этажей не существует'
            else:
                self.number_of_floors -= other
                return self
        elif isinstance(other, House):
            if other.number_of_floors >= self.number_of_floors:
                return 'Такого кол-ва этажей не существует'
            else:
                self.number_of_floors -= other.number_of_floors
                return self

    def __mul__(self, other):
        if isinstance(other, int):
            self.number_of_floors *= other
            return self
        elif isinstance(other, House):
            self.number_of_floors *= other.number_of_floors
            return self

    def __truediv__(self, other):
        if isinstance(other, int):
            self.number_of_floors = self.number_of_floors // other
            return self
        elif isinstance(other, House):
            self.number_of_floors = self.number_of_floors // other.number_of_floors
            return self

    def __floordiv__(self, other):
        if isinstance(other, float):
            if self.number_of_floors % other != 0:
                return 'Такого кол-ва этажей не существует'
            else:
                self.number_of_floors = self.number_of_floors / other
                return self
        elif isinstance(other, House):
            self.number_of_floors = self.number_of_floors / other.number_of_floors
            return self

h1 = House('ЖК Горский', 10)
h2 = House('Домик в деревне', 20)

# __str__
print(h1)
print(h2)

# __eq__
print(h1 == h2)

# __add__
h1 = h1 + 10
print(h1)
print(h1 == h2)

# __iadd__
h1 += 10
print(h1)

# __radd__
h2 = 10 + h2
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__

# __sub__
h1 = h1 - 10
print(h1)
h2 = h2 - h1
print(h2)

# __truediv__
h1 = h1 / 4
print(h1)
h2 = h2 / h1
print(h2)

# __mul__
h1 = h1 * 2
print(h1)
h2 = h2 * 10
print(h2)

print('----------')