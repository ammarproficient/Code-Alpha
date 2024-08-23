# import random
#
# # List of possible words
# word_list = ['Code', 'Alpha', 'Python', 'Web Development']
#
# # Randomly select a word and convert it to lowercase for comparison
# word = random.choice(word_list).lower()
# hidden_word = ['_'] * len(word)
# guessed_letters = []
# tries = 6
#
# def display_word():
#     print(' '.join(hidden_word))
#
# def guess_letter(letter):
#     global tries
#     letter = letter.lower()  # Convert guess to lowercase
#     if letter in guessed_letters:
#         print(f'You already guessed "{letter}".')
#         return
#
#     guessed_letters.append(letter)
#
#     if letter in word:
#         # Update the hidden_word with the correct guesses
#         for i, char in enumerate(word):
#             if char == letter:
#                 hidden_word[i] = letter
#     else:
#         tries -= 1
#         print(f'Wrong guess. "{letter}" is not in the word. Tries left: {tries}')
#
# def hangman():
#     global tries
#
#     print('HINT: Total length of the word is', len(word))
#     display_word()
#
#     while tries > 0:
#         guess_user = input('Enter a letter: ').lower()
#
#         if len(guess_user) != 1 or not guess_user.isalpha():
#             print('Please enter a single letter.')
#             continue
#
#         guess_letter(guess_user)
#         display_word()
#
#         if '_' not in hidden_word:
#             print(f'Congratulations! You guessed the word: {word}')
#             break
#     else:
#         print(f'Sorry, you ran out of tries. The word was: {word}')
#
# if __name__ == "__main__":
#     hangman()




# import random
#
# word_list = ['java', 'python', 'ammar']
#
# word = random.choice(word_list)
# print(list(word))
#
# length = len(word)
# print(length)
#
# for i in range(length + 3):
#     guess = input(str('Enter the character'))
#     if len(guess) > 1:
#         print('type only 1 letter')
#     if guess in word:
#         print('yes', guess)
#     else:
#         print('no')







import random


word_list = ['java', 'python', 'ammar']


word = random.choice(word_list)
word_length = len(word)


guessed_word = ['_'] * word_length
attempts = word_length + 3
guessed_letters = []

print("Welcome to Hangman!")
print(' '.join(guessed_word))

while attempts > 0:
    guess = input("Enter a letter: ").lower()


    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue


    if guess in guessed_letters:
        print(f"You've already guessed '{guess}'. Try again.")
        continue


    guessed_letters.append(guess)


    if guess in word:
        print(f"Yes, '{guess}' is in the word!")
        for i in range(word_length):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        print(f"No, '{guess}' is not in the word.")
        attempts -= 1


    print(' '.join(guessed_word))


    if '_' not in guessed_word:
        print("Congratulations! You've guessed the word:", word)
        break

    print(f"Attempts remaining: {attempts}")

if attempts == 0:
    print("Game over! The word was:", word)
