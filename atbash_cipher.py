def atbash_cipher(text):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr(90 - (ord(char) - 65))
            else:
                result += chr(122 - (ord(char) - 97))
        else:
            result += char
    return result

text = input("Enter text: ")
print("Cipher: " + atbash_cipher(text))

