text = input()

words = text.split()

print("Words:", len(words))

longest = words[0]

for i in words:
    if len(i) > len(longest):
        longest = i

print("Longest:", longest)

count = {}

for ch in text:
    if ch == " ":
        continue

    if ch in count:
        count[ch] += 1
    else:
        count[ch] = 1

mostchar = ""
mostcount = 0

for ch in count:

    if count[ch] > mostcount:
        mostcount = count[ch]
        mostchar = ch

print("Most repeated char:", mostchar)