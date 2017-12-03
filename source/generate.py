import pickle
import random

"""
generate.py

All strings are acutally byte
strings so that things like emoji
are preserved

Read $pickled_file and choose a
random key. Use the key to find
the next word, and then use the
current last 2 words to find a
new word

$WORD_LIMIT is the maximum 
amount of words a chain can
contain
"""

WORD_LIMIT = 100
BYTE_SPACE = b" "
print("Word limit:", WORD_LIMIT)

pickled_file = "trained.pickle"
chain = b""

print("Loading dictionary")
with open(pickled_file, "rb") as f:
    trained_dict = pickle.load(f)

print("Generating chain...")
key = random.choice(list(trained_dict))

print("Starting key:", key)
chain += key

NUMBER_OF_KEY_WORDS = len(key.split(BYTE_SPACE))
words_processed = NUMBER_OF_KEY_WORDS
print("Number of words in each key:", NUMBER_OF_KEY_WORDS)

while 1:
    try:
        key =  BYTE_SPACE.join(chain.split(BYTE_SPACE)[(-NUMBER_OF_KEY_WORDS):])

        values = trained_dict[key]
        new_word = random.choice(values)

        chain += (BYTE_SPACE + new_word)
        words_processed += 1

        if words_processed == WORD_LIMIT:
            break  # Helps prevent loops
    except KeyError:
        break

print("Words processed: {}".format(words_processed))
print("Chain done:")
print()
print(chain)
