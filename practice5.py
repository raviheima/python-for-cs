# Write a program that asks the user to enter a weight in kilograms. The program should
# convert it to pounds, printing the answer rounded to the nearest tenth of a pound.

weight_in_kg = float(input("Enter your weight in KG:"))
KGToPounds = weight_in_kg * 2.2 
rounded_pounds = round(KGToPounds,1)
print(rounded_pounds)