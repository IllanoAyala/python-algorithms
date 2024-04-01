#Resolve [0,1,0,1,0,1,99] pick number that is not repeated.

numbers = [0,1,0,1,0,1,99]
def find_unique_number(numbers):
    unique_number = None

    for number in numbers:
        if numbers.count(number) == 1:
            unique_number = number
        else:
            pass

    return unique_number


print(find_unique_number(numbers))