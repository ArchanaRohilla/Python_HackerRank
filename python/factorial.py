num = input("Enter the number : ")

try:
    number=int(num)
    print("Input is an integer number. Number = ", number)
    #fact=1
    try:
        if number>0:
            fact=1
            while number >0:
                fact=fact*number
                number=number-1
            print(f"The factorial is:{fact}")
            
        elif number==0:
            print(f"factorial=1")
        else:
            print(f"negative number")
    except:
        print("wrong input")
        
except:
    print(f"Input is not an integer number.")
        
        
                        
                
# except ValueError:
#     try:
        
#     while number>0:
#         fact=fact*number
#         number=number-1
        
#     print(f"The factorial is:{fact}") 
    
    
# except:
#     print(f"Wrong input")
