sentence = 'This is a common interview question'
sentence = 'Pratik Priyadarshan Singh'
sentence = 'ABCD ABCD ABC AB A'

sentence = sentence.lower()
count_all = {}

for char in sentence:
    if char == ' ':
        continue
    if char in count_all:
        count_all[char] += 1
    else:
        count_all[char] = 1

most_repated_char = ''
count = 0

for char in count_all:
    if count_all[char] > count:
        most_repated_char = char
        count = count_all[char]

print(f'Most repeated character is {most_repated_char} with repetitions {count}')

