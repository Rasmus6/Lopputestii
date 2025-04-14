import random

def generate_password(length, special_characters_count, numbers_count):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()"
    numbers = "0123456789"

    if special_characters_count + numbers_count > length:
        print("Erikoismerkkien ja numeroiden yhteismäärä ei voi ylittää salasanan kokonaispituutta.")
        return None

    password = ""

    for _ in range(special_characters_count):
        password += random.choice(special_characters)

    for _ in range(numbers_count):
        password += random.choice(numbers)

    for _ in range(length - special_characters_count - numbers_count):
        password += random.choice(characters)

    password = ''.join(random.sample(password, len(password)))

    return password

password_length = int(input("Syötä haluamasi salasanan pituus: "))
special_characters_count = int(input("Syötä haluamasi määrä erikoismerkkejä: "))
numbers_count = int(input("Syötä haluamasi määrä numeroita: "))

generated_password = generate_password(password_length, special_characters_count, numbers_count)

if generated_password:
    print(f"Generated password: {generated_password}")
