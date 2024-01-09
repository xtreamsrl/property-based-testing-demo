import hypothesis.strategies as st
import pytest
from hypothesis import given, settings, Verbosity

from src.PizzaGenerator import calculate_order_total_price, Pizza, Dough, Ingredient, PizzaGenerator


# @given(st.integers(), st.integers())
# @settings(max_examples=50)
# def test_generate_random_pizza_le_than_max_toppings(max_toppings: int, n_ingredients: int):
#     generated_pizza = PizzaGenerator(max_toppings).generate_random_pizza(n_ingredients)
#
#     assert len(generated_pizza.toppings) <= max_toppings
#
#
# @pytest.mark.parametrize("max_toppings, ingredients", [(-2, 3), (3, -2), (-4, -4)])
# def test_negative_values_raise_an_error(max_toppings, ingredients):
#     with pytest.raises(ValueError):
#         _ = PizzaGenerator(max_toppings).generate_random_pizza(ingredients)
#
#
# @st.composite
# def order_composite(draw):
#     n_pizza = draw(st.integers(min_value=0, max_value=100))
#
#     order = [Pizza(
#         dough=draw(st.sampled_from(Dough)),
#         toppings=draw(st.lists(st.sampled_from(Ingredient))),
#         price=draw(st.floats())
#     ) for _ in range(n_pizza)]
#
#     return order
#
#
# @given(order_composite())
# @settings(max_examples=20)
# def test_correct_total_price(order):
#     price = calculate_order_total_price(order)
#     assert sum([pizza.price for pizza in order]) == price
#
#
# @pytest.mark.parametrize('wrong_prices', [float('nan'), float('-inf'), float('+inf'), float('inf'), -10])
# def test_raise_error_for_wrong_prices(wrong_prices):
#     with pytest.raises(ValueError):
#         Pizza(Dough.NORMAL, [Ingredient.POTATO, Ingredient.MUSHROOMS], wrong_prices)


# DEMO SAVER
# @given(st.integers(min_value=0, max_value=200), st.integers(min_value=0, max_value=200))
# @settings(max_examples=50)
# def test_generate_random_pizza_le_than_max_toppings(max_toppings: int, n_ingredients: int):
#     generated_pizza = PizzaGenerator(max_toppings).generate_random_pizza(n_ingredients)
#
#     assert len(generated_pizza.toppings) <= max_toppings
#
#
# @pytest.mark.parametrize("max_toppings, ingredients", [(-2, 3), (3, -2), (-4, -4)])
# def test_negative_values_raise_an_error(max_toppings, ingredients):
#     with pytest.raises(ValueError):
#         _ = PizzaGenerator(max_toppings).generate_random_pizza(ingredients)
#
#
# @st.composite
# def order_composite(draw):
#     n_pizza = draw(st.integers(min_value=0, max_value=100))
#
#     order = [Pizza(
#         dough=draw(st.sampled_from(Dough)),
#         toppings=draw(st.lists(st.sampled_from(Ingredient))),
#         price=draw(st.floats(allow_infinity=False, allow_nan=False, min_value=0))
#     ) for _ in range(n_pizza)]
#
#     return order
#
#
# @given(order_composite())
# @settings(max_examples=20)
# def test_correct_total_price(order):
#     price = calculate_order_total_price(order)
#     assert sum([pizza.price for pizza in order]) == price
#
#
# @pytest.mark.parametrize('wrong_prices', [float('nan'), float('-inf'), float('+inf'), float('inf'), -10])
# def test_raise_error_for_wrong_prices(wrong_prices):
#     with pytest.raises(ValueError):
#         Pizza(Dough.NORMAL, [Ingredient.POTATO, Ingredient.MUSHROOMS], wrong_prices)
