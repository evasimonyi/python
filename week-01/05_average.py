def average(numbers):
    sum = 0
    for i in numbers:
        sum += i
    return sum / len(numbers)


print(average([1, 2, 3, 4, 5]))
