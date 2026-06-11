import math

def main():
    print("This program calculates pH level of a solution.")
    print("Enter 0 to quit the program.")
    hydroxide_ions = float(input("Please input the concentration of hydroxide:"))
    
    while hydroxide_ions > 0:
        hydronium_ions =(10**(-14)/hydroxide_ions)
        pH=(-math.log10(hydronium_ions))
        if pH < 7:
            pH_level = "Acidic"
        elif pH > 7:
            pH_level = "Basic"
        print(f"The pH level of solution {hydroxide_ions} is {pH}. The solution is {pH_level}.")
        return main()
        
    else:
        print("You entered 0, so the program will quit.")
        
main()

