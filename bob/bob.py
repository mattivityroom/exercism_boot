def response(hey_bob):
    if hey_bob.isupper() and "?" in hey_bob:
        return 'Calm down, I know what I\'m doing!'

    if hey_bob.isupper():
        return 'Whoa, chill out!'

    if hey_bob.strip().endswith('?'):
        return 'Sure.'

    if hey_bob.strip() == "":
        return 'Fine. Be that way!'

    return 'Whatever.'