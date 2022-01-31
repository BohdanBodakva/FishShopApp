from ctypes import Union
from datetime import date
from typing import List


class FishInfo:
    def __init__(self, name, price_in_uah_per_kilo, origin, is_frozen, package_date) -> None:
        self.name = name
        self.price_in_uah_per_kilo = price_in_uah_per_kilo
        self.origin = origin
        self.package_date = package_date
        self.is_frozen = is_frozen


class Fish (FishInfo):
    current_weight = None

    def __init__(self, name: str = "Unnamed fish", price_in_uah_per_kilo: float = 0, origin: str = "Undefined origin", is_frozen: bool = False, package_date: date = date(2022, 1, 1)) -> None:
        super().__init__(name, price_in_uah_per_kilo, origin, is_frozen, package_date)


class FishBox:
    def __init__(self) -> None:
        self.max_weight = 200
        self.current_weight = 0
        self.frozen_fish = []

    def set_max_weight(self, max_weight: float = 100):
        self.max_weight = max_weight


class FishShop:
    def __init__(self) -> None:
        self.fresh_fish = []
        self.fish_box = FishBox()

    def add_fish(self, fish: Fish, weight: float):
        try:
            if weight <= (self.fish_box.max_weight - self.fish_box.current_weight):
                if fish.is_frozen:
                    if not (fish in self.fish_box.frozen_fish):
                        self.fish_box.frozen_fish.append(fish)
                    self.fish_box.current_weight += weight
                    print(weight, "kg of frozen", fish.name, "was added to fish box\t\tfillness:",
                          self.fish_box.current_weight, "/", self.fish_box.max_weight, "kg")
                else:
                    if not (fish in self.fresh_fish):
                        self.fresh_fish.append(fish)
                    print(weight, "kg of fresh", fish.name,
                          "was added to fish box")
            else:
                print("You can add only", (self.fish_box.max_weight -
                      self.fish_box.current_weight), "kg of", fish.name, ", but not", weight, "kg")
        except:
            print("Fish", fish.name, "is unidentified")

    def sell_fish(self, fish: Fish, weight: float):
        try:
            if weight <= self.fish_box.current_weight:
                if fish.is_frozen:
                    self.fish_box.current_weight -= weight
                    print(weight, "kg of frozen", fish.name, "was sold \t\tprofit:", weight*fish.price_in_uah_per_kilo,
                          "hrn\t\tfillness:", self.fish_box.current_weight, "/", self.fish_box.max_weight, "kg")
                else:
                    print(weight, "kg of fresh", fish.name,
                          "was added to fish box")
            else:
                print("You can add only", (self.fish_box.max_weight -
                      self.fish_box.current_weight), "kg of", fish.name, ", but not", weight, "kg")
        except:
            print("Fish", fish.name, "is unidentified")

    def sort_fish_by_price(self):
        new_fish_list = self.fresh_fish + self.fish_box.frozen_fish
        for fish in sorted(new_fish_list, key=lambda x: x.price_in_uah_per_kilo):
            print("Fish:", fish.name, "\t\tprice:",
                  fish.price_in_uah_per_kilo, "\t\torigin:", fish.origin)






fish_1 = Fish("Salmon", 100, "Norway", True, (2022, 1, 20))
fish_2 = Fish("Tuna", 150, "China", True, (2022, 1, 10))
fish_3 = Fish("Carp", 70, "Ukraine", True, (2022, 1, 5))
fish_4 = Fish("Shark", 100, "USA", True, (2022, 1, 20))
fish_5 = Fish("Spike", 100, "Japan", True, (2022, 1, 1))

fish_shop = FishShop()

fish_shop.add_fish(fish_1, 10)
fish_shop.add_fish(fish_2, 10)
fish_shop.add_fish(fish_3, 10)
fish_shop.add_fish(fish_4, 10)
fish_shop.add_fish(fish_5, 10)


fish_shop.sell_fish(fish_1, 5)
fish_shop.sort_fish_by_price()
