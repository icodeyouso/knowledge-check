# Odd or Even

def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


# Convert a number to a string
def interger_tostring(num):
    return str(num)

# Vowel Count


def get_count(sentence):

    vowels = 'iouea'
    return sum(1 for char in sentence if char in vowels)
