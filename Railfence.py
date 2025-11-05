def encrypt_rail_fence(text, key):
    rail = ['' for _ in range(key)]
    direction_down = False
    row = 0
    for char in text:
        rail[row] += char
        if row == 0 or row == key - 1:
            direction_down = not direction_down
        row += 1 if direction_down else -1
    return ''.join(rail)
def decrypt_rail_fence(cipher, key):
    rail = [['\n' for _ in range(len(cipher))]
            for _ in range(key)]

    direction_down = None
    row, col = 0, 0

    # mark zigzag path with '*'
    for i in range(len(cipher)):
        if row == 0:
            direction_down = True
        if row == key - 1:
            direction_down = False
        rail[row][col] = '*'
        col += 1
        row += 1 if direction_down else -1
    # fill the ciphertext letters
    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if (rail[i][j] == '*' and index < len(cipher)):
                rail[i][j] = cipher[index]
                index += 1
    # read in zigzag to reconstruct plaintext
    result = []
    row, col = 0, 0
    for i in range(len(cipher)):
        if row == 0:
            direction_down = True
        if row == key - 1:
            direction_down = False
        if rail[row][col] != '*':
            result.append(rail[row][col])
            col += 1
        row += 1 if direction_down else -1
    return ''.join(result)
# Input from user
plaintext = input("Enter the string to be encrypted: ")
key = int(input("Enter the key (number of rails): "))

# Encryption
ciphertext = encrypt_rail_fence(plaintext, key)
print("\nEncrypted Text:", ciphertext)

# Decryption prompt
choice = input("\nIf you want to decrypt, type 'd' or type 'e' for exit: ")
if choice == 'd':
    decrypted_text = decrypt_rail_fence(ciphertext, key)
    print("\nDecrypted Text:", decrypted_text)
else:
    print("\nProgram exited...")
