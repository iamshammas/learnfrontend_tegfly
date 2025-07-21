# Ask user for marks and print grade based on:
# >90: A, >75: B, >60: C, else: Fail

# mark = int(input("Enter ur mark: "))

# if mark>=90:
#     print('A')
# elif mark>=75:
#     print('B')
# elif mark>=60:
#     print('C')
# else:
#     print('FAIL')

# Print multiplication table of 5 using for loop

# for i in range(5,51):
#     if i%5==0:
#         print(i)
    
# print("another way")

# for i in range(5,51,5):
#     print(i)
    

# Create a countdown from 10 to 1

# count = 10
# while count >= 1:
#     print(count)
#     count-=1

# NUMBER GUESSING GAME


# 😢 Out of tries. The number was {secret}

import random

secret = random.randint(1,20)

retries=0
while retries < 5:
    guess = int(input('Guess the number (1–20): '))
    if guess == secret:
        print('🎉 Correct! You guessed it.')
        break
    elif guess > secret:
        print('Too High')
    elif guess < secret:
        print('Too Low')

    retries+=1

if guess!=secret:
    print(f"😢 Out of tries. The number was {secret}")