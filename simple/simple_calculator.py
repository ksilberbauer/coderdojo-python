first_number = int(input("Enter first number:"))
operator = input("Enter math operator (+, -, *, /):")
second_number = int(input("Enter second number:"))

if operator is "+":
    print first_number + second_number
elif operator is "-":
    print first_number - second_number
elif operator is "*":
    print first_number * second_number
elif operator is "/":
    print first_number / second_number
else:
    print "How did we get here??!?"


