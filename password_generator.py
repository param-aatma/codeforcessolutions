import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to password generator")

n = int(input("Number of numbers: "))
a = int(input("Number of alphabets: "))
s = int(input("Number of symbols: "))

password = []

for char in range(0, a):
  password += (random.choice(letters))


for char in range(0, s):
  password += (random.choice(symbols))

for char in range(0, n):
  password += (random.choice(numbers))

random.shuffle(password)

print("Your password is: " + (''.join(password))) 


"""Hard Level
password_list = []

for char in range(0, a):
  password_list.append(random.choice(letters))

for char in range(0, s):
  password_list += random.choice(symbols)

for char in range(0, n):
  password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")"""