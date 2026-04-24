def calculator():
    while True:
        print("Select operation:")
        print("1. Add")
        print("2. Subtract") 
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        
        choice = input("Enter choice 1-5: ")
        
        if choice == '5':
            print("Bye!")
            break
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
            
        if choice == '1':
                print(f"Result: {num1 + num2}")
        elif choice == '2':
                print(f"Result: {num1 - num2}")
        elif choice == '3':
                print(f"Result: {num1 * num2}")
        elif choice == '4':
            try:
                num1/num2
                print(f"Result: {num1 / num2}") 
            except ZeroDivisionError:
                  print('can not divide by zero') 

        
calculator()





