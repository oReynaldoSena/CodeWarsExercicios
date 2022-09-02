#You will be given an array a and a value x. All you need 
# to do is check whether the provided array contains the value.

#Array can contain numbers or strings. X can be either.

#Return true if the array contains the value, false if not.

def check(seq, elem):
    a=0
    for i in seq:
        if i == elem:
            a+=1
    if a!= 0:
        return True
    else: return False

#You get an array of numbers, return the sum of all of the positives ones.

def positive_sum(arr):
    sum = 0 
    for number in arr:
        if number > 0:
            sum += number
    return sum


    #After a hard quarter in the office you decide to get 
    # some rest on a vacation. So you will book a flight for 
    # you and your girlfriend and try to leave all the mess behind you.

#You will need a rental car in order for you to get around in 
# your vacation. The manager of the car rental makes you some good offers.

#Every day you rent the car costs $40. If you rent the car for
#  7 or more days, you get $50 off your total. Alternatively,
#  if you rent the car for 3 or more days, you get $20 off your total.

#Write a code that gives out the total amount for different days(d).

def rental_car_cost(d):
    if d<3:
        return 40*d
    elif (d>3) and (d<7):
        return (40*d)-20
    else: return (40*d)-50


#If we list all the natural numbers below 10 that are 
# multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

#Finish the solution so that it returns the sum     of all 
# the multiples of 3 or 5 below the number passed in. 
# Additionally, if the number is negative, return 0 (for languages that do have them).

#Note: If the number is a multiple of both 3 and 5, only count it once.

def solution(number):
    soma = 0
    for n in range(number):
        if (n % 3) == 0 or (n % 5) == 0 :
            soma += n
    return soma


#Given a random non-negative number, you have to return the digits 
# of this number within an array in reverse order.

def digitize(n):
    num = n
    x = [int(a) for a in str(num)]
    x.reverse()
    return (x)


#Create a function with two arguments that will return an array of the first n multiples of x.

#Assume both the given number and the number of times to count will be positive numbers greater than 0        

def count_by(x, n):
    aLista = []
    for num in range(1, n+1):
        resultado = x * num
        aLista.append(resultado)
        
    
    return aLista

    #ou

def count_by(x, n):
    return [i * x for i in range(1,n+1)]

#Are You Playing Banjo?
# Create a function which answers the question "Are you playing banjo?".
#If your name starts with the letter "R" or lower case "r", you are playing banjo!

def areYouPlayingBanjo(name):
    if name[0].lower() == 'r':
        return name + ' plays banjo'
    else:
        return name + ' does not play banjo'

#We want an array, but not just any old array, an array with contents!

#Write a function that produces an array with the numbers 0 to N-1 in it        

def arr(n=0): 
    return [i for i in range(n)]


#The cockroach is one of the fastest insects. Write a function which takes
#  its speed in km per hour and returns it in cm per second, rounded down to the integer (= floored).

def cockroach_speed(s):
    vel = s * 27.7778
    return  int(vel)


#Complete the function that takes two integers (a, b, where a < b) and return an array 
# of all integers between the input parameters, including them.    

def between(a,b):
    num = []
    for numero in range(a, b, 1):
        num.append(numero)
    num.append(b)
    return (num)

#   All of the animals are having a feast! Each animal is bringing one dish.
#   There is just one rule: the dish must start and end with the same letters as the animal's name.
#   For example, the great blue heron is bringing garlic naan and the chickadee is bringing chocolate cake.
#   Write a function feast that takes the animal's name and dish as arguments and returns true or false
#   to indicate whether the beast is allowed to bring the dish to the feast.
#   Assume that beast and dish are always lowercase strings, and that each has
#   at least two letters. beast and dish may contain hyphens and spaces, 
#   but these will not appear at the beginning or end of the string. They will not contain numerals.  


def feast(beast, dish):
    if beast[0]== dish[0]:
        if beast[-1]== dish[-1]:
            return True
        else: return False
    else: return False

    ou 
def feast(beast, dish):
    if (beast[0]== dish[0]) and (beast[-1]== dish[-1]):
        return True
    else: return False


#Nathan loves cycling.

#Because Nathan knows it is important to stay hydrated, 
# he drinks 0.5 litres of water per hour of cycling.
#You get given the time in hours and you need to return
#  the number of litres Nathan will drink, rounded to the smallest value.

def litres(time):
    a = (time/2)
    return int(a)

#Create a function that gives a personalized greeting. This function takes two parameters: name and owner.

#Use conditionals to return the proper message:                
# name equals owner	'Hello boss' 
#otherwise	'Hello guest'

def greet(name, owner):
    return 'Hello boss' if name == owner else 'Hello guest'

#In this game, the hero moves from left to right. The player rolls the dice 
# and moves the number of spaces indicated by the dice two times.
#Create a function for the terminal game that takes the current position
#  of the hero and the roll (1-6) and return the new position   


def move(position, roll):
    finalPosit = (position + 2*roll)
    return finalPosit

#Create a function that takes 2 integers in form of a string as an input, 
# and outputs the sum (also as a string):

from operator import not_


def sum_str(a, b):
    if not a:
        if not b:
            return str(0)
        else: return str(0+int(b))
    if not b:
        if not a:
            return str(0)
        else: return str(int(a)+0)  

        
    else: return str(int(a)+int(b))

    