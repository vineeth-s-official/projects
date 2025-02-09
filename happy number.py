number = 19
seen_numbers = set()  

while number != 1 and number not in seen_numbers:
    seen_numbers.add(number)
    number = sum(int(digit) ** 2 for digit in str(number))

if number == 1:
    print(f"{number} is a Happy Number!")
else:
    print(f"{number} is not a Happy Number.")
