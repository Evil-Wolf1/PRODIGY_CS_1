def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            elif char.isupper():
                encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                decrypted_text += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            elif char.isupper():
                decrypted_text += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
        else:
            decrypted_text += char
    return decrypted_text

def main():
    print("Welcome to Caesar Cipher!")
    print("**************************")
    print("1 : Enter  to encrypt a message.")
    print("2 : Enter  to decrypt a message.")
    option = input("Choose an option (1 or 2): ")

    if option not in ['1', '2']:
        print("Invalid option. Please choose '1' or '2'.")
        return
    
    message = input("Enter the message: ")
    shift = input("Enter the shift value (a positive number): ")

    if not shift.isdigit() or int(shift) < 1:
        print("Shift value must be a positive integer.")
        return

    shift = int(shift)

    if option == '1':
        result = encrypt(message, shift)
        print("\n*** Encryption Result ***")
        print("Encrypted message:", result)
    else:
        result = decrypt(message, shift)
        print("\n*** Decryption Result ***")
        print("Decrypted message:", result)

    print("**************************")

if __name__ == "__main__":
    main()
