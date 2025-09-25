# Alot of cell phones have tip calculators. Write one. Ask the user for the price of the meal
# and the percent tip they want to leave. Then print both the tip amount and the total bill
# with the tip included.

meal_price = float(input("Enter the price of the meal: "))
tip_amount = float(input("How many percent tip would you like to leave: "))
tip = meal_price * (tip_amount / 100)
total = meal_price + tip
print(f"Your meal price is :{meal_price}, and a tip of {tip_amount}%  ")
print(f"Tip amount is ${tip:.2f}")
print(f"Total: ${total}")



