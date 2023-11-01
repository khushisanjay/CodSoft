#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# A simple calculator  that performs basic arithmetic operations
# Allows the user to input two numbers and an operation choice and display the result

print("****CALCULATOR ****")


#This function adds two numbers

def addition(a, b):
    return a + b


#This function subtracts two numbers

def subtraction(a, b):
    return a - b


#This function multiplies two numbers

def multiplication(a, b):
    return a * b


#This function divides two numbers

def division(a, b):
    if b == 0:
        return "Cannot divide by zero"  #If b=0 , returns cannot divide by zero to avoid error
    return a / b

print("SELECT YOUR OPERATION")

print(" 1-Addition\n 2-Subtraction\n 3-Multiplication\n 4-Division")

while True:
    choice = int(input("Enter the operation you want to perform:"))

    if choice in (1, 2, 3, 4):     # ensures that the user selects only from the given choices
        try:
            a = float(input("Enter First Number:"))
            b = float(input("Enter Second Number:"))
        except:
            print("Invalid Input. \n Please enter a valid input")
            continue

        if choice == 1:
            print("The addition of two numbers is:", addition(a, b))              
            
        elif choice == 2:
            print("The subtraction of two numbers is:", subtraction(a, b))        
            
        elif choice == 3:
            print("The multiplication of two numbers is:", multiplication(a, b))   
            
        elif choice == 4:
            result = division(a, b)                                                
            if result == "Cannot divide by zero":
                print(result)
            else:
                print("The division of two numbers is:", result)

        continue_operation = input("Do You Want To Continue? (y/n):")
        
        
        if continue_operation.lower() == "n" or continue_operation.lower() == "N":   
            print("PROGRAM FINISHED")
            break
            
        elif continue_operation.lower() == "y" or continue_operation.lower == "Y":
            continue     #continue with the loop
            
        else:
            print("Invalid input. \n Please enter 'y' to continue or 'n' to exit.")   #displays error message to enter 'y' or 'n'
            
    else:
        print("Invalid Input\n Please enter a number between 1-4")


# In[ ]:




