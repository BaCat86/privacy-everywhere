from cryptography.fernet import Fernet

# Функция для генерации ключа
def generate_key():
    key = Fernet.generate_key()
    with open('secret.key', 'wb') as key_file:
        key_file.write(key)
    return key

# Функция для загрузки ключа
def load_key():
    return open('secret.key', 'rb').read()

# Функция для шифрования сообщения
def encrypt_message(message):
    key = load_key()
    fernet = Fernet(key)
    encrypted = fernet.encrypt(message.encode())
    return encrypted

# Функция для дешифрования сообщения
def decrypt_message(encrypted_message):
    key = load_key()
    fernet = Fernet(key)
    decrypted = fernet.decrypt(encrypted_message).decode()
    return decrypted

# Функция для шифрования файла
def encrypt_file(filename):
    key = load_key()
    fernet = Fernet(key)
    with open(filename, 'rb') as file:
        original = file.read()
    encrypted = fernet.encrypt(original)
    with open(filename + '.enc', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

# Функция для дешифрования файла
def decrypt_file(encrypted_filename):
    key = load_key()
    fernet = Fernet(key)
    with open(encrypted_filename, 'rb') as encrypted_file:
        encrypted = encrypted_file.read()
    decrypted = fernet.decrypt(encrypted)
    with open(encrypted_filename[:-4], 'wb') as decrypted_file:
        decrypted_file.write(decrypted)

# Генерация ключа (раскомментируйте, если ключ еще не создан)
# key = generate_key()

if __name__ == "__main__":
    while True:
        print("\nВыберите действие:")
        print("1. Шифровать сообщение")
        print("2. Дешифровать сообщение")
        print("3. Шифровать файл")
        print("4. Дешифровать файл")
        print("5. Выход")

        choice = input("Введите номер действия: ")

        if choice == "1":
            user_input = input("Введите строку для шифрования: ")
            encrypted_message = encrypt_message(user_input)
            print(f"Зашифрованное сообщение: {encrypted_message}")

        elif choice == "2":
            encrypted_message = input("Введите зашифрованное сообщение: ")
            decrypted_message = decrypt_message(encrypted_message.encode())
            print(f"Дешифрованное сообщение: {decrypted_message}")

        elif choice == "3":
            filename = input("Введите имя файла (с расширением): ")
            encrypt_file(filename)
            print(f"{filename} был зашифрован!")

        elif choice == "4":
            encrypted_filename = input("Введите имя зашифрованного файла (с расширением): ")
            decrypt_file(encrypted_filename)
            print(f"{encrypted_filename} был дешифрован!")

        elif choice == "5":
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")
