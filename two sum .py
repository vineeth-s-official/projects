def two_sum(numbers, target):
    a = {}
    for i, num in enumerate(numbers):
        remainder = target - num
        if remainder in a:
            return [a[remainder], i]
        a[num] = i
    return []
numbers = [1,2,3,4]
target = 7
print(two_sum(numbers, target))






