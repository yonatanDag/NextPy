class Dog:
    count_animals = 0

    def __init__(self, age, name="Omega"):
        self._name = name
        self._age = int(age)
        Dog.count_animals += 1

    def birthday(self):
        self._age += 1

    def get_age(self):
        return self._age

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name


# def main():
#     dog1 = Dog(5)
#     dog2 = Dog(7, "Haaland")
#     dog1.birthday()
#     dog2.set_name("Foden")
#     print(dog1.get_name(), ", ", dog1.get_age())
#     print(dog2.get_name(), ", ", dog2.get_age())
#     print(Dog.count_animals)
#
#
# if __name__ == "__main__":
#     main()

class Pixel:

    def __init__(self, x, y, red=0, green=0, blue=0):
        self._x = x
        self._y = y
        self._red = red
        self._green = green
        self._blue = blue

    def set_coords(self, x, y):
        self._x = x
        self._y = y

    def set_grayscale(self):
        avg = int((self._red + self._green + self._blue)/3)
        self._red = avg
        self._green = avg
        self._blue = avg

    def print_pixel_info(self):
        count = (self._red == 0) + (self._green == 0) + (self._blue == 0)
        if count == 2 and max(self._red, self._green, self._blue) > 50:
            color = ""
            if self._red > 50:
                color = "Red"
            elif self._blue > 50:
                color = "Blue"
            else:
                color = "Green"
            print("X: ", self._x, ", Y: ", self._y, "Color: (", self._red, ", ", self._green, ", ", self._blue, ") ", color)
        else:
            print("X: ", self._x, ", Y: ", self._y, "Color: (", self._red, ", ", self._green, ", ", self._blue, ")")


# def main():
#     pixel1 = Pixel(5, 6, 250)
#     pixel1.print_pixel_info()
#     pixel1.set_grayscale()
#     pixel1.print_pixel_info()
#
#
# if __name__ == "__main__":
#     main()


class BigThing:

    def __init__(self, parameter):
        self._parameter = parameter

    def size(self):
        if isinstance(self._parameter, int) or isinstance(self._parameter, float):
            return self._parameter
        return len(self._parameter)


class BigCat(BigThing):

    def __init__(self,parameter, weight):
        super().__init__(parameter)
        self._weight = weight

    def size(self):
        if self._weight > 20:
            return "Very Fat"
        elif self._weight > 15:
            return "Fat"
        return "OK"

cutie = BigCat("mitzy", 22)
print(cutie.size())