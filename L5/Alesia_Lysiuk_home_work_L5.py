# Home work 5.1.
def is_year_leap(year):
    '''Determinate, are year is a leap?'''

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr, '-->', end='')
    result = is_year_leap(yr)
    if result == test_results[i]:
        print('OK')
    else:
        print('Failed')

# Home work 5.3.
# Calculate factorial without recursion.
def function(number):
    factorial = 1
# Check if the number is negative, positive, zero, one.
    if number < 0:
        return
    if number <= 1:
        return 1

    for i in range(1, number + 1):
        factorial *= 1
        return factorial
    print('factorial is: ', function(number = int(input('Enter a number: '))))

# Home work 5.4.
# Fibonacci numbers.
def febo(n):
    if n < 1:
        return None
    if n < 3:
        return 1

    f1 = f2 = 1

    for _ in range(2, n):
        f1, f2 = f2, f1 + f2

    return f2


for i in range(-1, 25):
    print(febo(i))
    