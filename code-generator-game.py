
>>> import random
>>> 
>>> def generate_code():
...   # Generate a random 4-digit code
...   code = str(random.randint(1000, 9999))
...   return code
... 
>>> def play_game():
...   # Generate the code
...   code = generate_code()
...   print("Code generated! Try to guess the code.")
...   
...   # Set the number of attempts to 0
...   attempts = 0
...   
...   # Start the game loop
...   while True:
...     # Get the player's guess
...     guess = input("Enter your guess: ")
...     
...     # Increment the number of attempts
...     attempts += 1
...     
...     # Check if the guess is correct
...     if guess == code:
...       print("You guessed the code in {} attempts!".format(attempts))
...       break
...     else:
...       print("Incorrect guess. Try again.")
... 
>>> # Start the game
>>> play_game()

