class Animal:
    # the name of the zoo
    zoo_name = "Hayaton"

    def __init__(self, name, hunger=0):
        """
        initialize an Animal instance.
        param name: the name of the animal.
        type name: str
        param hunger: the initial hunger level of the animal.
        type hunger: int
        """
        self._name = name
        self._hunger = hunger

    def get_name(self):
        """
        get the name of the animal.
        returns: the name of the animal.
        type: str
        """
        return self._name

    def is_hungry(self):
        """
        check if the animal is hungry.
        returns: True if the animal's hunger level is greater than 0, False otherwise.
        type: bool
        """
        return self._hunger > 0

    def feed(self):
        """
        Reduce the animal's hunger level by 1.
        """
        self._hunger -= 1

    def talk(self):
        """
        Placeholder method for the animal's sound that should be overridden by subclasses.
        """
        pass


class Dog(Animal):
    def talk(self):
        """
        Print the sound a dog makes.
        """
        print("woof woof")

    @staticmethod
    def fetch_stick():
        """
        Print a message indicating the dog has fetched a stick.
        """
        print("There you go, sir!")


class Cat(Animal):
    def talk(self):
        """
        Print the sound a cat makes.
        """
        print("meow")

    @staticmethod
    def chase_laser():
        """
        Print a message indicating the cat is chasing a laser.
        """
        print("Meeeeow")


class Skunk(Animal):

    def __init__(self, name, hunger=0, stink_count=6):
        """
        Initialize a Skunk instance.
        param name: the name of the skunk.
        type name: str
        param hunger: the initial hunger level of the skunk.
        type hunger: int
        param stink_count: the initial stink count of the skunk.
        type stink_count: int
        """
        super().__init__(name, hunger)
        self._stink_count = stink_count

    def talk(self):
        """
        Print the sound a skunk makes.
        """
        print("tsssss")

    @staticmethod
    def stink():
        """
        Print a message indicating the skunk is stinking.
        """
        print("Dear lord!")


class Unicorn(Animal):
    def talk(self):
        """
        Print the sound a unicorn makes.
        """
        print("Good day, darling")

    @staticmethod
    def sing():
        """
        Print a message indicating the unicorn is singing.
        """
        print("I’m not your toy...")


class Dragon(Animal):

    def __init__(self, name, hunger=0, color="Green"):
        """
        Initialize a Dragon instance.
        param name: the name of the dragon.
        type name: str
        param hunger: the initial hunger level of the dragon.
        type hunger: int
        param color: the color of the dragon.
        type color: str
        """
        super().__init__(name, hunger)
        self._color = color

    def talk(self):
        """
        Print the sound a dragon makes.
        """
        print("Raaaawr")

    @staticmethod
    def breath_fire():
        """
        Print a message indicating the dragon is breathing fire.
        """
        print("$@#$#@$")


def main():
    dog = Dog("Brownie", 10)
    cat = Cat("Zelda", 3)
    skunk = Skunk("Stinky")
    unicorn = Unicorn("Keith", 7)
    dragon = Dragon("Lizzy", 1450)
    zoo_lst = [dog, cat, skunk, unicorn, dragon]

    dog2 = Dog("Doggo", 80)
    zoo_lst.append(dog2)
    cat2 = Cat("Kitty", 80)
    zoo_lst.append(cat2)
    skunk2 = Skunk("Stinky Jr.", 80)
    zoo_lst.append(skunk2)
    unicorn2 = Unicorn("Clair", 80)
    zoo_lst.append(unicorn2)
    dragon2 = Dragon("McFly", 80)
    zoo_lst.append(dragon2)

    for animal in zoo_lst:
        if animal.is_hungry():
            print(animal.__class__.__name__,  " ", animal.get_name())
            while animal.is_hungry():
                animal.feed()
        animal.talk()
        if isinstance(animal, Dog):
            animal.fetch_stick()
        elif isinstance(animal, Cat):
            animal.chase_laser()
        elif isinstance(animal, Skunk):
            animal.stink()
        elif isinstance(animal, Unicorn):
            animal.sing()
        elif isinstance(animal, Dragon):
            animal.breath_fire()
    print(Animal.zoo_name)


if __name__ == "__main__":
    main()
