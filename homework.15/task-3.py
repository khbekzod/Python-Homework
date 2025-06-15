# Create a dictionary called country_capitals where the keys are country names and the values are their respective capital cities.
# Prompt the user to enter a country name and print its capital city.

country_capitals={"USA" : "Washington, D.C", "France" : "Paris", "Germany" : "Berlin", "Japan" : "Tokyo", "UK" : "London"}

# print=(input(f"Enter your country {country_capitals}"))
country=(input("Please choose your country from the list: USA, France, Germany, Japan, UK.  "))

if country == "USA":
    print(country_capitals["USA"])
elif country == "France":
    print(country_capitals["France"])
elif country == "Germany":
    print(country_capitals["Germany"])
elif country == "Japan":
    print(country_capitals["Japan"])
elif country == "UK":
    print(country_capitals["UK"])
else:
    print("Please choose from the list")
    
