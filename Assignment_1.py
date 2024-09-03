year = int(input("Enter the year: "))
if (year%4 == 0 and year%100 != 0) or (year%400 == 0):
    print("Year is leap year !!!")
else:
    print("Year is not leap year !!!")