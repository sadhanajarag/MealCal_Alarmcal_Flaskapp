#Part 1:
#Write a program that calculates the total amount of a meal purchased at a restaurant. 
# The program should ask the user to enter the charge for the food and then calculate the amounts with an 18 percent tip and 7 percent sales tax. 
# Display each of these amounts and the total price.

def calculate_total_charges(food_charge):
      
    #Calculate the total amount
    tip = food_charge * 0.18
    sales_tax = food_charge * 0.07
    total_amount = food_charge + tip + sales_tax
    #Display the amount
    print(f"Charge of the food is  : ${food_charge}")
    print(f"Tip(18 %)  : ${tip}")
    print(f"Sales Tax (7%)   : ${sales_tax}")
    print(f"Total amount need to pay  : ${total_amount}")   

def main():
    #Ask the user the charge of food
    food_charge= float(input("Enter the charge of the food : "))
    calculate_total_charges(food_charge)
    

if __name__ == "__main__":
        main()
