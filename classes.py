import uuid
from typing import List


class Item:
    '''
    Base class for any cargo unit.
    An Item can represent a simple package or, through inheritance, a container.
    '''

    def __init__(self, name: str, weight: float, length: float = 0, width: float = 0, height: float = 0,
                 category: str = "general", value: float = 0.0):
        self._id = str(uuid.uuid4())  # unique identifier
        self._name = name
        self._weight = weight
        self._length = length
        self._width = width
        self._height = height
        self._category = category
        self._value = value

    # --- Getters ---
    def get_id(self) -> str:
        return self._id

    def get_name(self) -> str:
        return self._name

    def get_weight(self) -> float:
        '''Base items just return their weight (containers will override)'''
        return self._weight

    def get_volume(self) -> float:
        return self._length * self._width * self._height

    def get_category(self) -> str:
        return self._category

    def get_value(self) -> float:
        return self._value

    def __str__(self) -> str:
        return (f"Item[{self._id[:6]}]: {self._name}, "
                f"Weight={self._weight}kg, Volume={self.get_volume():.2f}m³, "
                f"Category={self._category}, Value=${self._value:.2f}")


class Container(Item):
    '''
    A container is also an Item, but it can hold multiple Items (composition).
    '''

    def __init__(self, name: str, max_weight: float, max_volume: float,
                 length: float = 0, width: float = 0, height: float = 0):
        # initialize as an Item with weight=0 (container's own structural weight can be added if needed)
        super().__init__(name, weight=0, length=length, width=width, height=height, category="container")
        self._max_weight = max_weight
        self._max_volume = max_volume
        self._items: List[Item] = []

    def add_item(self, item: Item) -> bool:
        '''Attempt to add an item, return True if successful.'''
        if self.get_weight() + item.get_weight() > self._max_weight:
            return False
        if self.get_volume() + item.get_volume() > self._max_volume:
            return False
        self._items.append(item)
        return True

    def remove_item(self, item_id: str) -> bool:
        ''' Remove an item by ID.'''
        for i, it in enumerate(self._items):
            if it.get_id() == item_id:
                del self._items[i]
                return True
        return False

    def get_weight(self) -> float:
        '''Return combined weight of items inside.'''
        return sum(it.get_weight() for it in self._items)

    def get_volume(self) -> float:
        '''Return combined volume of items inside.'''
        return sum(it.get_volume() for it in self._items)

    def get_value(self) -> float:
        '''Return total value of contained items.'''
        return sum(it.get_value() for it in self._items)

    def list_items(self) -> List[Item]:
        return self._items.copy()

    def get_utilization(self) -> dict:
        '''Return utilization percentages for weight and volume.'''
        return {
            "weight": self.get_weight() / self._max_weight * 100 if self._max_weight else 0,
            "volume": self.get_volume() / self._max_volume * 100 if self._max_volume else 0
        }

    def __str__(self) -> str:
        util = self.get_utilization()
        return (f"{self.get_name()} (Container): {len(self._items)} items, "
                f"Weight {self.get_weight():.2f}/{self._max_weight}kg ({util['weight']:.1f}%), "
                f"Volume {self.get_volume():.2f}/{self._max_volume}m³ ({util['volume']:.1f}%)")


class RefrigeratedContainer(Container):
    '''Specialized container for perishable goods '''

    def __init__(self, name: str, max_weight: float, max_volume: float, min_temp: float):
        super().__init__(name, max_weight, max_volume)
        self._min_temp = min_temp

    def check_temp_range(self, current_temp: float) -> bool:
        return current_temp <= self._min_temp

    def __str__(self) -> str:
        return f"Refrigerated {super().__str__()} | Min Temp: {self._min_temp}°C"


class HazardousMaterialContainer(Container):
    '''Specialized container for hazardous goods '''

    def __init__(self, name: str, max_weight: float, max_volume: float, hazard_classes: list[str]):
        super().__init__(name, max_weight, max_volume)
        self._hazard_classes = hazard_classes

    def validate_hazards(self, item: Item) -> bool:
        return item.get_category() in self._hazard_classes

    def __str__(self) -> str:
        return f"Hazardous {super().__str__()} | Hazards: {self._hazard_classes}"


class CargoHold(Container):
    '''
    CargoHold is a specialized large Container.
    It can hold other containers and provides additional reporting.
    ''' 

    def __init__(self, name: str, max_weight: float, max_volume: float):
        super().__init__(name, max_weight, max_volume)

    def get_efficiency_report(self) -> str:
        util = self.get_utilization()
        return (f"CargoHold Efficiency Report:\n"
                f"  - Total Weight: {self.get_weight():.2f}/{self._max_weight}kg ({util['weight']:.1f}%)\n"
                f"  - Total Volume: {self.get_volume():.2f}/{self._max_volume}m³ ({util['volume']:.1f}%)\n"
                f"  - Total Value: ${self.get_value():.2f}")
