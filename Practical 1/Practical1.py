# For my project I am going to create a simply interest calculator
# that can either deal with compound interest or with simple interest

a = str(input("Would you like to compute simple or compound interest? "))
b = a.lower()
years = int(input("How many years are you calculating for? "))
start = float(input("What is the starting amount of money? "))
rate = float(input("What is the percentage interest rate? "))

if b == "compound":
    total = round(start * ((rate+100)/100) ** years, 2)
    interest = total - start
    print(f'The end amount of money is £{total} and the total amount of interest is £{interest}')
elif b == "simple":
    total = round((start + years*((start*(rate+100)/100)-start)), 2)
    interest = total-start
    print(f'The end amount of money is £{total} and the total amount of interest is £{interest}')
else:
    print("Please enter valid values for the interest calaculator")
