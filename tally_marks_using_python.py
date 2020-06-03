#Retrieve number form end-user
number = int(input("Input a positive number:"))

#how many blocks of 5 tallies: ||||- to include
quotient = number // 5

#Find out how many tallies are remaining
remainder = number % 5

tallyMarks = "||||-   " * quotient + "|" * remainder
print(tallyMarks)

