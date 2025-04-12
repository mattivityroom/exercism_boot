LIMIT = 64

def square(number):
    if ( number <= 0 or number > LIMIT ):
        raise ValueError("square must be between 1 and 64")
    return 1 << number - 1

def total():
    return (1 << 64) - 1