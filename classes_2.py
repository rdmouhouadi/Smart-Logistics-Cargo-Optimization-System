# Base class
class Weighable:
    def weight(self):
        '''Returns the weight. Should be implemented by subclasses.'''
        raise NotImplementedError("Subclasses must implement this method.")

# Part 1
class Item(Weighable):

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

# Part 2
class Suitcase(Weighable):

    def __init__(self, max_weight):
        # Maximum weight of the suitcase
        self.__max_weight = max_weight
        
        # list to hold the items stored in the suitcase
        self.__items = []
    
    def add_item(self, item):
        '''This function adds an item to the suitcase if suitcase total weight doesn't exceed the maximum weight'''
        current_weight = self.weight()
        if current_weight + item.weight() <= self.__max_weight:
            self.__items.append(item)
    
    def __str__(self):
        '''returns the following format : ".. items (..kg)"'''
        total_weight = self.weight()

        # returns grammatically correct string if there's only 1 item
        if len(self.__items) == 1:
            return f"1 item ({total_weight} kg)"
        else:
            return f"{len(self.__items)} items ({total_weight} kg)"
        
    #-------Part 4 ------------------------------------
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
        '''returns the or one of the heaviest items in the Suitcase'''

        # returns "None" if there are no items in the Suitcase
        if not self.__items:
            return None
        
        # assume the first item as the heaviest
        heaviest = self.__items[0]
        for item in self.__items:    # loops to find the item position of the actual heaviest item
            if item.weight() > heaviest.weight():
                heaviest = item # updates with the position of the heaviest item found

        return heaviest
