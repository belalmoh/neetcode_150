import string


def decipher(cipherText: str, knownWord: str):
    alphabets = list(string.ascii_lowercase)
    splittedString = cipherText.split()
    result = ""

    for word in splittedString:
        if len(word) == len(knownWord):
            firstLetter = word[0].lower()
            knownFirstLetter = knownWord[0].lower()

            difference = abs(alphabets.index(firstLetter) - alphabets.index(knownFirstLetter)) % 26
            coeff = 0

            if alphabets.index(firstLetter) + difference == alphabets.index(knownFirstLetter):
                coeff += difference
            elif alphabets.index(firstLetter) - difference == alphabets.index(knownFirstLetter):
                coeff -= difference
            else:
                continue

            new_word = ""

            for letter in word:
                if letter.isalpha():
                    shiftedLetter = alphabets[(alphabets.index(letter.lower()) + coeff) % 26]

                    if letter.isupper():
                        shiftedLetter = shiftedLetter.upper()

                    new_word += shiftedLetter

            if new_word.lower() == knownWord.lower():
                for letter in cipherText:
                    if letter.isalpha():
                        shiftedLetter = alphabets[(alphabets.index(letter.lower()) + coeff) % 26]

                        if letter.isupper():
                            shiftedLetter = shiftedLetter.upper()

                        result += shiftedLetter
                    else:
                        result += letter

                break

    return result


if __name__ == "__main__":
    result = decipher("Eqfkpi vguvu ctg hwp!", "tests")
    print(result)