#calculating the number of squares on any given square: that is calculated by multiplying the number of the square by itslef and then substracting it once.
def square(number):
    if number>=1 and number<=64:
        return (2**(number-1))
    else:
        raise ValueError("square must be between 1 and 64")
#Giving the total amount of grains on the chessboard.
def total():
    return 2**64 - 1