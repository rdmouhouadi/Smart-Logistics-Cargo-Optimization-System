'''
My Reasonning:
                - Item: a single object
                - Suitcase and CargoHold: items with the ability of storing other items
'''

# Part 1
class Item:

    def __init__(self, name, weight):
        # private attributes
        self.__name = name
        self.__weight = weight

    def name(self):
        '''a method that returns the item name'''
        return self.__name

    def weight(self):
        '''a method that returns the item weight'''
        return self.__weight

    def __str__(self):
        '''returns attribute (..kg)'''
        return f"{self.__name} ({self.__weight} kg)"

# Part 2, 3, 4, 5
class Suitcase(Item):

    def __init__(self, max_weight):
        # suitcases are unnamed items that contain other items
        super().__init__("suitcase", 0)

        # Maximum weight of the suitcase
        self.__max_weight = max_weight

        # list to hold the items stored in the suitcase
        self.__items = []

    def add_item(self, item):
        '''This function adds an item to the suitcase if total weight doesn't exceed the maximum'''
        current_weight = self.weight()
        if current_weight + item.weight() <= self.__max_weight:
            self.__items.append(item)

    def __str__(self):
        '''returns the following format : ".. items (..kg)"'''
        total_weight = self.weight()

        if len(self.__items) == 1:
            return f"1 item ({total_weight} kg)"
        else:
            return f"{len(self.__items)} items ({total_weight} kg)"

    def print_items(self):
        '''prints out all the items stored in the suitcase'''
        for item in self.__items:
            print(item)

    def weight(self):
        '''returns the total weight of the suitcase'''
        total_weight = 0
        for item in self.__items:
            total_weight += item.weight()
        return total_weight

    def heaviest_item(self):
        '''returns the or one of the heaviest items in the suitcase'''

        # returns "None" if there are no items in the suitcase
        if not self.__items:
            return None

        # assume the first item as the heaviest
        heaviest = self.__items[0]
        for item in self.__items:
            if item.weight() > heaviest.weight():
                heaviest = item
        return heaviest

# Part 6 & 7
class CargoHold(Item):

    def __init__(self, max_weight):
        # cargo hold is an unnamed item holding suitcases
        super().__init__("cargo hold", 0)

        # Maximum weight capacity of the Cargo Hold
        self.__max_weight = max_weight

        # List of all the suitcases stored
        self.__suitcases = []

    def add_suitcase(self, suitcase):
        '''Adds a suitcase if the combined weight does not exceed the cargo hold's max weight'''
        current_weight = self.weight()
        if current_weight + suitcase.weight() <= self.__max_weight:
            self.__suitcases.append(suitcase)

    def __str__(self):
        '''Returns the format: "X suitcase(s), space for Y kg"'''
        count = len(self.__suitcases)

        used_weight = self.weight()
        space_left = self.__max_weight - used_weight

        if count == 1:
            return f"1 suitcase, space for {space_left} kg"
        else:
            return f"{count} suitcases, space for {space_left} kg"

    def print_items(self):
        '''Print out all the items in all the suitcases within the cargo hold'''
        for suitcase in self.__suitcases:
            suitcase.print_items()

    def weight(self):
        '''Returns the combined weight of all suitcases in the cargo hold'''
        total_weight = 0
        for suitcase in self.__suitcases:
            total_weight += suitcase.weight()
        return total_weight
