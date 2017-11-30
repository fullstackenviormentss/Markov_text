import pickle

"""
train_markov_dict.py

Read $training_file and construct a
dictionary of {2 words : [next word(s)]}
then save to $pickled_file
"""

WORD_LIMIT = None  # None for all the words in the file

training_file = "to_read.txt"
plain_text = ""
trained_dict = {}
pickled_file = "trained.pickle"

print("Reading file")
with open(training_file, "r") as f:
    text = f.readlines()

print("Constructing string")
# Construct one long string with just words
# (no newlines, extra whitespace, etc.)
for line in text:
    line = line.strip()
    if line == "":
        continue
    plain_text += line + " "

print("Training model:")
word_list = plain_text.split(" ")
words_processed = 2
w1 = word_list[0]
w2 = word_list[1]

for word in word_list[2:WORD_LIMIT]:
    new_key = w1 + " " + w2
    if new_key in trained_dict:
        trained_dict[new_key].append(word)
    else:
        trained_dict[new_key] = [word]
    w1 = w2
    w2 = word
    words_processed += 1
    print("\rWords processed: {}".format(words_processed), end="")
print()  # Newline

print("Dumping trained dict to {}".format(pickled_file))
with open(pickled_file, "wb") as f:
    pickle.dump(trained_dict, f)

print("Done!")
