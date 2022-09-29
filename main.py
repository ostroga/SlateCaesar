alphabet = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w",
    "x", "y", "z"
    ]

phrase = str(input())
result = ""

for item in phrase:
    try:
        current_index = alphabet.index(item.lower())
        if current_index + 3 > - len(alphabet):
            new_index = current_index + 3 - len(alphabet)
        else:
            new_index = current_index + 3
        result += alphabet[new_index]
    except ValueError:
        result += item

print(result)