# # Fahrenheit to Celsius converter

# : User se temperature input lienge
fahrenheit = float(input("Enter temperatre in Fahrenheit: "))

#  Convert Fahrenheit to Celsius
celsius = (fahrenheit - 32) * 5.0 / 9.0

#: Result print karna
print("Temperature:", fahrenheit, "F =", celsius, "C")
