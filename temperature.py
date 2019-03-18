"""
Workshop for the Tucson Python Meetup working on learning functions
"""

def fahr_to_celsius(fahr):
    """
    >>> fahr_to_celsius(212)
    100.0
    >>> fahr_to_celsius(-40)
    -40.0
    >>> fahr_to_celsius('40')
    Traceback (most recent call last):
     ...
    TypeError: unsupported operand type(s) for -: 'str' and 'int'
    """
    # print(f"This is fahrenheit: {fahr}")
    celsius = (fahr - 32) * (5/9)
    # print(f"This is celsius: {celsius}")
    return celsius


def celsius_to_fahr(celsius):
    print(f"This is celsius: {celsius}")
    fahr = (celsius * (9/5)) + 32
    print(f"This is fahrenheit: {fahr}")
    return fahr


def fahr_to_kelvin(fahr):
    celsius = fahr_to_celsius(fahr)
    kelvin = celsius + 273.15
    return kelvin

    
def celsius_to_kelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin


if __name__ == '__main__':
    fahr = input("Give me a Fahrenheit: ")
    fahr = float(fahr)
    celsius = fahr_to_celsius(fahr)
    print(f"Here is the celsius: {celsius}")









