def is_armstrong_number(number):
    str_number = str(number)
    total = 0
    for i in str_number:
        total = total + ( int(i) ** len(str_number))

    if total == number:
        return True
    return False


