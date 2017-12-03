import pickle

"""
train_markov_dict.py

All strings are acutally byte
strings so that things like emoji
are preserved

$NUMBER_OF_KEY_WORDS is the number
of words to use for each key when
generating the dictionary

$WORD_LIMIT limits the amount of words
read from the text file. Change this
to however many you want, or set it
to None to read the whole file
"""

NUMBER_OF_KEY_WORDS = 2
WORD_LIMIT = None  # None for all the words in the file
BYTE_SPACE = b" "
print("Word limit:", WORD_LIMIT, "\nNumber of words in key:", NUMBER_OF_KEY_WORDS)

training_file = "to_read.txt"
plain_text = b""  # Empty bytes
trained_dict = {}
pickled_file = "trained.pickle"

print("Reading file")
with open(training_file, "rb") as f:
    text = f.readlines()

print("Constructing safe string")
# Construct one long string with just words
# (no newlines, extra whitespace, etc.)
for line in text:
    line = line.strip()
    if not line:
        continue
    plain_text += line + BYTE_SPACE

print("Training model:")
word_list = plain_text.split(BYTE_SPACE)
words_processed = NUMBER_OF_KEY_WORDS
previous_words = word_list[:NUMBER_OF_KEY_WORDS]

for word in word_list[NUMBER_OF_KEY_WORDS:WORD_LIMIT]:
    key = BYTE_SPACE.join(previous_words)
    if key in trained_dict:
        trained_dict[key].append(word)
    else:
        trained_dict[key] = [word]
    # Shift previous words right by 1 word
    previous_words.pop(0)
    previous_words.append(word)
    words_processed += 1

print("Words processed: {}".format(words_processed))
print("Dumping trained dict to {}".format(pickled_file))
with open(pickled_file, "wb") as f:
    pickle.dump(trained_dict, f)

print("Done!")
