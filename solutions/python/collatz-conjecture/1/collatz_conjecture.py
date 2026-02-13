#This code tests ou the collatz conjecture.
'''The Collatz Conjecture finds the eventual path to 1 of an integer, taking two different paths for an odd and even integer.
For an even number it divides it by two and for an uneven one it multiplies it and add one. Btw i need to not forget that if 
you take for example 10, you divide it by two which makes 5 and because five is an odd number you multiply it by 3 and add 1.
This function executes the Collatz Conjecture and returns the number of steps it takes to reach 1 when inputing a number.
'''
def steps(number):
#I first raise an exception for if the number is negative.
    if number <=0:
        raise ValueError("Only positive integers are allowed")
#I establish the parameter step_counter to count the amount of steps done. I put it at 0 since there have been no steps executed yet.
    step_counter=0
#I now create the loop that will divide if its even or do 3n=1 if not WHILE NUMBER !=1.
    while number != 1:
        if number%2==0:
            number//=2
            step_counter+=1
        else:
            number=(number*3)+1
            step_counter+=1
#Finally, I return the step_counter.
    return step_counter
