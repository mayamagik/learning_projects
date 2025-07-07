# input_utils.py

def get_valid_name(prompt):
    while True:
        value = input(prompt)
        if value.isalpha():
            return value
        print("Only letters allowed!")

def get_valid_numbers(prompt, min_value, max_value, range_msg):
    while True:
        try:
            number = int(input(prompt))
            if number < min_value or number > max_value:
                print(range_msg)
                continue
            return number
        except ValueError:
            print("Invalid input, try again!")
