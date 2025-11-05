Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def encrypt(plain_text, key):
    cipher_text = ""
    for char in plain_text:
        if char.isalpha():
            char_upper = char.upper()
            char_value = ord(char_upper) - ord('A')
            encrypted_value = (char_value * key) % 26
            encrypted_char = chr(encrypted_value + ord('A'))
            cipher_text += encrypted_char
        else:
            cipher_text += char
    return cipher_text

def decrypt(cipher_text, key):
    plain_text = ""
    try:
        key_inverse = pow(key, -1, 26)
    except ValueError:
        return "Error: Key does not have a modular inverse (must be coprime to 26)."

    for char in cipher_text:
        if char.isalpha():
            char_upper = char.upper()
            char_value = ord(char_upper) - ord('A')
            decrypted_value = (char_value * key_inverse) % 26
            decrypted_char = chr(decrypted_value + ord('A'))
            plain_text += decrypted_char
        else:
            plain_text += char
    return plain_text

def get_valid_key():
    while True:
        try:
            key = int(input("Enter a multiplicative key (an integer coprime to 26, e.g., 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25): "))

            if gcd(key, 26) == 1:
                return key
            else:
                print("Invalid key. The key must be coprime to 26.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    while True:
        print("\nMultiplicative Cipher Menu:")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")

        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            message = input("Enter the plaintext message: ")
            key = get_valid_key()
            encrypted_message = encrypt(message, key)
            print(f"Encrypted message: {encrypted_message}")
        elif choice == '2':
            message = input("Enter the ciphertext message: ")
            key = get_valid_key()
            decrypted_message = decrypt(message, key)
            print(f"Decrypted message: {decrypted_message}")
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
[DEBUG ON]
>>> 
[DEBUG OFF]
>>> 