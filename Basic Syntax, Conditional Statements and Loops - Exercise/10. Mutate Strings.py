word1 = input()
word2 = input()

new = ''
add = ''

for i in range(len(word1)):
    if word1[i] == word2[i]:
        add = word1[i]
        new += add
    else:
        add = word2[i]
        new += add
        new1 = new
        for j in range(i + 1, len(word1)):
            new1 += word1[j]
        print(new1)
