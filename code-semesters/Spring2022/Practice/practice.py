# write a funtion that takes a list of numbers and returns a new list with only the odd numbers
def odd_numbers(numbers):
    odd_numbers = []
    for number in numbers:
        if number % 2 != 0:
            odd_numbers.append(number)
    return odd_numbers