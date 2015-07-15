percentage = input("Enter your percentage out of 100%")
percentage = int(percentage)

if percentage < 0 or percentage > 100:
    print "Invalid percentage"
elif percentage < 60:
    print "F"
elif percentage < 70:
    print "D"
elif percentage < 80:
    print "C"
elif percentage < 90:
    print "B"
else:
    print "A"