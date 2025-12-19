# # from cryptography.fernet import Fernet

# # # Функция для генерации ключа
# # def generate_key():
# #     key = Fernet.generate_key()
# #     with open('secret.key', 'wb') as key_file:
# #         key_file.write(key)
# #     return key

# # # Функция для загрузки ключа
# # def load_key():
# #     return open('secret.key', 'rb').read()

# # # Функция для шифрования сообщения
# # def encrypt_message(message):
# #     key = load_key()
# #     fernet = Fernet(key)
# #     encrypted = fernet.encrypt(message.encode())
# #     return encrypted

# # # Функция для дешифрования сообщения
# # def decrypt_message(encrypted_message):
# #     key = load_key()
# #     fernet = Fernet(key)
# #     decrypted = fernet.decrypt(encrypted_message).decode()
# #     return decrypted

# # # Генерация ключа (раскомментируйте, если ключ ещё не сгенерирован)
# # key = generate_key()

# # # Пример использования
# # if __name__ == "__main__":
# #     user_input = input("Введите строку для шифрования: ")
# #     encrypted_message = encrypt_message(user_input)
# #     print(f"Зашифрованное сообщение: {encrypted_message}")

# #     # Для тестирования - дешифровка
# #     decrypted_message = decrypt_message(encrypted_message)
# #     print(f"Дешифрованное сообщение: {decrypted_message}")

# # # Функция для шифрования сообщения
# # def encrypt_message(message):
# #     key = load_key()
# #     fernet = Fernet(key)
# #     encrypted = fernet.encrypt(message.encode())
# #     return encrypted

# # # Функция для дешифрования сообщения
# # def decrypt_message(encrypted_message):
# #     key = load_key()
# #     fernet = Fernet(key)
# #     decrypted = fernet.decrypt(encrypted_message).decode()
# #     return decrypted

# # # Генерация ключа (раскомментируйте, если ключ ещё не сгенерирован)
# # key = generate_key()

# # # Пример использования
# # if __name__ == "__main__":
# #     user_input = input("Введите строку для шифрования: ")
# #     encrypted_message = encrypt_message(user_input)
# #     print(f"Зашифрованное сообщение: {encrypted_message}")

# #     # Для тестирования - дешифровка
# #     decrypted_message = decrypt_message(encrypted_message)
# #     print(f"Дешифрованное сообщение: {decrypted_message}")

# # def menu():
# #     print('Добро пожаловать в ')

# from cryptography.fernet import Fernet
# import os

# # Функция для генерации ключа
# def generate_key():
#     key = Fernet.generate_key()
#     with open('secret.key', 'wb') as key_file:
#         key_file.write(key)
#     return key

# # Функция для загрузки ключа
# def load_key():
#     return open('secret.key', 'rb').read()

# # Функция для шифрования файла
# def encrypt_file(filename):
#     key = load_key()
#     fernet = Fernet(key)

#     # Чтение изображения в бинарном формате
#     with open(filename, 'rb') as file:
#         original = file.read()

#     # Шифрование
#     encrypted = fernet.encrypt(original)

#     # Запись зашифрованного файла
#     with open(filename + '.enc', 'wb') as encrypted_file:
#         encrypted_file.write(encrypted)

# # Функция для дешифрования файла
# def decrypt_file(encrypted_filename):
#     key = load_key()
#     fernet = Fernet(key)

#     # Чтение зашифрованного файла
#     with open(encrypted_filename, 'rb') as encrypted_file:
#         encrypted = encrypted_file.read()

#     # Дешифрование
#     decrypted = fernet.decrypt(encrypted)

#     # Запись дешифрованного файла
#     with open(encrypted_filename[:-4], 'wb') as decrypted_file:
#         decrypted_file.write(decrypted)

# # Генерация ключа (раскомментируйте, если ключ еще не создан)
# # key = generate_key()

# if __name__ == "__main__":
#     action = input("Выберите действие (encrypt/decrypt): ")
#     filename = input("Введите имя файла (с расширением): ")

#     if action == "encrypt" or action == "e":
#         encrypt_file(filename)
#         print(f"{filename} был зашифрован!")
#     elif action == "decrypt" or action == "d":
#         decrypt_file(filename)
#         print(f"{filename} был дешифрован!")
#     else:
#         print("Неверное действие.")
