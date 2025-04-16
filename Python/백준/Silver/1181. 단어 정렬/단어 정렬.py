t = int(input())
words = []
for i in range(t):
    w = input()
    words.append((w, len(w)))
words = list(set(words))
words = sorted(words, reverse=False, key= lambda w : (w[1], w[0]))
for w in words:
    print(w[0])