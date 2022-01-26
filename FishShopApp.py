from audioop import reverse
from hashlib import new
from operator import attrgetter, itemgetter
from typing import Union, List
from xmlrpc.client import boolean
from cv2 import sort


class Fish:

    def __init__(self, name: str = "Unnamed fish",
                 price_in_uah_per_kilo: float = 0, body_only: boolean = True,
                 weight: float = 0, origin: str = "Unnamed country") -> None:
        self.name = name
        self.price_in_uah_per_kilo = price_in_uah_per_kilo
        self.body_only = body_only
        self.weight = weight
        self.origin = origin


class FishShop:

    is_list_sorted = False

    fish_list = []

    def add_fish(self, fish: Fish):
        max_fish_price_in_list = 0
        for j in self.fish_list:
            if j.price_in_uah_per_kilo > max_fish_price_in_list:
                max_fish_price_in_list = j.price_in_uah_per_kilo
        if max_fish_price_in_list <= fish.price_in_uah_per_kilo:
            self.is_list_sorted = True
        elif max_fish_price_in_list > fish.price_in_uah_per_kilo:
            self.is_list_sorted = False
        self.fish_list.append(fish)
        print("Fish", fish.name, "was added to the list")

    def sort_fish_names_by_price(self):
        self.is_list_sorted = True
        self.fish_list = sorted(
            self.fish_list, key=lambda x: x.price_in_uah_per_kilo)
        print("Fish list was sorted")

    def print_fish_list(self):
        if self.is_list_sorted == True:
            print("Sorted fish list:")
        elif self.is_list_sorted == False:
            print("Unsorted fish list:")

        for index in self.fish_list:
            print("Fish name:", index.name,
                  "\t\tprice:", index.price_in_uah_per_kilo,
                  "\t\tbody only:", index.body_only,
                  "\t\tweight:", index.weight,
                  "kgs\t\torigin:", index.origin)

    def sell_fish(self, fish_name: Fish, weight: float):
        try:
            if weight > fish_name.weight:
                print("You have chosen too much weight for the fish!")
            elif weight == fish_name.weight:
                self.fish_list.remove(fish_name)
                print("All the available", fish_name.name, "was sold")
            elif weight < fish_name.weight:
                fish_name.weight -= weight
                print(weight, "kgs of", fish_name.name, "was sold")
        except:
            print("There is no such fish in fish list!")

    def cast_out_old_fish(self, fsh: Fish):
        try:
            self.fish_list.remove(fsh)
            print("Fish", fsh.name, "was removed from fish list")
        except:
            print("There is no such fish in fish list!")


class Buyer:
    def __init__(self) -> None:
        pass

    amount_of_money = 0

    number_of_bought_fish = 0

    def buy_fish(self):
        pass

    def get_current_money_balance(self):
        pass


class Seller:
    def __init__(self) -> None:
        pass

    earned_money = 0

    number_of_sold_fish = 0

    def sell_fish(self):
        pass

    def get_earned_money():
        pass


fish_shop = FishShop()

fish_1 = Fish("anchovy", 400, True, 200, "Ukraine")
fish_2 = Fish("salmon", 500, False, 400, "Turkey")
fish_3 = Fish("carp", 1000, True, 600,  "China")
fish_4 = Fish("bream", 250, False, 800, "Japan")
fish_5 = Fish("pout", 10, True, 120, "South Africa")

fish_shop.add_fish(fish_1)
fish_shop.add_fish(fish_2)
fish_shop.add_fish(fish_3)
fish_shop.add_fish(fish_4)

fish_shop.print_fish_list()
fish_shop.sort_fish_names_by_price()
fish_shop.print_fish_list()
fish_shop.add_fish(fish_5)
fish_shop.print_fish_list()
