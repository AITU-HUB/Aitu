cart = []

def add_item(cart, name, price, quantity):
    for item in cart:
        if item["name"] == name:
            item["quantity"] += quantity
            return
    cart.append({
        "name": name,
        "price": price,
        "quantity": quantity
    })

def remove_item(cart, name):
    for item in cart[:]:
        if item["name"] == name:
            cart.remove(item)

def update_quantity(cart, name, quantity):
    for item in cart:
        if item["name"] == name:
            item["quantity"] = quantity
            if item["quantity"] == 0:
                cart.remove(item)
            return

def calculate_total(cart):
    total = 0
    for item in cart:
        total += item["price"] * item["quantity"]
    return total

add_item(cart, "apple", 300, 2)
add_item(cart, "banana", 200, 3)
add_item(cart, "apple", 300, 1)
add_item(cart, "onion", 300, 1)

update_quantity(cart, "banana", 3)
update_quantity(cart, "apple", 1)
remove_item(cart, "onion")

print(cart)
print(calculate_total(cart))
