# Caesar Cipher Program

This project implements a simple Caesar Cipher program in Python, allowing users to encrypt and decrypt text using a shift key. The Caesar Cipher is a basic encryption technique where each letter in the plaintext is shifted by a fixed number of positions in the alphabet.

---

## Features

1. **Encryption**:
   - Converts plaintext into ciphertext by shifting letters forward in the alphabet.

2. **Decryption**:
   - Converts ciphertext back into plaintext by reversing the shift.

3. **Custom Shift Key**:
   - Users can specify the number of positions to shift the alphabet.

4. **Interactive Interface**:
   - Allows users to repeatedly encrypt or decrypt text until they choose to exit.

---

## How It Works

1. The user specifies whether they want to `encrypt` or `decrypt` text.
2. The user inputs the text to be processed.
3. A shift key (number of positions to shift) is provided by the user.
4. The program processes the text and outputs the result.
5. The user can choose to perform another operation or exit the program.

---

## Code Structure

### **Alphabet List**
A list of lowercase English letters is used for indexing during the shift:
```python
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
         'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
```

### **Functions**

#### 1. **Encryption**
Encrypts plaintext by shifting each letter forward by the shift key:
```python
def Encryption(plain_text, shift_key):
    cipher_text = ""
    for char in plain_text:
        if char in alpha:
            position = alpha.index(char)
            new_position = (position + shift_key) % 26
            cipher_text += alpha[new_position]
        else:
            cipher_text += char
    print(f"The text after Encryption: {cipher_text}")
```

#### 2. **Decryption**
Decrypts ciphertext by reversing the shift:
```python
def Decryption(cipher_text, shift_key):
    plain_text = ""
    for char in cipher_text:
        if char in alpha:
            position = alpha.index(char)
            new_position = (position - shift_key) % 26
            plain_text += alpha[new_position]
        else:
            plain_text += char
    print(f"The text after Decryption: {plain_text}")
```

### **Main Program Flow**
- Uses a `while` loop to provide an interactive experience.
- Handles user input for operation type, text, and shift key.
- Allows the user to continue or exit after each operation.

---

## How to Run

1. Clone the repository or download the script:
   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```bash
   cd <project-directory>
   ```

3. Run the script:
   ```bash
   python caesar_cipher.py
   ```

---

## Example Usage

### Sample Input:
```plaintext
Enter 'encrypt' for Encryption and 'decrypt' for Decryption:
 encrypt
Enter the text:
 hello
Enter the no of shift key:
 3
```

### Output:
```plaintext
The text after Encryption: khoor
```

### Sample Decryption:
```plaintext
Enter 'encrypt' for Encryption and 'decrypt' for Decryption:
 decrypt
Enter the text:
 khoor
Enter the no of shift key:
 3
```

### Output:
```plaintext
The text after Decryption: hello
```

---

## Customization

### Adding Support for Uppercase Letters
To include uppercase letters, modify the `alpha` list and check for uppercase characters in the encryption and decryption logic.

### Cross-Platform Screen Clearing
Replace `os.system('cls')` (used on Windows) with a platform-independent solution:
```python
import os
os.system('cls' if os.name == 'nt' else 'clear')
```

---

## Dependencies
- Python 3.6 or higher

---

## Limitations
- Only supports lowercase letters.
- Does not handle non-English alphabets.

---

## License
This project is open-source and available under the [MIT License](LICENSE).

---



## Contact
For questions or feedback, please contact Shajan J Jacob.

