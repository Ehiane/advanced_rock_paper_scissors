#Things to watch out for:
# '/' - float division, '//' integer division
#Order of priority: P_E_MD_AS_LR
# print(3+3*3/3-3);
# round function helps a lot

# 1 year = 365 days
#        = 52 weeks
#        = 12 months


def calcAgeto90(currentAge):
    """
    get user's current age, subtract from 90, to get years left, 
    convert the age in years to days, months and weeks
    """
    WEEKS = 52;
    DAYS = 365;
    MONTHS = 12;

    age_in_years = int(currentAge);
    years_left = 90 - age_in_years;

    #converting to weeks:
    weeks_left = years_left * WEEKS;
    days_left = years_left * DAYS;
    months_left = years_left * MONTHS;

    return days_left, weeks_left, months_left;

def tip_calculator(bill):
  custom_tip = int(input("How much tip would you like to give? 10, 12, or 15?"));
  custom_tip= 1 + custom_tip/100;
  tip_w_bill = bill * custom_tip;
  split_amount = int(input("How many people to split the bill? "));
  split_amount = tip_w_bill/split_amount;
  bill_per_person = round(split_amount, 2);
  return bill_per_person;

def calc_bmi(height, weight):
  user_bmi = weight / height**2;
  user_bmi = round(user_bmi, 2);
  return user_bmi;

def determine_bmi(height, weight):
    user_bmi = calc_bmi(height, weight);
    if user_bmi < 18.5:
        print(f"Your BMI is {user_bmi}, you are underweight");
    elif user_bmi >= 18.5 and user_bmi < 25:
        print(f"Your BMI is {user_bmi}, you have a normal weight");
    elif user_bmi >= 25 and user_bmi < 30:
        print(f"Your BMI is {user_bmi}, you are slightly overweight.");
    elif user_bmi>= 30 and user_bmi < 35:
        print(f"Your BMI is {user_bmi}, you are obese.");
    elif user_bmi >= 35:
        print("Your BMI is {user_bmi}, you are clinically obese.")

def checkExtra(size, pepperoni, cheese):
    extra_bill = 0
    is_pepperoni = True if pepperoni == "Y" else False;
    is_cheese = True if cheese == "Y" else False;
    
    if is_pepperoni == True and is_cheese == True:
        if(size == "M" or size == "L"):
            extra_bill += 3;
        else:
            extra_bill += 2; #for pepperoni
            extra_bill +=1; #for cheese

    elif is_pepperoni == False and is_cheese == True:
        extra_bill += 1;

    elif is_pepperoni == True and is_cheese == False:
        if(size == "M" or size == "L"):
            extra_bill += 3;
        else:
            extra_bill += 2;
    else:
        pass;

    return extra_bill;
    
def pizzaBill(size, pepperoni, cheese):
    bill = 0;

    if size == "S":
        bill = 15;
        extra = checkExtra(size,pepperoni, cheese);
        bill += extra
        print(f"Your final bill is: ${bill}");

    elif size == "M":
        bill = 20;
        extra = checkExtra(size,pepperoni, cheese);
        bill += extra
        print(f"Your final bill is: ${bill}");
    elif size == "L":
        bill = 25;
        extra = checkExtra(size,pepperoni, cheese);
        bill += extra
        print(f"Your final bill is: ${bill}");

def loveCalc(name1, name2):
    name1,name2 = name1.lower(),name2.lower();
    #truelove
    t_tally = name1.count("t") + name2.count("t");
    r_tally = name1.count("r") + name2.count("r");
    u_tally = name1.count("u") + name2.count("u");
    e_tally = name1.count("e") + name2.count("e");
    first_score = t_tally + r_tally + u_tally + e_tally;

    l_tally = name1.count("l") + name2.count("l");
    o_tally = name1.count("o") + name2.count("o");
    v_tally = name1.count("v") + name2.count("v");
    second_score = l_tally + o_tally +v_tally +e_tally;

    #convert to string
    first_score, second_score = str(first_score), str(second_score);
    total_score = first_score + second_score;
    total_score = int(total_score);
    return total_score;



def main():
  # age = input("What is you current age? ");
  # [days_remaining, weeks_remaining,months_remaing] = calcAgeto90(age);
  # print(f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaing} months left.");

  # print("\n-------------------------------[next function]-----------------------------------\n")

  # total_bill = float(input("What was your total bill? "));
  # each_person_pay = tip_calculator(total_bill);
  # print(f"Each person should pay: ${each_person_pay}");
  # height = float(input("enter your height in m: "))
  # weight = float(input("enter your weight in kg: "))
  # determine_bmi(height, weight);
  # print("\n-------------------------------[next function]-----------------------------------\n")

  # print("Welcome to Python Pizza Deliveries!")
  # size = input("What size pizza do you want? S, M, or L ")
  # add_pepperoni = input("Do you want pepperoni? Y or N ")
  # extra_cheese = input("Do you want extra cheese? Y or N ")
  # pizzaBill(size, add_pepperoni, extra_cheese);
#   print("Welcome to the Love Calculator!")
#   name1 = input("What is your name? \n")
#   name2 = input("What is their name? \n")

  
#   score = loveCalc(name1, name2);
#   if score < 10 or score > 90:
#     print(f"Your score is {score}, you go together like coke and mentos.");
#   elif score >= 40 and score <=50:
#     print(f"Your score is {score}, you are alright together.");
#   else:
#     print(f"Your score is {score}.");

    pass;
    fruits = ["apple","cherry","mango"];
    vegetables = ["celery", "potatoes", "tomatoes"];
    fruits_veg = [fruits,vegetables];
    print(fruits_veg);

main();