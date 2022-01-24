#Math module
import math

#Greeting
print("Welcome to Tom's amazing Scientific Calculator")

#Keeps user inside select menu
while True:
    print("\nChoose the math operation.\n\n0  - Addition\n1  - Subtraction\n2  - Multiplication\n3  - Division\n4  - Modulo\n5  - Raising to a power\n6  - Square Root\n7  - Logarithm\n8  - Sine\n9  - Cosine\n10 - Tangent\n")
    
    #Line for user input
    oper = input("\nEnter the number corresponding with the desired operation: ")
    
    #User chooses Addition
    if oper == "0":
        stilladding = True
    
        while stilladding == True:
            print("\nAddition\n")
            #Takes user values
            val1 = float(input("\nFirst Value: "))
            val2 = float(input("\nSecond Value to add: "))
        
            #Finds summation
            print("\nThe result is: " + str(val1 + val2) + "\n")
        
            #Continue adding?
            adding = input('\nWould you like to add some more numbers? (y/n) ')
            
            if adding == 'y':
                continue
            elif adding == 'n':
                stilladding = False
                break
            else:
                print("\nInvalid Entry\n")
        
        #Continue mathing?
        back = input('\nGo back to the main menu? (y/n) ')
        
        if back == 'y':
            continue
        elif back == 'n':
            break
        else:
            print("\nInvalid Entry!\n")
            continue
    
    #User chooses Subtraction
    elif oper == "1":
        stillminus = True
    
        while stillminus == True:
            print("\nSubtraction\n")
            #Takes user values
            val1 = float(input("\nFirst Value: "))
            val2 = float(input("\nSecond Value to Subtract: "))
        
            #Finds summation
            print("\nThe result is: " + str(val1 - val2) + "\n")
        
            #Continue minusing?
            minus = input('\nWould you like to subtract some more numbers? (y/n) ')
            
            if minus == 'y':
                continue
            else:
                stillminus = False
                break
        
        #Continue mathing?
        back = input('\nGo back to the main menu? (y/n) ')
        
        if back == 'y':
            continue
        elif back == 'n':
            break
        else:
            print("\nInvalid Entry!\n")
            continue
        
    #User chooses Multiplication
    elif oper == "2":
        stilltimes = True
    
        while stilltimes == True:
            print("\nMultiplication\n")
            #Takes user values
            val1 = float(input("\nFirst Value: "))
            val2 = float(input("\nSecond Value to Multiply: "))
        
            #Finds result
            print("\nThe result is: " + str(val1 * val2) + "\n")
        
            #Continue timesing?
            multi = input('\nWould you like to multiply some more numbers? (y/n) ')
            
            if multi == 'y':
                continue
            else:
                stilltimes = False
                break
        
        #Continue mathing?
        back = input('\nGo back to the main menu? (y/n) ')
        
        if back == 'y':
            continue
        else:
            break
    
    #User chooses Division
    elif oper == "3":
        stilldividing = True
    
        while stilldividing == True:
            print("\nDivision\n")
            #Takes user values
            val1 = float(input("\nFirst Value: "))
            val2 = float(input("\nSecond Value to Divide: "))
        
            #Finds result
            print("\nThe result is: " + str(val1 / val2) + "\n")
        
            #Continue dividing?
            divide = input('\nWould you like to divide some more numbers? (y/n) ')
            
            if divide == 'y':
                continue
            else:
                stilldividing = False
                break
        
        #Continue mathing?
        back = input('\nGo back to the main menu? (y/n) ')
        
        if back == 'y':
            continue
        else:
            break
    
    #User chooses Modulo
    elif oper == "4":
        stillmod = True
    
        while stillmod == True:
            print("\nModulo\n")
            #Takes user values
            val1 = float(input("\nFirst value: "))
            val2 = float(input("\nSecond Value to Modulo: "))
        
            #Finds result
            print("\nThe result is: " + str(val1 % val2) + "\n")
        
            #Continue modulo?
            mod = input('\nWould you like to modulo some more numbers? (y/n) ')
            
            if mod == 'y':
                continue
            else:
                stillmod = False
                break
        
        #Continue mathing?
        back = input('\nGo back to the main menu? (y/n) ')
        
        if back == 'y':
            continue
        else:
            break
            
    #User chooses Raise to a power
    elif oper == "5":
        stillpower = True
    
        while stillpower == True:
            print("\nRaising to a Power\n")
            #Takes user values
            val1 = float(input("\nFirst value: "))
            val2 = float(input("\nSecond Value to Raise Power: "))
        
            #Finds result
            print("\nThe result is: " + str(math.pow(val1, val2)) + "\n")
        
            #Continue power?
            power = input('\nWould you like to raise the power of some more numbers? (y/n) ')
            
            if power == 'y':
                continue
            else:
                stillpower = False
                break
        
        #Continue mathing?
        back = input('\nGo back to the main menu? (y/n) ')
        
        if back == 'y':
            continue
        else:
            break
                
    #User chooses Square Root
    elif oper == "6":
        stillsquare = True
    
        while stillsquare == True:
            print("\nSquare Root\n")
            #Takes user value
            val1 = float(input("\nValue for Evaluation: "))
        
            #Finds result
            print("\nThe result is: " + str(math.sqrt(val1)) + "\n")
        
            #Continue square?
            square = input('\nWould you like to find root of some more numbers? (y/n) ')
            
            if square == 'y':
                continue
            else:
                stillsquare = False
                break
        
        #Continue mathing?
        back = input('\nGo back to the main menu? (y/n) ')
        
        if back == 'y':
            continue
        else:
            break
    
    #User chooses Logarithm
    elif oper == "7":
        stilllog = True
    
        while stilllog == True:
            print("\nLogarithm\n")
            #Takes user value
            val1 = float(input("\nValue for Evaluation: "))
        
            #Finds result
            print("\nThe result is: " + str(math.log(val1, 2)) + "\n")
        
            #Continue Logarithm?
            log = input('\nWould you like to continue logarithm? (y/n) ')
            
            if log == 'y':
                continue
            else:
                stilllog = False
                break
        
        #Continue mathing?
        back = input('\nGo back to the main menu? (y/n) ')
        
        if back == 'y':
            continue
        else:
            break
            
    #User chooses Sine
    elif oper == "8":
        stillsine = True
    
        while stillsine == True:
            print("\nSine\n")
            #Takes user value
            val1 = float(input("\nEnter the value (in degrees) for calculating the sine: "))
        
            #Finds result
            print("\nThe result is: " + str(math.sin(math.radians(val1))) + "\n")
        
            #Continue Sine?
            sine = input('\nWould you like to continue calculating sine? (y/n) ')
            
            if sine == 'y':
                continue
            else:
                stillsine = False
                break
        
        #Continue mathing?
        back = input('\nGo back to the main menu? (y/n) ')
        
        if back == 'y':
            continue
        else:
            break
            
    #User chooses Cosine
    elif oper == "9":
        stillcosine = True
    
        while stillcosine == True:
            print("\nCosine\n")
            #Takes user value
            val1 = float(input("\nEnter the value (in degrees) for calculating the cosine: "))
        
            #Finds result
            print("\nThe result is: " + str(math.cos(math.radians(val1))) + "\n")
        
            #Continue Cosine?
            cosine = input('\nWould you like to continue calculating cosine? (y/n) ')
            
            if cosine == 'y':
                continue
            else:
                stillsine = False
                break
        
        #Continue mathing?
        back = input('\nGo back to the main menu? (y/n) ')
        
        if back == 'y':
            continue
        else:
            break
            
    #User chooses Tangent
    elif oper == "10":
        stilltan = True
    
        while stilltan == True:
            print("\nTangent\n")
            #Takes user value
            val1 = float(input("\nEnter the value (in degrees) for calculating the Tangent: "))
        
            #Finds result
            print("\nThe result is: " + str(math.tan(math.radians(val1))) + "\n")
        
            #Continue Tangent?
            tan = input('\nWould you like to continue calculating tangent? (y/n) ')
            
            if tan == 'y':
                continue
            else:
                stilltan = False
                break
        
        #Continue mathing?
        back = input('\nGo back to the main menu? (y/n) ')
        
        if back == 'y':
            continue
        else:
            break
                
    #User inputs invalid option
    else:
        print("\nInvalid Entry!\n")
        continue
        
#End of program