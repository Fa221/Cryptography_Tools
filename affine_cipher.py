def affine_encrypt(text, a, b):
    result = ""
    
    for char in text:
        if char.isalpha():
            char_val = ord(char.lower()) - ord('a')
            encrypted_char = (a * char_val + b) % 26
            result += chr(encrypted_char + ord('a')) if char.islower() else chr(encrypted_char + ord('A'))
        else:
            result += char
    
    return result

def affine_decrypt(cipher, a, b):
    result = ""
    mod_inverse_a = pow(a, -1, 26)
    
    for char in cipher:
        if char.isalpha():
            char_val = ord(char.lower()) - ord('a')
            decrypted_char = mod_inverse_a * (char_val - b) % 26
            result += chr(decrypted_char + ord('a')) if char.islower() else chr(decrypted_char + ord('A'))
        else:
            result += char
    
    return result

text = input("Enter text: ")
a = int(input("Enter value for 'a': "))
b = int(input("Enter value for 'b': "))
print("Encrypted: " + affine_encrypt(text, a, b))

