# for loop გამოიყენება მიმდევრობით (ეს არის სია, ტიპი, ლექსიკონი, ნაკრები ან სტრიქონი) განმეორებისთვის.

# ეს ნაკლებად ჰგავს for საკვანძო სიტყვას სხვა პროგრამირების ენებში და უფრო მეტად მუშაობს itator მეთოდის მსგავსად, როგორც ეს სხვა ობიექტზე ორიენტირებულ პროგრამირების ენებშია ნაპოვნი.

# for მარყუჟის საშუალებით ჩვენ შეგვიძლია შევასრულოთ განცხადებების ნაკრები, ერთხელ თითოეული ელემენტისთვის სიაში, tuple, set და ა.შ.

   
# import random

# # List of the words
# words = ["house", "mate", "ilia", "tuta", "hello"]

# # Choosing the random word
# secret_word = random.choice(words).lower()

# # variables
# attempts = 6
# guessed_letters = []

# # Hangman stages
# hangman_stages = [
#     """
#        +---+
#        |   |
#            |
#            |
#            |
#            |
#      =======""",
#     """
#        +---+
#        |   |
#        O   |
#            |
#            |
#            |
#      =======""",
#     """
#        +---+
#        |   |
#        O   |
#        |   |
#            |
#            |
#      =======""",
#     """
#        +---+
#        |   |
#        O   |
#       /|   |
#            |
#            |
#      =======""",
#     """
#        +---+
#        |   |
#        O   |
#       /|\  |
#            |
#            |
#      =======""",
#     """
#        +---+
#        |   |
#        O   |
#       /|\  |
#       /    |
#            |
#      =======""",
#     """
#        +---+
#        |   |
#        O   |
#       /|\  |
#       / \  |
#            |
#      ======="""
# ]

# #games loop

# while attempts > 0:
#     #displaying the hangman stage
#     print(hangman_stages[6 - attempts])

#     #displaying the status
#     display_word = ''.join([char if char in guessed_letters else '_' for char in secret_word])
#     print(display_word)

#     #checking if the word is guesde

#     if '_' not in display_word:
#         print("nice one! you guessed the word that was:", secret_word)
#         break

#     #the code for input
#     guess = input("guess a letter:").lower()

#     #checking if the letter is already guessed
#     if guess in guessed_letters:
#         print("you guessed that letter already")
#         continue
#     guessed_letters.append(guess)

#     #checking if the letter is in the word
#     if guess not in secret_word:
#         attempts -= 1
#         print("incorrect guess :( you have",  attempts, "attempts left")
#     else:
#         print("correct guess nice")

#         #game over!

#         if attempts == 0:
#             print("game over! the word was:", secret_word)
            


name = "daniel

if name == "daniel":
    print("my name is daniel")
elif name == "anonym":
    print("my name is anonym")
else:
    print("im not daniel")