import hypothesis.strategies as st
import pytest
from hypothesis import given, settings

from src.PizzaGenerator import calculate_order_total_price, Pizza, Dough, Ingredient, PizzaGenerator


@given(st.integers(min_value=0), st.integers())
@settings(max_examples=20)
def test_generate_random_pizza_less_than_max_toppings(max_toppings: int, n_ingredients: int):
    generated_pizza = PizzaGenerator(max_toppings).generate_random_pizza(n_ingredients)

    assert len(generated_pizza.toppings) <= max_toppings


@st.composite
def order_composite(draw):
    n_pizza = draw(st.integers())

    order = [Pizza(
        dough=draw(st.sampled_from(Dough)),
        toppings=draw(st.lists(st.sampled_from(Ingredient))),
        price=draw(st.floats(min_value=0, allow_nan=False, allow_infinity=False))
    ) for _ in range(n_pizza)]

    return order


@given(order_composite())
@settings(max_examples=20)
def test_correct_total_price(order):
    price = calculate_order_total_price(order)
    assert sum([pizza.price for pizza in order]) == price


@pytest.mark.parametrize('wrong_prices', [float('nan'), float('-inf'), float('+inf'), float('inf')])
def test_raise_error_for_wrong_prices(wrong_prices):
    with pytest.raises(ValueError):
        Pizza(Dough.NORMAL, [Ingredient.POTATO, Ingredient.MUSHROOMS], wrong_prices)
