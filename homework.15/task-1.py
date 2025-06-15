year=int(input("Enter number of years: "))
unit=input("""Please choose your option:
1 - Hours.
2 - Days.
3 - Weeks. 
 Your choice is: """)

if unit == "1":
    print(f"{year*8760} hours. ")
elif unit == "2":
    print(f"{year*365} days. ")
elif unit == "3":
    print(f"{year*52} weeks. ")
else:
    print ("Wrong choice. ")

