# # GAME 1:
# ----------------------------------------------

# import random
# secret_number = random.randint(1,5)
# guess_count = 0

# while guess_count < 2:
#     try:
#         guess = int(input("Guess a number (1-10): ")) 
#     except ValueError:
#         print("Please enter a valid integer.")
#         continue

#     guess_count += 1

#     if guess == secret_number:
#         print("Congratulations, you guessed it!")
#         break
#     else:
#         print("Try again")

# if guess_count == 2:
#     print(f"Sorry, you ran out of guesses.The number was {secret_number}")



# # GAME 2:
# # -----------------------------------------------------------

favorite_aeroplane = "Dreamliner"
guess_count = 0

while guess_count < 3:
    try:
          
        guess = input("Which aeroplane do you think is my favorite? ")
        print("(Hint:Another name for Boeing 787)")
      
    except ValueError:
        print("Please input a string!")

    guess_count += 1

    if guess == ("Dreamliner").lower():
        print("You are a genius")
        break
    else:
        print("Try again, you are almost there!")

if guess_count == 3:
    print(f"Oops!You ran out of guesses.The answer was {favorite_aeroplane}!")


# total = 0
# sum_evn= 0
# for num in range (1,20):
#  sum_evn += 2
#  if num % 2:
#   print(sum_evn)



















