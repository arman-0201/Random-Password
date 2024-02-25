import random
import string

def generatepassword(length):
    return ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))

password_length = int(input())
print("Generated Password:", generatepassword(password_length))
