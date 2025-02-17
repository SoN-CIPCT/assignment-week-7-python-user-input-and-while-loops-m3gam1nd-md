pizza_orders = ['pepperoni', 'sausage', 'extra cheese', 'meat-lovers', 'supreme', 'hawaiian']
finished_pizzas = []

while pizza_orders:
    current_pizza = pizza_orders.pop()
    print(f"Your pizza pie is finished!")
    finished_pizzas.append(current_pizza)

for finished_pizza in finished_pizzas:
    print(f"\nThe pizza {finished_pizza.title()} was made.")