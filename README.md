# Cryptography Tools

## Overview

This repository contains implementations of several cryptographic algorithms and security tools, including the **Playfair Cipher**, **RSA Cipher**, and a **Bluetooth Mobile DoS** (Denial of Service) script. Each script is written in Python and designed for educational purposes, demonstrating the mechanics behind encryption and security techniques.

## Files in the Repository

1. **playfair_cipher.py**
   - Implements the Playfair Cipher, a symmetric encryption technique used for secure text encryption.
   - The Playfair Cipher uses a 5x5 matrix of letters for encryption, working by encrypting digraphs (pairs of letters) rather than single letters.

2. **RSA_Cipher_Alg.py**
   - A Python implementation of the RSA algorithm, a public-key cryptosystem that is widely used for secure data transmission.
   - The script includes key generation, encryption, and decryption processes.

3. **BluetoothMobileDOS.py**
   - Simulates a Denial of Service (DoS) attack targeting Bluetooth-enabled mobile devices.
   - This script is intended for educational purposes only and demonstrates potential vulnerabilities in Bluetooth security protocols.

## How to Use

### Prerequisites

- Python 3.x
- Required libraries (if any): [Specify here if the scripts require any additional libraries]

### Running the Scripts

#### 1. Playfair Cipher
To run the **Playfair Cipher** encryption script:
```bash
python playfair_cipher.py
