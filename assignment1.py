# In this assignment, you will create a simple Linux temperature converter that converts temperatures from Celsius to Fahrenheit. 
# The program will prompt the user to enter a temperature in Celsius, perform the conversion, and then display the result in Fahrenheit.
# This assignment will help you practice basic input/output operations, arithmetic calculations, and string formatting in Python.
import time

print("""
>=============<
|             |
|    HELLO    |
|             |
>=============<
""")

print("Welcome to Linux temperature converter.")

celsius = float(input("Enter the temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.")