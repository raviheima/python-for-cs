# Write a program that asks the user how many credits they have taken. If they have taken
# 23 or less, print that the student is a freshman. If they have taken between 24 and 53,
# print that they are a sophomore. The range for juniors is 54 to 83, and for seniors it is 84
# and over
# 84 > senior
# 54 - 83 junior
# 24 - 53 sophomore
# 23 or < freshman
taken_credits = int(input("Enter the total credits you have taken: "))

if taken_credits >= 84:
    print("Your're a Senior")
elif taken_credits >=54 and taken_credits<=83:
    print("You're a Junior")
elif taken_credits >= 24 and taken_credits <=53:
    print("You're a Sophomore")
elif taken_credits <= 23:
    print("Your're a freshman")