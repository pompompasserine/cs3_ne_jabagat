def calculate_checkout(cart_total, shipping_speed):
    if shipping_speed == "express":
        shipping = 20
    elif shipping_speed == "overnight":
        shipping = 35
    elif shipping_speed == "standard" and cart_total >= 100:
        shipping = 0
    elif shipping_speed == "standard" and cart_total <= 100:
        shipping = 10
    else:
        print("Sorry, dear customer, but there has been an error in your input. Please try again.")
        shipping = 0

    return cart_total + shipping

print(calculate_checkout(4644588, "overnight"))

