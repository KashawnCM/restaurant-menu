# Restaurant Menu Ordering Program

A command-line ordering program for a fictional restaurant, **Chef Kash Aroni**, written in Python.

## What it does
- Displays a numbered menu with prices
- Lets the customer order multiple items with quantities
- Validates input (rejects items not on the menu, non-numbers, and quantities of 0 or less)
- Prints an itemized receipt with subtotal, 7% sales tax, and final total

## Concepts used
- Dictionaries for the menu and prices
- Lists and tuples for storing the order
- Functions for each step (menu, ordering, tax, totals, receipt)
- `while` loops and `try/except` for input validation
- f-string formatting for currency

## How to run
Requires Python 3.

```
python restaurant_menu.py
```

## Example
```
Welcome to Chef Kash Aroni!

Menu
1. Wings: $12.00
2. Burger: $10.00
...

Choose an item or type done: burger
How many burgers would you like? 2
2 Burger added to your order.

Choose an item or type done: done

Order for Samurai
2 x Burger: $20.00

Subtotal: $20.00
Tax: $1.40
Total: $21.40
```
