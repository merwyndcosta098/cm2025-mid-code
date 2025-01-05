def decrypt_vigenere(ciphertext, key):
    # Assigning numeric values to letters
    def char_to_num(c):
        return ord(c) - ord('A')
    
    def num_to_char(n):
        return chr(n + ord('A'))

    # Converting ciphertext and key to uppercase
    ciphertext = ciphertext.upper()
    key = key.upper()

    # Ensuring the key is long enough
    if len(key) < len(ciphertext):
        raise ValueError("Key must be at least as long as the ciphertext")

    # Decryption process
    plaintext = []
    for i in range(len(ciphertext)):
        if 'A' <= ciphertext[i] <= 'Z':  # Ignoring non-alphabetic characters
            ct_num = char_to_num(ciphertext[i])
            key_num = char_to_num(key[i])
            pt_num = (ct_num - key_num + 26) % 26
            plaintext.append(num_to_char(pt_num))
        else:
            plaintext.append(ciphertext[i])  # Keeping non-alphabetic characters as-is

    return ''.join(plaintext)

ciphertext = "FLZOGF"
key = "THISISANEXAMPLEKEYINCOMPUTERSECURITYEXAM"

plaintext = decrypt_vigenere(ciphertext, key)

print("Ciphertext:", ciphertext)
print("Key:", key[:len(ciphertext)])  
print("Plaintext:", plaintext)
