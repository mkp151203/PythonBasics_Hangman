try:
    from cryptography.fernet import Fernet
except:
    print('downloading resources.....(please wait)')
    import os
    crypto = lambda: os.system('pip install cryptography')
    crypto()
    print('installation complete.')
    from cryptography.fernet import Fernet
def generate_key():
    # Generate a new encryption key
    key = Fernet.generate_key()
    with open("encryption_key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    # Load the encryption key from the file
    with open("encryption_key.key", "rb") as key_file:
        return key_file.read()

def encrypt_file(file_path, key):
    cipher = Fernet(key)
    with open(file_path, "rb") as file:
        file_data = file.read()
    encrypted_data = cipher.encrypt(file_data)
    with open(file_path, "wb") as file:
        file.write(encrypted_data)

def decrypt_file(file_path, key):
    cipher = Fernet(key)
    with open(file_path, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = cipher.decrypt(encrypted_data)
    with open(file_path, "wb") as file:
        file.write(decrypted_data)

try:
    key = load_key()
    file_path = "score.txt"
    decrypt_file(file_path, key)
    encrypt_file(file_path,key)
    print('requirement already satisfied')
except:
    generate_key()
    key = load_key()
    file_path = "score.txt"
    encrypt_file(file_path, key)
    print('key generated')
    
