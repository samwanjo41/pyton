from datetime import date
import random 
import datetime

awarded = []
remaining = []
compartment_number = 1
user_details = []

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
def enter_details():
    name = input("name: ")
    dob = input("Date of birth: ")    
    mob = input("Month of birth in number: ") 
    Id = input("Id No: ")
    telNo = input("Telephone number: ") 

    if(name == ''):
        print("Name cannot be blank")
        enter_details()

    date = int(dob)
    if(date <= 0 or date >31):
        print("Invalid date. Please enter a date from 1 to 31")
        enter_details()
    
    month = int(mob)
    if(month <= 0 or month > 12):
        print("Invalid Month. Please enter month from 1 to 12")
        enter_details()

    user_details.append(name)
    user_details.append(dob)
    user_details.append(mob)
    user_details.append(Id)
    user_details.append(telNo)




# TODO: verify entered date and month is valid


#create a customer object
# r1 = Customer(name, dob, mob, Id, telNo)

# generate compartment number
def cmptmnt_no():
    compartment_number = random.randint(1, 77) 
    print("\n")
    print("Welcome to ABC Supermarket Family\nYou are now elligible for the loyalty points program")
    print ("Your compartment number is {}".format(compartment_number))



def calculate_amount():
# random number to represent user's purchase amount
    # amount = random.randint(100, 10000)  
    print("\n")
    amount = int(input("Enter your shopping amount: "))

    print("\n")
    print("Your shopping amount is: {}".format(amount))
    

# calculate loyalty points after users purchases     
    if(amount >= 100 and amount <= 5000):
        points_awarded = (amount/100) * 1
        awarded.append(points_awarded)
        
    elif(amount > 5000):
        diff = amount - 5000
        points_awarded = (int(diff/100)) * 1.5
        points_awarded = points_awarded + 50
        awarded.append(points_awarded)
    else:
        points_awarded = 0
        awarded.append(points_awarded)

#check if its the user's birthday and apply discount
    dt = datetime.datetime.today()
    day = str(dt.day)
    month = str(dt.month)
    if(user_details[1] == day and user_details[2] == month):
        amount = amount - (amount * 0.1)
    else:
        amount = amount - (amount * 0)

#  redeem loyalty points according to user's choice
    print("\n")
    ans = input("You have {} points.Do you wish to redeem your points\n Y or N: ".format(points_awarded))
    if(ans == "Y" or ans == "y"):        
        points_redeem = int(input("Enter points to be redeemed: "))
        if(points_redeem > points_awarded):
            print("You have insufficient points")
            points_redeem = 0
            remaining.append(points_awarded)
        else:
            points_awarded = points_awarded - points_redeem
            print("You have redeemed {} points.\n Points remaining are: {}".format(points_redeem, points_awarded))
            remaining.append(points_awarded)
            
    else:
        print("No points redeemed")
        points_redeem = 0
        remaining.append(points_awarded)

# calculate final tally
    amount = amount - points_redeem    
    print("Total amount to pay is {}".format(amount))
    return amount




def checkout():
    enter_details()
    cmptmnt_no()
    amount = calculate_amount()
    print("\n")
    payment = int(input("Enter Payment option: \n1. Cash\n2. MPesa\n3. Visa-Card\n\t"))
    if(payment == 2 or payment == 3):
        amount = amount - (amount * 0.02)
    else:
        amount = amount -(amount * 0.0)

    date =  datetime.date.today()
    time = datetime.datetime.now().time()

    print("                          ABC SUPERMARKET                                 ")
    print("--------------------------------------------------------------------------")
    print("Name:   {}".format(user_details[0]))    
    print("Date:   {}\t\t\tTime:    {}".format(date, time))
    print("Total Amount:   {} KES".format(amount))
    print("Points earned:   {}".format(awarded))
    print("Points Remaining:   {}".format(remaining))
    # day = birthday()
    dt = datetime.datetime.today()
    day = str(dt.day)
    month = str(dt.month)
    if(user_details[1] == day and user_details[2] == month):
        print("\t\t\t******Happy Birthday {}******".format(user_details[0]))
    

checkout()
