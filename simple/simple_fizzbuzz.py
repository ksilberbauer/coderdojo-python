number_as_string = input("Enter a number")
number = int(number_as_string)

result = ""
if number % 3 == 0:
    result = result + "Fizz"
if number % 5 == 0:
    result = result + "Buzz"
if number % 3 != 0 and number % 5 != 0:
    result = number

print result