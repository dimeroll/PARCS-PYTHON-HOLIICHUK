import string, random

strings = []
for _ in range(3000000):
    is_psevdo_palindrome = bool(random.choice([0, 1]));
    s = ''.join(random.choices(string.ascii_letters, k=random.randint(1, 10)))

    if is_psevdo_palindrome:
        s1 = ''
        for c in s:
            s1 += chr(ord(c) + 1)
        s += s1[::-1]
    strings.append(s)

with open('input.txt', 'w') as f:
    for s in strings:
        f.write(s + '\n')