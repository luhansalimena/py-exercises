import random

def getWords() -> list:
    words: list = []
    with open('./hangman/words.txt', encoding='utf8') as file:
        for word in file.readlines():
            words.append(word.replace('\n',''))

    return words

words = getWords()
randomWord = list(random.choice(words).upper())
length: int = len(randomWord)
guesseds: list = []
wrongLetters: list = []

for i in range(length):
    guesseds.append('_')

def showLines():
    print(randomWord)
    lines = ''

    for letter in guesseds:
        lines += letter
    
    print(lines)

def guessedRight(letter: str):
    indexes = [n for n,x in enumerate(randomWord) if x==letter]
    for index in indexes:
        guesseds[index] = letter

def guessedWrong(letter: str):
    print('You guessed Wrong!')

def guessLetter():
    letter = input("Guess a letter: ").upper()
    if(letter in randomWord):
        guessedRight(letter)
    else:
        guessedWrong(letter)
    
    main()

def main():
    showLines()
    guessLetter()

main()
