from datetime import date
import random 


loyalty_points = 0
compartment_number = 1





# create a class for the customer
class Customer:
    def __init__(self, name, dob, mob, Id, telNo):
        self. name = name
        self.dob = dob
        self.mob = mob
        self.Id = Id
        self.telNo = telNo   

    def dance(self):
        return "{} is now dancing".format(self.name)

# Ask the customer to input their details
name = input("name: ")
dob = input("Date of birth: ")
mob = input("Month of birth: ")
Id = input("Id No: ")
telNo = input("Telephone number: ")

#create a customer object
r1 = Customer(name, dob, mob, Id, telNo)

# Function to check whether the date entered is the customer's birthday
def birthday():
    date_today = 13
    if(r1.dob == str(date_today)):
        return True
        
    else:
        return False


# generate compartment number
def cmptmnt_no():
    compartment_number = random.randint(1, 77) 
    return "Your compartment number is{}".format(compartment_number)


def shopping_amount():
    amount = random.randint(100, 10000)     
    return amount


def loyal_points():
    amount = shopping_amount()
    if(amount >= 100 and amount <= 5000):
        amount = (amount/100) * 1
        
    elif(amount > 5000):
        diff = (amount - 5000)
        amount = (diff/100) * 1.5
    else:
        amount = 0

    print("\n")
    ans = input("You have {} points.Do you wish to redeem your points\n Y or N: ".format(amount))
    if(ans == "Y" or ans == "y"):        
        points = int(input("Enter points to be redeemed: "))
        if(points > amount):
            print("You have insufficient points")
        else:
            amount = amount - points
            print("You have redeemed {}points.\n Points remaining are: {}".format(points, amount))
            return points
    else:
        print("No points redeemed")
        return 0


def amount_to_pay():
    amount = shopping_amount()
    birthdate = birthday()
    if(birthdate == True):
        amount = amount - (amount * 0.1)
        print("Your Total shopping amount is: {}".format(amount))
    else:
        amount = amount - (amount * 0.0)
        print("Your Total shopping amount is: {}".format(amount))
    

    points = loyal_points()

    amount = amount - points
    print("Total amount to pay is {}".format(amount))
    return amount

def checkout():
    amount = amount_to_pay()
    payment = input("Enter Payment option: \n1. Cash\n2. MPesa\n3. Visa-Card")
    if(payment == 2 or payment == "MPesa" or payment == 3 or payment == "Visa-Card\n"):
        amount = amount - (amount * 0.2)
    else:
        amount = amount -(amount * 0.0)

    print("                          ABC SUPERMARKET                                 ")
    print("--------------------------------------------------------------------------")
    print("Name:   {}".format(r1.name))
    print("Date:   {}               Time: {}".format(r1.dob, name))
    print("Amount: {}".format(amount))
    # print("Points: {}".format(points))
    # print("Loyalty Points Bal: {}".format(points))


checkout()