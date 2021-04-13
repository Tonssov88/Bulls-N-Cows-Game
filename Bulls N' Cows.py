import random
guessed = 0
bulls = 0
cows = 0
validNum = False

# Generates a random number with NO REPEATED DIGITS
while validNum == False:
    secretNumber = random.randint(1000, 9999)
    num1 = secretNumber
    digits = []
    for i in range(4):
        lastDigit = secretNumber % 10
        secretNumber = secretNumber // 10
        digits.insert(0, lastDigit)
    for digit in range(4):
        validNum = True
        if digits.count(digits[digit]) > 1:
            print(f"Invalid number, redoing...")
            validNum = False
            break
    if validNum:
        secretNumber = [str(d) for d in digits]
        print("Valid Number Found")

while bulls!=4:
    bulls = 0
    cows = 0
    playerGuess = input("What is your guess: ")
    guess = list(str(playerGuess))
    for i in range(4):
        if guess[i] == secretNumber[i]:
            bulls +=1
        elif guess[i] in secretNumber:  ## might be a problem...
            cows +=1
    print(f"There are {cows} cow(s) and {bulls} bull(s)")

print(f"Correct! My secret number was {num1}! Have a nice day!")
