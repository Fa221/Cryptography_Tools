import numpy as np

def hill_cipher_encrypt(message, key_matrix):
    message_vector = [ord(char) - 65 for char in message.upper()]
    message_matrix = np.array(message_vector).reshape(-1, len(key_matrix))

    cipher_matrix = np.dot(message_matrix, key_matrix) % 26
    cipher_text = ''.join([chr(int(c) + 65) for c in cipher_matrix.flatten()])
    
    return cipher_text

message = input("Enter message: ")
key_matrix = np.array([[3, 3], [2, 5]])  # Example key matrix for 2x2 Hill cipher
print("Encrypted Message: " + hill_cipher_encrypt(message, key_matrix))

