import random

user = input("Rock, Paper, or Scissors?")
computer = random.choice(['rock', 'paper', 'scissors'])

print "You: " + user
print "Computer: " + computer

if user == computer:
    print "You picked the same!"
elif user == "rock" and computer == "paper":
    print "computer wins"
elif user == "paper" and computer == "scissors":
    print "computer wins"
elif user == "scissors" and computer == "rock":
    print "computer wins"
elif user == "rock" and computer == "scissors":
    print "YOU WIN!"
elif user == "paper" and computer == "rock":
    print "YOU WIN!"
elif user == "scissors" and computer == "paper":
    print "YOU WIN!"
