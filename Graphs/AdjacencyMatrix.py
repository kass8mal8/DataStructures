nums = 1349


def getSum(number):
    rem, num_rem = number % 10, abs(number)
    sum = 0

    while num_rem:
        rem, num_rem = num_rem % 10, num_rem // 10
        sum += rem

    return sum


print(getSum(nums))
