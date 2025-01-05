def encrypt_vigenere(plaintext, key):
    # Assigning numeric values to letters
    def char_to_num(c):
        return ord(c) - ord('A')
    
    def num_to_char(n):
        return chr(n + ord('A'))

    # Converting plaintext and key to uppercase
    plaintext = plaintext.upper()
    key = key.upper()

    # Ensuring the key is long enough
    if len(key) < len(plaintext):
        raise ValueError("Key must be at least as long as the plaintext")

    # Encryption process
    cipher = []
    for i in range(len(plaintext)):
        if 'A' <= plaintext[i] <= 'Z':  # Ignoring non-alphabetic characters
            pt_num = char_to_num(plaintext[i])
            key_num = char_to_num(key[i])
            cipher_num = (pt_num + key_num) % 26
            cipher.append(num_to_char(cipher_num))
        else:
            cipher.append(plaintext[i])  # Keeping non-alphabetic characters as-is

    return ''.join(cipher)

plaintext = "MERWYN"
key = "THISISANEXAMPLEKEYINCOMPUTERSECURITYEXAM"

cipher = encrypt_vigenere(plaintext, key)

print("Plaintext:", plaintext)
print("Key:", key[:len(plaintext)]) 
print("Cipher:", cipher)
