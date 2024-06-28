class CaesarCipher:
    def __init__(self, shift):
        self.shift = shift % 26  # Ensure the shift is within the range of 0-25

    def encrypt(self, text):
        encrypted_text = ""
        for char in text:
            if char.isalpha():
                shifted = ord(char) + self.shift
                if char.islower():
                    if shifted > ord('z'):
                        shifted -= 26
                elif char.isupper():
                    if shifted > ord('Z'):
                        shifted -= 26
                encrypted_text += chr(shifted)
            else:
                encrypted_text += char
        return encrypted_text

    def decrypt(self, text):
        decrypted_text = ""
        for char in text:
            if char.isalpha():
                shifted = ord(char) - self.shift
                if char.islower():
                    if shifted < ord('a'):
                        shifted += 26
                elif char.isupper():
                    if shifted < ord('A'):
                        shifted += 26
                decrypted_text += chr(shifted)
            else:
                decrypted_text += char
        return decrypted_text

def main():
    print("Welcome to the Caesar Cipher program!")
    while True:
        mode = input("Would you like to (E)ncrypt or (D)ecrypt a message? (Enter E or D, or Q to quit): ").strip().upper()
        if mode == 'Q':
            print("Goodbye!")
            break
        if mode not in ['E', 'D']:
            print("Invalid option. Please enter E, D, or Q.")
            continue

        shift = int(input("Enter the shift value (0-25): ").strip())
        message = input("Enter the message: ").strip()

        cipher = CaesarCipher(shift)

        if mode == 'E':
            result = cipher.encrypt(message)
            print(f"Encrypted message: {result}")
        elif mode == 'D':
            result = cipher.decrypt(message)
            print(f"Decrypted message: {result}")

if __name__ == "__main__":
    main()
