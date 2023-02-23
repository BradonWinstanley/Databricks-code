# Databricks notebook source
print("hello world")

# COMMAND ----------

# Strings
First_name = "Brandon"
Last_name = "Winstanley"
print(First_name + " " + Last_name)

# Booleans
bool1 = True
bool2 = False
print(bool1)

# Integers
int1=1
int2=10
int3=100
print(int1+int2)

# Floats
float1=1.1
float2=2.2
float3=3.3
print (float3-float1)

# Lists
list1 = ("Bacon", "Tomato", "Sausage", "Egg")
print (list1)

# COMMAND ----------

number1 = input("please neter input")
number2 = input ("please enter second number")

print(int(number1) + int(number2))

# COMMAND ----------

varname = "variable"
var2name = 14
var2name = var2name-2

print(var2name)

# COMMAND ----------

num1 = 10
num2 = 16

print(num1 == num2)#equl to
print(num1 < num2)#less than
print(num1 > num2)#greater than
print(num1 != num2)#not equal to
print(num1 <= num2)#not less than
print(num1 >= num2)#not greater than

or and #'or' and 'and' can also be used

# COMMAND ----------

num1 = 17
num2 = 10

if num1<num2:
    print("first number is less than the second")
elif num1 == num2:
    print("the numbers are equal")
else:
    print("first number is greater than the second")


# COMMAND ----------

#TASK: Ask for two numbers to be input, then display the greatest

number1 = input("please eneter input")
number2 = input ("please enter second number")

if number1>number2:
    print(number1)
elif number1 == number2:
    print("One is not greater than the other, the numbers are equal")
else:
    print(number2)

# COMMAND ----------

#TASK: Write some code that will output to the screen if you were born was a leap year (Assuming leap years are divisable by 4)
number1 = input("please eneter your birth year")

if number1 % 4 == 0:
    print("You were born on a leap year")
else:
    print("You were not born on a leap year")
    
#Solution
inputyear = input("What year were you born?")

if(int(inputyear) % 4==0):
    print("leap year")
else:
    print("not a leap year")

# COMMAND ----------

products = [1,2,3,4,5,6,7,8,8,18,"foo bar",18,24,24,3]

for counter in range(len(products)):
    print(counter, products[counter])
    
# Script will print items in the list

# COMMAND ----------

# while is used to run script continuously until citeria is met
count = 1
while count < 10:
    print(count)
    count += 1

# COMMAND ----------



# COMMAND ----------

#Task
# Ask the user to enter a series of numbers
# Create a total by adding each number to the last
# Stop adding numbers when the user types zero
# Print out the total at the end

#while True:
    #numbers = input("Enter number. When finished, type 'Calculate'")
   # if numbers != "Calculate":
        #print ("enter another number")
        #continue
    #print ("Calculating")
    #break
    
#SOLUTION



        
    

    
    

# COMMAND ----------

#DAY TWO

# COMMAND ----------

round # round numbers
eval # allows integers and strings to be combined
import (random.randint(1,10)) #creates random number between 1-10

# COMMAND ----------

def square():
    print("hellow world")
    print("hellow world")
    print("hellow world")
    print("hellow world")
    print("hellow world")
    print("hellow world")
    print("hellow world")
    
square()

# COMMAND ----------

#TASK - create a function that converts pounds to kilograms (1kg=2.2lb)

pounds = input("Please enter pounds to be converted")

print (pounds, "lbs into KG is", (int(pounds))*0.454)

# COMMAND ----------

Ans = input("Do you want to convert pounds or kilograms?")

if Ans == "pounds":
    pounds = input("Please enter pounds to be converted")
    print (pounds, "lbs into KG is", (int(pounds))*0.454)

else:
    kilograms = input("Please enter kilograms to be converted")
    print (kilograms, "KGs into lbs is", (int(kilograms))*2.2)

# COMMAND ----------

#TASK - create a function that converts fahrenheit to celcius (fh -32*5/9)

fah = input("Please enter temperature in Fahrenheit to be converted to Celcius")

print(fah, "Fahrenheit into Celcius is", ((int(fah)-32)*0.5556))

# COMMAND ----------

mylist = ["i", "d", "l", "e"]

#del mylist[1:4]            :Deleted last two in list
#mylist[1]="n"              :Replaces item 1 with "n"
#newlist = ["s"] = mylist   :Adds item to list
#newlist.append("g")        :adds item to the end
#newlist.insert(1, "t")     :inserts item. first place and second item

finallist = []
for i in mylist:
    print(i, mylist.index(i))
    finallist.append(mylist.index(i))
    
print(finallist)

print(sum(finallist))
print(len(finallist))


# COMMAND ----------

#TASK
# create a list with 10 integers that the user has entered
# calculate and display the sum and average of the numbers in this list
# display each number in turn, with a message stating if it is above below or equal to the average
#e.g 10 is above average

#SOLUTION

user_input = []

for i in range(10):
    print(i)
    input_number = 
    
    

# COMMAND ----------

#DAY2 AFTERNOON

# COMMAND ----------

#Return a String as an Integer
string_int=int
string_int("1000")


# COMMAND ----------

#Is the Word Singular or Plural?
def is_plural(word):
	return word[-1] == "s"

is_plural("changes")

# COMMAND ----------

# Return the First Element in a List
def get_first_value(number_list):
	return number_list[0]
get_first_value([-500, 0, 50])

# COMMAND ----------

#50-30-20 Strategy
def fifty_thirty_twenty(ati):
	x = 0.3 * ati
	y = 0.2 * ati
	z = 0.5 * ati
	return {"Needs":z, "Wants":x,"Savings":y}
fifty_thirty_twenty(1000)

# COMMAND ----------

#DAY 3

# COMMAND ----------

#Dice Rolling Simulator

from random import randint
repeat = True
while repeat:
    print("You rolled",randint(1,6))
    print("Do you want to roll again?")
    repeat = ("y" or "yes") in input().lower()

# COMMAND ----------

#Guess The Number

#import random
#number = random.randrange(1,10)
#guess = input (eval("Enter any number: "))
                                         #input = eval("Enter any number: ")
#while number != guess:
    #if guess < number:
        #print("Too low")
        #guess = int(input("Try again: "))
    #elif number > guess:
        #print ("Too high")
        #guess = int(input("Try again: "))
    #else:
        #break
#Print (("Correct, my number was:"), number)

# COMMAND ----------

import random
number = random.randint(1, 10)

player_name = input("Hello, What's your name?")
number_of_guesses = 0
print('okay! '+ player_name+ ' I am Guessing a number between 1 and 10:')

while number_of_guesses < 5:
    guess = int(input())
    number_of_guesses += 1
    if guess < number:
        print('Your guess is too low')
    if guess > number:
        print('Your guess is too high')
    if guess == number:
        break
if guess == number:
    print('You guessed the number in ' + str(number_of_guesses) + ' tries!')
else:
    print('You did not guess the number, The number was ' + str(number))

# COMMAND ----------

#Mad Libs Generator

loop = 1
while (loop < 10):
#All the questions that the program asks the user
    noun = input("Choose a noun: ")
    p_noun = input("Choose a plural noun: ")
    noun2 = input("Choose a noun: ")
    place = input("Name a place: ")
    adjective = input("Choose an adjective (Describing word): ")
    noun3 = input("Choose a noun: ")
#Displays the story based on the users input
    print ("------------------------------------------")
    print ("Be kind to your",noun,"- footed", p_noun)
    print ("For a duck may be somebody's", noun2,",")
    print ("Be kind to your",p_noun,"in",place)
    print ("Where the weather is always",adjective,".")
    print ()
    print ("You may think that is this the",noun3,",")
    print ("Well it is.")
    print ("------------------------------------------")
#Loop back to "loop = 1"
    loop = loop + 1

# COMMAND ----------


