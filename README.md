# Cipher Algorithms Collection

This repository contains implementations of various classical and modern cipher algorithms written in Python. These ciphers are widely used in cryptography for securing information and understanding cryptographic techniques.

## Table of Contents

- [About](#about)
- [Ciphers Included](#ciphers-included)
  - [Playfair Cipher](#playfair-cipher)
  - [Caesar Cipher](#caesar-cipher)
  - [Affine Cipher](#affine-cipher)
  - [Hill Cipher](#hill-cipher)
  - [Rail Fence Cipher](#rail-fence-cipher)
  - [Baconian Cipher](#baconian-cipher)
  - [Vigenère Cipher](#vigenere-cipher)
  - [Atbash Cipher](#atbash-cipher)
  - [RSA Cipher](#rsa-cipher)
  - [Bluetooth Mobile DOS](#bluetooth-mobile-dos)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## About

This project showcases a collection of cipher algorithms ranging from classic ciphers like Caesar and Atbash to more complex encryption schemes such as RSA. Each cipher is implemented in Python and can be used for both educational purposes and practical cryptographic tasks.

## Ciphers Included

### Playfair Cipher
The **Playfair Cipher** is a digraph substitution cipher that encrypts pairs of letters.

File: `playfair_cipher.py`

### Caesar Cipher
The **Caesar Cipher** is one of the simplest encryption techniques, where each letter is shifted by a certain number of positions.

File: `ceaser_cipher.py`

### Affine Cipher
The **Affine Cipher** is a type of monoalphabetic substitution cipher, which uses mathematical functions for encryption.

File: `affine_cipher.py`

### Hill Cipher
The **Hill Cipher** is a polygraphic substitution cipher using linear algebra and matrix manipulation.

File: `hill_cipher.py`

### Rail Fence Cipher
The **Rail Fence Cipher** is a transposition cipher where the text is written in a zigzag pattern.

File: `rail_fence_cipher.py`

### Baconian Cipher
The **Baconian Cipher** is a substitution cipher, which replaces each letter with a binary code.

File: `baconian_cipher.py`

### Vigenère Cipher
The **Vigenère Cipher** uses a keyword to encrypt the text with a series of Caesar ciphers.

File: `vigenere_cipher.py`

### Atbash Cipher
The **Atbash Cipher** is a simple substitution cipher that reverses the alphabet.

File: `atbash_cipher.py`

### RSA Cipher
The **RSA Cipher** is a widely used public-key cryptosystem that secures communications over the internet.

File: `RSA_Cipher_Alg.py`

### Bluetooth Mobile DOS
This file simulates a **Bluetooth Mobile Denial-of-Service (DoS)** attack and is provided for research and educational purposes only.

File: `BluetoothMobileDOS.py`

## Usage

To use any of the cipher algorithms:

1. Clone this repository:

    ```bash
    git clone https://github.com/yourusername/cipher-algorithms.git
    cd cipher-algorithms
    ```

2. Navigate to the desired cipher folder.
3. Run the Python script:

    ```bash
    python <cipher_name>.py
    ```

4. Follow the on-screen prompts to input plaintext or ciphertext and use the desired encryption/decryption functions.

## Contributing

If you would like to contribute to this repository, feel free to open a pull request or submit an issue with suggestions.

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
