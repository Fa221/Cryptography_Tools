def rail_fence_cipher(text, key):
    rail = [['\n' for i in range(len(text))] for j in range(key)]
    direction = False
    row, col = 0, 0

    for char in text:
        if row == 0 or row == key - 1:
            direction = not direction
        rail[row][col] = char
        col += 1
        row += 1 if direction else -1

    result = []
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])
    return "".join(result)

text = input("Enter text: ")
key = int(input("Enter number of rails: "))
print("Cipher: " + rail_fence_cipher(text, key))

