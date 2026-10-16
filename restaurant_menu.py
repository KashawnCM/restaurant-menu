# Chef Kash Aroni - Restaurant Ordering Program
# Shows a menu, takes an order, validates input, and prints a receipt with tax.

RESTAURANT_NAME = "Chef Kash Aroni"
TAX_RATE = 0.07

menu = {
    "wings": 12.00,
    "burger": 10.00,
    "steak": 25.00,
    "fries": 4.00,
    "salad": 7.00,
    "drink": 3.00
}


def show_menu():
    print(f"\nWelcome to {RESTAURANT_NAME}!")
    print("\nMenu")
    for number, (item, price) in enumerate(menu.items(), start=1):
        print(f"{number}. {item.title()}: ${price:.2f}")


def get_quantity(item):
    while True:
        try:
            quantity = int(input(f"How many {item}s would you like? "))

            if quantity > 0:
                return quantity
            else:
                print("Please enter a number greater than 0.")

        except ValueError:
            print("Please enter a whole number.")


def calculate_item_total(price, quantity):
    return price * quantity


def calculate_tax(subtotal):
    return subtotal * TAX_RATE


def calculate_final_total(subtotal, tax):
    return subtotal + tax


def take_order():
    order = []

    while True:
        choice = input("\nChoose an item or type done: ").lower().strip()

        if choice == "done":
            break

        if choice in menu:
            quantity = get_quantity(choice)
            order.append((choice, quantity))
            print(f"{quantity} {choice.title()} added to your order.")
        else:
            print(f"Sorry, {choice.title()} is not on the menu.")

    return order


def print_receipt(customer_name, order):
    print(f"\nOrder for {customer_name}")

    if len(order) == 0:
        print("No items were ordered.")
        return

    subtotal = 0
    for item, quantity in order:
        item_total = calculate_item_total(menu[item], quantity)
        subtotal += item_total
        print(f"{quantity} x {item.title()}: ${item_total:.2f}")

    tax = calculate_tax(subtotal)
    final_total = calculate_final_total(subtotal, tax)

    print(f"\nSubtotal: ${subtotal:.2f}")
    print(f"Tax: ${tax:.2f}")
    print(f"Total: ${final_total:.2f}")
    print(f"\nThank you for ordering from {RESTAURANT_NAME}!")


if __name__ == "__main__":
    show_menu()
    customer_name = input("\nEnter your name: ")
    order = take_order()
    print_receipt(customer_name, order)
