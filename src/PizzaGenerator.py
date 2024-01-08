import math
from dataclasses import dataclass
from enum import Enum, auto
import random
from typing import List


class Ingredient(Enum):
    PEPPERONI = auto()
    PINEAPPLE = auto()
    MUSHROOMS = auto()
    POTATO = auto()
    GORGONZOLA = auto()


class Dough(Enum):
    NORMAL = auto()
    WHOLEMEAL = auto()


@dataclass
class Pizza:
    dough: Dough
    toppings: List[Ingredient]
    price: float

    def __post_init__(self):
        if math.isnan(self.price) | (not 0 <= self.price < float('inf')):
            raise ValueError("Pizza price couldn't be NaN")


class PizzaGenerator:
    def __init__(self, max_toppings: int = 3):
        self.max_toppings = max_toppings

    def generate_random_pizza(self, n_ingredients: int) -> Pizza:
        n_ingredients = min(n_ingredients, self.max_toppings)
        toppings = [random.choice(list(Ingredient)) for _ in range(n_ingredients)]
        dough = random.choice(list(Dough))
        price = random.uniform(0, 30)

        return Pizza(dough, toppings, price)


def calculate_order_total_price(order: List[Pizza]) -> float:
    return sum([pizza.price for pizza in order])