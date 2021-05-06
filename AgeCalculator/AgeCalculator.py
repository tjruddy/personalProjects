import datetime
name = input("Please enter your name: ")
Year = int(input("Now enter the year you were born: "))
Month = int(input("And now the month e.g 12 = December: "))
Day = int(input("Finally enter the day you were born: "))

DOB = datetime.datetime(Year, Month, Day)
Age = (datetime.datetime.now() - DOB)

convertdays = (Age.days)
AgeYears = convertdays / 365

print(name, "is " + (f"{AgeYears:.2f}") + " years old!")