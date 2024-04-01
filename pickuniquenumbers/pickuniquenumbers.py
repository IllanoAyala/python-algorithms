#Resolve [2,2,3,7,5,4,5,4] pick number that is not repeated.

numbers = [2,2,9,7,5,4,5,4,8,10,9,3,5]
def find_unique_number(numbers):
    unique_number = []

    for number in numbers:
        if numbers.count(number) == 1:
            unique_number.append(number)
        else:
            pass

    return unique_number


print(find_unique_number(numbers))