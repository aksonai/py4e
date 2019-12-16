# Exercise 3: Write a program that reads a file and prints the letters in decreasing
# order of frequency. Your program should convert all the input to lower case and
# only count the letters a-z. Your program should not count spaces, digits, punctua-
# tion, or anything other than the letters a-z. Find text samples from several different
# languages and see how letter frequency varies between languages. Compare your
# results with the tables at wikipedia.org/wiki/Letter_frequencies.

alphabet = 'abcdefghijklmnopqrstuvxwyz'

filename = input("Enter a file name: ")
fhand = open(filename, 'r')
text = fhand.read()

freq_dict = {}
for ch in text.lower():
    if ch in alphabet:
        freq_dict[ch] = freq_dict.get(ch, 0) + 1

lst = []
for key, value in freq_dict.items():
    lst.append((value,key))

lst.sort(reverse=True)
for freq, letter in lst:
    print(letter, freq)
