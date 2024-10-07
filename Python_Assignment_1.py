# # Exercise 1 Write Python code that prints your name, student number and email address.
Name = "Winston"
Student_Number = "ST1001"
Email_address = "winston@gmail.com"
print("Name:"'Winston')
print("Student_Number:"'ST1001')
print("Email_address:"'winston@gmail.com')


# # Exercise 2 Write Python code that prints your name, student number and email address using escape sequences.
print(f"\tName: {'Winston'}\n\tStudent Number: {'ST1001'}\n\tEmail Address: {'winston@gmail.com'}")


# # Exercise 3 Write Python code that add, subtract, multiply and divide the two numbers.You can use the two numbers 14 and 7.
a=14+7
s=14-7
m=14*7
d=14/7
print(a,s,m,d)


# # Exercise 4 Write Python code that displays the numbers from 1 to 5 as steps.Display numbers from 1 to 5 as steps
print("1")
print(" 2")
print("  3")
print("   4")
print("    5")


# # Exercise 5 Write Python code that outputs the following sentence (including the quotation marks and line break) to the
# # screen: An example runs of the program: "SDK" stands for "Software Development Kit", whereas "IDE" stands for "Integrated
# # Development Environment".
# # Output the sentence with quotation marks and a line break
print('"SDK" stands for "Software Development Kit", whereas \n"IDE" stands for "Integrated Development Environment".')


# # Exercise 6 Practice and check the output print("python is an \"awesome\" language.") print("python\n\t2023")
# # print('I\'m from Entri.\b') print("\65") print("\x65") print("Entri", "2023", sep="\n") print("Entri", "2023", sep="\b")
# # print("Entri", "2023", sep="*", end="\b\b\b\b")
print("python is an \"awesome\" language.")
print("python\n\t2023")
print('I\'m from Entri.\b')
print("\65")
print("\x65")
print("Entri", "2023", sep="\n")
print("Entri", "2023", sep="\b")
print("Entri", "2023", sep="*", end="\b\b\b\b")
print()


# # Exercise 7 Define the variables below. Print the types of each variable. What is the sum of your variables?
# # (Hint: use a type conversion function.) What datatype is the sum? num=23 textnum="57" decimal=98.3
num=23
textnum="57"
decimal=98.3
print("Type of num:", type(num))
print("Type of textnum:", type(textnum))
print("Type of decimal:", type(decimal))
sum1=num + int(textnum) + decimal
print("Sum:", sum1)
print("Type of sum:", type(sum1))


# # Exercise 8 calculate the number of minutes in a year using variables for each unit of time. print a statement that
# # describes what your code does also. Create three variables to store no of days in a year, minute in a hour,
# # hours in a day, then calculate the total minutes in a year and print the values (hint) total number of minutes
# # in an year =No.of days in an year * Hours in a day * Minutes in an    hour Exercise
no_of_days_in_a_year=365
hours_in_a_day=24
minutes_in_an_hour=60
total_number_of_minutes_in_a_year = no_of_days_in_a_year * hours_in_a_day * minutes_in_an_hour
print("This code calculates the total number of minutes in a year.")
print("Total minutes in a year:", total_number_of_minutes_in_a_year)



# Exercise 9 Write Python code that asks the user to enter his/her name and then output/prints his/her name with a greeting.
# An example runs of the program: Please enter you name: Tony Hi Tony, welcome to Python programming :)
Name=input("Enter your name:")
print(f"Hi {Name},Good Morning")



# Exercise 10 in file PoundsToDollars