import random
import string

password_length = int (input("Enter the length of password : "))

characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choices(characters  , k=password_length))

print ("Generated password ", password)