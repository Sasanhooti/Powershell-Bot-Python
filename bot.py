import datetime
from deep_translator import GoogleTranslator 
import webbrowser
import wikipedia
import random
def time():
    now = datetime.datetime.today()
    mm = str(now.month)
    dd = str(now.day)
    yyyy = str(now.year)
    hour = str(now.hour)
    mi = str(now.minute)
    ss = str(now.second)
    print (mm + "/" + dd + "/" + yyyy + " " + hour + ":" + mi + ":" + ss)
    again()
# Define again() function to ask user if they want to use the time again
def again():
    # Take input from user
    calc_again = input('''
    Do you want to time again?
    Please type Y for YES or N for NO.
    ''')
    # If user types Y, run the time function
    if calc_again.upper() == 'Y':
        time()
    # If user types N, say good-bye to the user and end the program
    elif calc_again.upper() == 'N':
        print('See you later.')
    # If user types another key, run the function again
    else:
        again()
# Call time() outside of the function
    

# kaliboys.com
# This function addition  two numbers
def addition(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y


def trans():
    text = input("what text : ")
    source1 = input( "What language do you write in? ,languogr ,fa, farsi  lamguoge ,en, english:")
    target1 = input("What language do you write in?  ,languogr ,fa, farsi  lamguoge ,en, english:")
    output = GoogleTranslator(source=source1,target=target1).translate(text)
    print(output)
    again()
# Define again() function to ask user if they want to use the calculator again
def again():
    # Take input from user
    calc_again = input('''
    Do you want to calculate again?
    Please type B for YES or C for NO.
    ''')
    # If user types B, run the trans() function
    if calc_again.upper() == 'B':
        trans()
    # If user types B, say good-bye to the user and end the program
    elif calc_again.upper() == 'C':
        print('See you later.')
    # If user types another key, run the function again
    else:
        again()
# Call trans() outside of the function

def web():
    opera = input("Will a new window open or do you want to search? Window ,w, and search ,s,  :")
    sassa = ("w")
    sama = ("s")
    if opera == sassa:
        pp = input("What site are you searching on?  :")
        iila = webbrowser.open(pp)
        print(iila)
    elif opera == sama:
       cc = input("what search ?   :")
       man = webbrowser.open_new_tab(cc)   
       print(man)  
    else:
        print('You have not typed a valid operator, please run the program again.')
    again()
# Define again() function to ask user if they want to use the web again
def again():
    # Take input from user
    calc_again = input('''
    Do you want to web again?
    Please type Y for YES or N for NO.
    ''')
    # If user types Y, run the web() function
    if calc_again.upper() == 'Y':
        web()
    # If user types N, say good-bye to the user and end the program
    elif calc_again.upper() == 'N':
        print('See you later.')
    # If user types another key, run the function again
    else:
        again()
# Call calculate() outside of the function       



def calculate():
    number_1 = int(input("Enter your the first number: "))
    number_2 = int(input("Enter your the second number: "))
    operation = input('''
    Please type in the math operation you would like to complete:
    + for addition
    - for subtraction
    * for multiplication
    / for division
    ''')
    if operation == '+':
        output_number = number_1 + number_2
        print( "{} + {} = {}" .format(number_1, number_2, output_number))
    elif operation == '-':
        output_number = number_1 - number_2
        print( "{} - {} = {}" .format(number_1, number_2, output_number))
    elif operation == '*':
        output_number = number_1 * number_2
        print( "{} * {} = {}" .format(number_1, number_2, output_number))
    elif operation == '/':
        output_number = number_1 / number_2
        print( "{} / {} = {}" .format(number_1, number_2, output_number))
    else:
        print('You have not typed a valid operator, please run the program again.')
    again()
# Define again() function to ask user if they want to use the calculator again
def again():
    # Take input from user
    calc_again = input('''
    Do you want to calculate again?
    Please type Y for YES or N for NO.
    ''')
    # If user types Y, run the calculate() function
    if calc_again.upper() == 'Y':
        calculate()
    # If user types N, say good-bye to the user and end the program
    elif calc_again.upper() == 'N':
        print('See you later.')
    # If user types another key, run the function again
    else:
        again()
# Call calculate() outside of the function


def wiki():
    operator=input("what search ?")
    Iran = wikipedia.summary(operator)
    print (Iran)
       
    again()
# Define again() function to ask user if they want to use the calculator again
def again():
    # Take input from user
    calc_again = input('''
    Do you want to calculate again?
    Please type B for YES or C for NO.
    ''')
    # If user types B, run the wiki() function
    if calc_again.upper() == 'B':
        wiki()
    # If user types B, say good-bye to the user and end the program
    elif calc_again.upper() == 'C':
        print('See you later.')
    # If user types another key, run the function again
    else:
        again()
# Call wiki() outside of the function
    
    

    
        
        
def check_win(user, computer):
    if (user == '1' and computer == '2') or (user == '2' and computer == '3') or (user == '3' and computer == '1'):
        return True

def rock_paper_scissors():
    player = input("SASAN HOOTI....  What is your choice - '1' for rock, '2' for scissor, '3' for paper: ")
    choices = ['1','2','3']
    opponent = random.choice(choices)


    if player == opponent:
        return print(f"good luck !  DRAW pc Choice is  {opponent}")

    if check_win(player, opponent):
        return print(f"OMG ! WINE!  Choice pc is {opponent}")

    if check_win(player, opponent) != True:
        return print(f"ohh noo !.  LOST pc Choice is {opponent}")
    else:
        
        
        
        print('You have not typed a valid operator, please run the program again.')
    again()
# Define again() function to ask user if they want to use the calculator again
def again():
    # Take input from user
    calc_again = input('''
    Do you want to calculate again?
    Please type B for YES or C for NO.
    ''')
    # If user types B, run the rock_paper_scissors() function
    if calc_again.upper() == 'B':
        rock_paper_scissors()
    # If user types B, say good-bye to the user and end the program
    elif calc_again.upper() == 'C':
        print('See you later.')
    # If user types another key, run the function again
    else:
        again()
# Call rock_paper_scissors() outside of the function

def robo():
    print(" ____________")
    print("|1.time      |")
    print("|____________|")
    print("|2.mashin    |")
    print("|____________|")
    print("|3.trans     |")
    print("|____________|")
    print("|4.search    |")
    print("|____________|")
    print("|5.game rock |")
    print("|____________|")
    print("|6.search wi |")
    print("|____________|")
    operator = input("Hello..SASAN..my name is robosan. how i can help you ?")
    nam1 = ("time")
    nam2 = ("khad =")
    nam3 = ("sen =")
    nam4 = ("mashin")   
    nam6 = ( "game rock")  
    nam8 = ("trans")
    nam7 = ("search wi")
    name8 = ("search")  

    if nam1 == operator:
        time()
    elif nam4 == operator:
        calculate()
    elif nam6 == operator:
        rock_paper_scissors()
    elif nam7 == operator:
        wiki()
    elif nam8 == operator:
        trans()
    elif name8 == operator:
        web()
    else:
        
        
        
        
        print('You have not typed a valid operator, please run the program again.')
        again()
# Define again() function to ask user if they want to use the calculator again
def again():
    # Take input from user
    calc_again = input('''
    Do you want again?
    Please type B for YES or C for NO.
    ''')
    # If user types B, run the robo() function
    if calc_again.upper() == 'B':
        robo()
    # If user types B, say good-bye to the user and end the program
    elif calc_again.upper() == 'C':
        print('See you later by....')
    # If user types another key, run the function again
    else:
        again()
# Call robo() outside of the function

def sasanhooti():
    name = input("...Welcome...enter password  :")
    name1 = ("1387331")
    if name == name1:
        robo()
    else:
        print('The password is incorrect, please try again')
        again()
# Define again() function to ask user if they want to use the sasanhooti again
def again():
    # Take input from user
    calc_again = input('''
    Do you want again?
    Please type B for YES or C for NO.
    ''')
    # If user types B, run the sasanhooti() function
    if calc_again.upper() == 'B':
        robo()
    # If user types B, say good-bye to the user and end the program
    elif calc_again.upper() == 'C':
        print('See you later by....')
    # If user types another key, run the function again
    else:
        again()
# Call sasanhooti() outside of the function    

def sasan():
    sasaa = input(">")
    sasasa = ("on")
    if sasaa == sasasa:
        sasanhooti()
        
        
        
sasan()
    