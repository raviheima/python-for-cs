# a program that checks if a user age is within 18 and 79
#if the user age is above 80 or below 18 it prints access denied
#and if the user age is within 18 to 79 it prints access granted
#if the user age is 10 print go home
age = int(input("type your age: " ))
 
if age >= 18 and age <80 :
    print("access granted")
elif age == 10:
    print ("go home")
else:
    print("access denied")

