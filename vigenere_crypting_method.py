import string


class Vigenere:
    def __init__(self):
        self.alphabet_lower = list(string.ascii_lowercase)
        self.alphabet_upper = list(string.ascii_uppercase)

    def encrypt(self, message, key):
        encrypted = []
        key = list(key)

        for letter in message:
            if letter.islower():
                index_letter_message = self.alphabet_lower.index(letter)
                index_letter_key = self.alphabet_lower.index(key[0])

                key.append(key.pop(0))

                if index_letter_message + index_letter_key < 26:
                    encrypted.append(self.alphabet_lower[index_letter_message + index_letter_key])
                else:
                    encrypted.append(self.alphabet_lower[(index_letter_message + index_letter_key) - 26])

            elif letter.isupper():
                index_letter_message = self.alphabet_upper.index(letter)
                index_letter_key = self.alphabet_lower.index(key[0])

                key.append(key.pop(0))

                if index_letter_message + index_letter_key < 26:
                    encrypted.append(self.alphabet_upper[index_letter_message + index_letter_key])
                else:
                    encrypted.append(self.alphabet_upper[(index_letter_message + index_letter_key) - 26])

            elif letter in string.punctuation or letter in string.whitespace:
                encrypted.append(letter)

        return "".join(encrypted)

    def decrypt(self, message, key):
        decrypted = []
        key = list(key)

        for letter in message:
            if letter.islower():
                index_letter_message = self.alphabet_lower.index(letter)
                index_letter_key = self.alphabet_lower.index(key[0])

                key.append(key.pop(0))

                if index_letter_message - index_letter_key >= 0:
                    decrypted.append(self.alphabet_lower[index_letter_message - index_letter_key])
                else:
                    decrypted.append(self.alphabet_lower[index_letter_message - index_letter_key + 26])

            elif letter.isupper():
                index_letter_message = self.alphabet_upper.index(letter)
                index_letter_key = self.alphabet_lower.index(key[0])

                key.append(key.pop(0))

                if index_letter_message + index_letter_key >= 0:
                    decrypted.append(self.alphabet_upper[index_letter_message - index_letter_key])
                else:
                    decrypted.append(self.alphabet_upper[index_letter_message - index_letter_key + 26])

            elif letter in string.punctuation or letter in string.whitespace:
                decrypted.append(letter)

        return "".join(decrypted)