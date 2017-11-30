import pickle
import random

"""
generate.py

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

pickled_file = "trained.pickle"
chain = ""

print("Loading dictionary")
with open(pickled_file, "rb") as f:
    trained_dict = pickle.load(f)

print("Generating chain...")
key = random.choice(list(trained_dict))
chain += key + " "

words_processed = 2
w1 = key.split(" ")[0]
w2 = key.split(" ")[1]

while 1:
    try:
        key = "{} {}".format(w1, w2)
        values = trained_dict[key]
        new_word = random.choice(values)
        
        chain += new_word + " "
        w1 = w2
        w2 = new_word

        words_processed += 1
        print("\rWords processed: {}".format(words_processed), end="")

        if words_processed == WORD_LIMIT:
            break  # Prevents loops
    except KeyError:
        break

print("\nChain done:")
print("\n" + chain)
