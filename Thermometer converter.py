print ("Welcome to my temperature converter.")

class temps():
    def celsius_to_farenheit(self, c):
        return c * 1.8 + 32
    def celsius_to_kelvin(self, c):
        return c + 273.15
    
    def farenheit_to_celsius(self, f):
        return(f - 32) / 1.8
    def farenheit_to_kelvin(self, f):
        return(f + 459.67) / 1.8
    
    def kelvin_to_celsius(self, k):
        return k - 273.15
    def kelvin_to_farenheit(self, k):
        return k * 1.8 - 459.67
    
convert = temps()

while True:
    
    choice = input("Will you be converting from celsius, farenheit, or kelvin? ")

    if choice == "celsius":
        c = float(input("Please enter the temperature in celsius: "))
    
        target = input("Would you like to convert to kelvin or farenheit? ")
    
        if target == "farenheit":
            conversion = convert.celsius_to_farenheit(c)
            print(conversion)
    
        if target == "kelvin":
            conversion = convert.celsius_to_kelvin(c)
            print(conversion)

    elif choice == "farenheit":
        f = float(input("Please enter the temperature in farenheit: "))
    
        target = input("Would you like to convert to celsius or kelvin? ")
    
        if target == "celsius":
            conversion = convert.farenheit_to_celsius(f)
            print(conversion)
    
        if target == "kelvin":
            conversion = convert.farenheit_to_kelvin(f)
            print(conversion)

    elif choice == "kelvin":
        k = float(input("Please enter the temperature in kelvin: "))
    
        target = input("would you like to convert to celsius or farenheit? ")
    
        if target == "celsius":
            conversion = convert.kelvin_to_celsius(k)
            print(conversion)
    
        if target =="farenheit":
            conversion = convert.kelvin_to_farenheit(k)
            print(conversion)

    again = input("Press enter to restart, or type quit to exit.")
    if again.lower() == "quit":
        break

