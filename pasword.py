import random

characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password_length = int(input("Введіть бажану довжину пароля: "))
generated_password = ""
for _ in range(password_length):
    generated_password += random.choice(characters)
print("Згенерований пароль:", generated_password)
