FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5  
def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR 
    celcius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celcius 
def convert_to_fahrenheit(celsius):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit
def main():
    try:
        temp = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        
        if unit == 'C':
            fahrenheit = convert_to_fahrenheit(temp)
            print(f"{temp}°C is {fahrenheit}°F")
        
        elif unit == 'F':
            celsius = convert_to_celsius(temp)
            print(f"{temp}°F is {celsius}°C")
        
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()


