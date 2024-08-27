def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9

def main():
    try:
        # Task 1: Ask the user to enter the temperature in Fahrenheit
        fahrenheit = input("Please enter the temperature in Fahrenheit: ")
        
        # Convert the input to a float
        fahrenheit = float(fahrenheit)
        
        # Task 2: Convert the Fahrenheit temperature to Celsius
        celsius = fahrenheit_to_celsius(fahrenheit)
        
        # Task 3: Print the converted temperature in a user-friendly format
        print(f"{fahrenheit} degrees Fahrenheit is {celsius:.2f} degrees Celsius.")
    
    except ValueError:
        # Handle the case where the input is not a valid number
        print("Invalid input. Please enter a numeric value.")
    
    finally:
        # Task 4: Thank the user for using the weather forecast application
        print("Thank you for using the weather forecast application.")

# Run the main function
if __name__ == "__main__":
    main()
