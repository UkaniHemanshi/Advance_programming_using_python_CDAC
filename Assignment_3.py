age = int(input("Enter your age: "))

if age < 5:
    print("Free Ticket")
elif (age >=5) and (age <=12):
    print("You have to paid RS 5")
elif (age >= 13) and (age <= 60):
    print("You have to paid RS 10")
elif age >60:
    print("You have to paid RS 7")
else:
    print("You are not eligible to purchase ticket")



