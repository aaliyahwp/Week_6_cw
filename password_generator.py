
import random
# Chosen to use the secrets module as opposed to the random module as this is more secure
import string
import secrets

characters = string.digits + string.punctuation + string.ascii_lowercase + string.ascii_uppercase
# characters is made out of digits punctuation, and lower and uppercase lettes from a -z

password = ''. join(secrets.choice(characters) for i in range (10))
# Join is a funtion used to take seperate iterables (in this case the values from the forloop) and combining them into one string
# Created a For loop using the range function, the value 10 means we the code will be run 10 times producing 10 values which makeup the password
print("Your random password is:", password)


