# Exercise 10 Name your file: PoundsToDollars.py Write a program that asks the user to enter an amount in pounds (£) and
# the program calculates and converts an amount in dollar ($) An example runs of the program: Please enter amount in
# pounds: XXX £ XXX are $ XXX
pounds = float(input("Enter amount in pounds(£):"))
conversion_rate=1.31
dollars = pounds * conversion_rate
print(f"£{pounds} are $ {dollars:}")