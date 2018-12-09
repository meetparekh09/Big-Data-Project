import os
import sys
import heapq
import re

base = '1_gram_probability/'
files = os.listdir(base)

print("========================================================================")
print("\t\tL O A D I N G  1 - G R A M  T E R M S")
print("========================================================================")

one_gram_probability = {}

for filename in files:
    file = open(base + filename, encoding='ISO-8859-1')
    for line in file:
        one_gram = line.split('\t')[0]
        prob = float(line.split('\t')[1])
        one_gram_probability[one_gram] = prob

print("Number of 1-gram terms loaded :: " + str(len(one_gram_probability.keys())))
print()
print()

#
# print("========================================================================")
# print("\t\tL O A D I N G  2 - G R A M  T E R M S")
# print("========================================================================")
#
# base = '2_gram_probability/'
# files = os.listdir(base)
#
# two_gram_probability = {}
#
# for filename in files:
#     file = open(base+filename, encoding='ISO-8859-1')
#     for line in file:
#         first = line.split('\t')[0]
#         second = line.split('\t')[1]
#         prob = float(line.split('\t')[2])
#         if first not in two_gram_probability:
#             two_gram_probability[first] = []
#         two_gram_probability[first].append((second, prob))
#
# length = 0
# for k in two_gram_probability.keys():
#     length += len(two_gram_probability[k])
#
# print("Number of 2-gram terms loaded :: " + str(length))
# print()
# print()


# ch = sys.stdin.readline().split('\n')[0]
# print(ch)
input = ''
with open('test') as file:
    for line in file:
        input += line.split('\n')[0]

input = re.sub(r'[^\w\s]','',input)
words = input.split(' ')

total_length = 0
predicted_length = 0

for word in words:
    word = word.lower()
    if len(word) <= 2:
        continue
    total_length += len(word)
    length = 0
    # print("Processing :: " + word)
    ch = ""
    for c in word:
        ch += c
        length+=1
        output = []
        for k in one_gram_probability.keys():
            if k.startswith(ch):
                output.append((k, one_gram_probability[k]))

        sorted(output, key=lambda x: x[1], reverse=True)
        top = []
        for o in output[:10]:
            top.append(o[0])

        # print(ch + ", "+ word + ", " + str(top_5))

        if word in top[:5]:
            predicted_length += len(word) - length
            print("Word Predicted :: " + word)
            break

    print("Total Length :: " + str(total_length))
    print("Predicted Length :: " + str(predicted_length))
