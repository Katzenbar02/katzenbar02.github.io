import random

def main():
    randnums = [16.2, 75.1, 52.3]
    print(randnums)

    append_random_numbers(randnums)
    print(randnums)
    
    append_random_numbers(randnums, 3)
    print(randnums)

    randwords = []

def append_random_numbers(numbers_list, quantity=1):
    for _ in range(quantity):
        random_num = random.uniform(0, 100)
        rounded = round(random_num, 1)
        numbers_list.append(rounded)

if __name__ == "__main__":
    main()