num = int(input("Enter the number: "))
secret_num = 5
i = 1
while i<=10:
    if num == secret_num:
        print("Your are right in guess the number")
        break
    else:
        i+=1
        print("Your are wrong !!! Please try again")
        num = int(input("Enter the number: "))

print("Thank you for playing")
print("Game is over")