# Write a program that asks the user to enter three numbers (use three separate input
# statements). Create variables called total and average that hold the sum and average of the
# three numbers and print out the values of total and average.

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
number3 = float(input("Enter the third number: "))
total = number1 + number2 + number3
average = total / 3

print(f"the total is number is {total} with an average of {average:.2f}")
