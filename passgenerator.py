import random
alphabets = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
sign = "!@#$%^&*()_+"
rand = alphabets+numbers+sign
length=int(input("Enter the length of password: "))
PassGenatr = "".join(random.sample(rand,length))
print("Password :"+PassGenatr)
