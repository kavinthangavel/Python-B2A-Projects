import random

def roll_dice(num):
    return random.randint(1, num)

def greet_user(name):
    return f"Hello, {name}!"

def get_file_ext(filename):
    return filename[filename.index(".") + 1:]