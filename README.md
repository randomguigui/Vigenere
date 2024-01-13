<h1>This is a vigenere encrypting and decrypting algorithm</h1>

<h3>Documentation :</h3>

- `Vigenere()`

Main class, it takes no argument.

- `Vigenere().encrypt(message, key)`

This method encrypt the `message` with the `key` and return the encrypted message as a string. Both must be string and the `key` must be in lower case.

- `Vigenere().decrypt(message, key)`

This method decrypt the given `message` with the `key` and return the decrypted message as a string. Both must be string and the `key` must be in lower case.


<h3>Example :</h3>

```python
from vigenere import Vigenere

vigenere = Vigenere()

encrypted_message = vigenere.encrypt('Hello World', 'gui')
# Nytri Eultj

decrypted_message = vigenere.decrypt(encrypted_message, 'gui')

print(decrypted_message)
# Hello World
```




