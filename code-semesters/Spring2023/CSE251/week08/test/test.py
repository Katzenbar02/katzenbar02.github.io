numbers = range(0,11)


def origianl(numbers):
    sum = 0

    for x in numbers:
        sum += (6*2**x)
        print(sum)

def ori_qual(numbers):
    sum = 0


    for x in numbers[:-2]:
        sum += (2**x) + numbers[:-2]
        print(sum)

origianl(numbers)
# ori_qual(numbers)