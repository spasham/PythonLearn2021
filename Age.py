from datetime import date

print ("Welcome to age calculator")

age = int(input("Please enter your year of birth: "))
current_year = date.today().year
current_age = current_year - age
print ("your current age is:", current_age) 