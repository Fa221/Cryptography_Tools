c = str(input('What word would you like to encrypt--> '))
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
key = str(input("Enter the key --> "))
x = key.replace(" ", "")
lowercase = x.lower()
c.lower()
cipher = []
for l in c:
    cipher.append(l)
final_cipher = []
for let in cipher:
    if let in letters:
        letters.remove(let)
for i in cipher:
    if i not in final_cipher:
        final_cipher.append(i)
final = final_cipher + letters
for elmo in range(0, len(lowercase), 2)]:
    lol = [lowercase[elmo:elmo + 2] 
print(lol)
