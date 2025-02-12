# Home work 2.1.
# Enter four numbers.
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the first number: "))
number3 = int(input("Enter the first number: "))
number4 = int(input("Enter the first number: "))

# Choose larger number1_2.
if number1 > number2:
    larger_number1_2 = number1
else:
    larger_number1_2 = number2

# Choose larger number3_4.
if number3 > number4:
    larger_number3_4 = number3
else:
    larger_number3_4 = number4

# Choose larger number1_2 or larger number3_4.
if larger_number1_2 > larger_number3_4:
    larger_number1_2_3_4 = larger_number1_2
else:
    larger_number1_2_3_4 = larger_number3_4

# Print the result.
print("The langer number is: ", larger_number1_2_3_4)             


# Home work 2.4.
# Adding module time.
import time
# Loop that count to five.
for counter in range(1,6):
    print(counter, "Mississippi")
    time.sleep(1)
# Final messange.
print("Ready or not, here I come!")

# Home work 2.6.
# Choose operation.
math_operation = input('+-*/ or exit')

while math_operation != "exit":
    number1, number2 = int(
        input("Enter first number: ")), int(input("Enter second number: "))
    
    if math_operation == '+':
        print(number1 + number2)
    elif math_operation == '-':
        print(number1 - number2)
    elif math_operation == '*':
        ptint(number1 * number2)
    elif math_operation == '/':
        print(number1 / number2)
    else:
        print(f'Не известная операция - {operation}')

    math_operation = input('+-*/ or exit: ')
