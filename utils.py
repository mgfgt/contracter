from typing import Callable

def loop_input_validation(prompt: str, validator: Callable[[str], bool], message: str):
    while True:
        value = input(prompt)
        if not validator(value):
            print(message)
            continue
        return value

def check_yes_or_no(val):
    val = val.lower()
    if (val == "y" or val == "n"):
        return True
    else:
        return False

def check_float(val):
    try:
        float(val)
        return True;
    except:
        return False;