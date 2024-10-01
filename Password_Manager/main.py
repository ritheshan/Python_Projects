from cryptography.fernet import Fernet
import os

# Step 1: Generate and load key
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("secret.key", "rb").read()

# Step 2: Encrypt and decrypt passwords
def encrypt_password(password):
    key = load_key()
    f = Fernet(key)
    encrypted_password = f.encrypt(password.encode())
    return encrypted_password

def decrypt_password(encrypted_password):
    key = load_key()
    f = Fernet(key)
    decrypted_password = f.decrypt(encrypted_password).decode()
    return decrypted_password

# Step 3: Store and retrieve passwords
def save_password(website, username, password):
    encrypted_password = encrypt_password(password)
    with open("passwords.txt", "a") as f:
        f.write(f"{website}|{username}|{encrypted_password.decode()}\n")
def load_passwords():
    try:
        with open("passwords.txt", "r") as f:
            for line in f.readlines():
                website, username, encrypted_password = line.strip().split("|")
                decrypted_password = decrypt_password(encrypted_password.encode())
                print(f"Website: {website}, Username: {username}, Password: {decrypted_password}")
    except FileNotFoundError:
        print("No password file found. A new one will be created.")
        open("passwords.txt", "w").close()


# Step 4: User interface
def main():
    if not os.path.exists("secret.key"):
            generate_key()
    while True:
        choice = input("\nWould you like to (1) add a new password or (2) view passwords? (q to quit): ")

        if choice == "1":
            website = input("Website: ")
            username = input("Username: ")
            password = input("Password: ")
            save_password(website, username, password)

        elif choice == "2":
            load_passwords()

        elif choice == "q":
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":


    main()
