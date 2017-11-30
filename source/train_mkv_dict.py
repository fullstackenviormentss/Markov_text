import pickle

"""
train_markov_dict.py

Read $training_file and construct a
dictionary of {2 words : next word}
then save to $pickled_file
"""

WORD_LIMIT = 100000  # None for all the words in the file

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
    trained_dict[w1 + " " + w2] = word
    w1 = w2
    w2 = word
    words_processed += 1
    print("\rWords processed: {}".format(words_processed), end="")
print()  # Newline

print("Dumping trained dict to {}".format(pickled_file))
with open(pickled_file, "wb") as f:
    pickle.dump(trained_dict, f)

print("Done!")
