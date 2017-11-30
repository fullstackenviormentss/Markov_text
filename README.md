# Markov_text

Generate text using Markov chains

## `train_mkv_dict.py`

This file creates and saves a dictionary to `trained.pickle`. The script reads plain text from `to_read.txt` (not supplied) and creates a dictionary that looks like `{2 words : 1 word}`.

For example, if the text had this string in it:
`"this is a great repo"`
the dictionary would look like:
`{"this is": "a", "is a": "great", "a great": "repo"}`

This is based off of [this stackoverflow answer](https://stackoverflow.com/a/5307230)

At the top of the script there is a variable, `WORD_LIMIT`: this limits the amount of words read from the text file. Change this to however many you want, or set it to `None` to read all the words

## `generate.py`

This script reads `trained.pickle` (the previously created dictionary) and generate a string.

The steps taken to generate this string are:

 - Pick a random key from the dictionary
 - Add those words and their value to a string
 - Use the last two words in the string as a new key
 - If there is a value in the dictionary, go back to step 2, otherwise, stop and show what has been made

Currently it will stop adding to the string if either there is no value for a key, or if the amount of words used goes over `1000`. This is to stop loops or insanely long chains.

# Resources

A good `to_read.txt` to try is [this shakespear play](https://ocw.mit.edu/ans7870/6/6.006/s08/lecturenotes/files/t8.shakespeare.txt). Before using it, I would remove the copyright warnings (they appear throughout the text)