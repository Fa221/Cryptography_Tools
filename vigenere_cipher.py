def generate_key(text, key):
    key = list(key)
    if len(text) == len(key):
        return "".join(key)
    else:
        for i in range(len(text) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

def vigenere_cipher(text, key):
    cipher_text = []
    key = generate_key(text, key)
    for i in range(len(text)):
        if text[i].isalpha():
            x = (ord(text[i]) + ord(key[i])) % 26
            x += ord('A') if text[i].isupper() else ord('a')
            cipher_text.append(chr(x))
        else:
            cipher_text.append(text[i])
    return "".join(cipher_text)

text = input("Enter text: ")
key = input("Enter key: ")
print("Cipher: " + vigenere_cipher(text, key))

