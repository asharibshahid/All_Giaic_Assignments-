class Temp_Converter:
    def cel_to_heit(c):
        return (c * 9/5) + 32
    
temp_in_f = Temp_Converter.cel_to_heit(37)
print(f"Temperature in Fahrenheit: {temp_in_f} F")    