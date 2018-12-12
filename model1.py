import os
import sys
import heapq
import re
import time
import matplotlib.pyplot as plt
import math

base = '1_gram_probability/'
files = os.listdir(base)

print("===================================================================================================================")
print("\t\tL O A D I N G  1 - G R A M  T E R M S")
print("===================================================================================================================")

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


print("===================================================================================================================")
print("\t\tL O A D I N G  2 - G R A M  T E R M S")
print("===================================================================================================================")

base = '2_gram_probability/'
files = os.listdir(base)

two_gram_probability = {}

for filename in files:
    file = open(base+filename, encoding='ISO-8859-1')
    for line in file:
        first = line.split('\t')[0]
        second = line.split('\t')[1]
        prob = float(line.split('\t')[2])
        if first not in two_gram_probability:
            two_gram_probability[first] = {}
        two_gram_probability[first][second] = prob

length = 0
for k in two_gram_probability.keys():
    length += len(two_gram_probability[k])

print("Number of 2-gram terms loaded :: " + str(length))
print()
print()


input = ''
with open('test') as file:
    for line in file:
        input += line.split('\n')[0]

input = re.sub(r'[^\w\s]','',input)
words = input.split(' ')

total_length = 0
predicted_length = 0

previous_word = ""
times = [0.00001, 0.0001, 0.001, 0.01, 0.1, 0, 1, 10, 100, 1000, 10000, 100000]
avg_response_times = []
predictions = []

for i in times:
    avg_time = 0
    tot_length = 0
    for word in words:
        word = word.lower()
        if len(word) <= 2:
            continue
        total_length += len(word)

        output_2 = None
        if previous_word in two_gram_probability.keys():
            output_2 = two_gram_probability[previous_word]

        length = 0
        ch = ""
        for c in word:
            tot_length += 1
            t1 = time.time()
            ch += c
            length+=1
            output = {}
            for k in one_gram_probability.keys():
                if k.startswith(ch):
                    output[k] = one_gram_probability[k]
                    if output_2 is not None and k in output_2.keys():
                        output[k] += i*output_2[k]

            output = sorted(output.items(), key=lambda x: x[1], reverse=True)
            top = []
            for o in output[:5]:
                top.append(o[0])
            t2 = time.time()
            avg_time += (t2-t1)
            if word in top[:5]:
                predicted_length += len(word) - length
                # print("Word Predicted :: " + word)
                break

        previous_word = word

    avg_response_times.append(avg_time/tot_length)
    predictions.append(predicted_length/total_length)

    print()
    print("===================================================================================================================")
    print("i :: " + str(i) + ", Keystrokes Percent saved :: " + str(predicted_length/total_length) + ", Time Take :: " + str(avg_time/tot_length))
    print("===================================================================================================================")
    print()

average = sum(avg_response_times) / len(avg_response_times)
# times = [math.log10(x) for x in times]

print("===================================================================================================================")
print("\t\tAverage response time per character :: " + str(average))
print("===================================================================================================================")


print(times)
print(average)
print(predictions)
