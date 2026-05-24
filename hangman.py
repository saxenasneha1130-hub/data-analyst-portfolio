import random

words = ["python", "coding", "laptop", "github", "analyst"]

word = random.choice(words)
guessed = []
attempts = 6
print("🎮 Welcome to Hangman!")

while attempts > 0:
    display = ""
    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "
    
    print("\nWord:", display)
    print("Attempts left:", attempts)
    print("Guessed:", guessed)
    
    if "_" not in display:
        print("🎉 You Won! Word was:", word)
        break
    
    guess = input("Guess a letter: ").lower()
    
    if guess in guessed:
        print("Already guessed!")
    elif guess in word:
        guessed.append(guess)
        print("✅ Correct!")
    else:
        guessed.append(guess)
        attempts -= 1
        print("❌ Wrong!")

if attempts == 0:
    print("💀 Game Over! Word was:", word)