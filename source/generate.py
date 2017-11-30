import pickle
import random

"""
generate.py

Read $pickled_file and choose a
random key. Use the key to find
the next word, and then use the
current last 2 words to find a
new word
"""

pickled_file = "trained.pickle"
chain = ""

print("Loading trained dict")
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
        new_word = trained_dict[key]
        chain += new_word + " "
        w1 = w2
        w2 = new_word

        words_processed += 1
        print("\rWords processed: {}".format(words_processed), end="")

        if words_processed > 1000:
            break  # Prevents loops
    except KeyError:
        print("\nChain done:")
        break

print("\n" + chain)
