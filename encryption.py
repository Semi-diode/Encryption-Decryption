def encrypt(message, shift):
    result = ""

    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char

    return result


def decrypt(message, shift):
    return encrypt(message, -shift)


print("===== ENCRYPTION AND DECRYPTION PROGRAM =====")

message = input("Enter your message: ")
shift = int(input("Enter shift number: "))

encrypted_message = encrypt(message, shift)
decrypted_message = decrypt(encrypted_message, shift)

print("\nOriginal Message:", message)
print("Encrypted Message:", encrypted_message)
print("Decrypted Message:", decrypted_message)