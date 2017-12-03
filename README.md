# Markov_text

Give a large amount of text as an input and this will generate text from that input using Markov chains

**Usage**:

 - Find whatever text you want to use and put it in `source/` as `to_read.txt` (it should be plain ASCII text)
 - Edit the `WORD_LIMIT` & `NUMBER_OF_KEY_WORDS` variables in both Python scripts to your preference (read below)
 - Open a terminal / command prompt in `source/`
 - Run `python3 train_mkv_dict.py`
 - Run `python3 generate.py`
 - You should now have some *interesting* text to read

**Warnings**

 - Using a large number for `NUMBER_OF_KEY_WORDS` will not produce very random results
 - Using a very small `WORD_LIMIT` may break the generation or just cause predictable results

## `train_mkv_dict.py`

This file creates and saves a dictionary to `trained.pickle`. The script reads plain text from `to_read.txt` (not supplied) and creates a dictionary that looks like `{{NUMBER_OF_KEY_WORDS} words : [next word(s)]}`.

For example, if the text had this string in it and `NUMBER_OF_KEY_WORDS` equal to `2`:
`"this is a great repo this is gud"`
the dictionary would look like:
`{"this is": ["a", "gud"], "is a": ["great"], "a great": ["repo"], "repo this": ["is"]}`

This is based off of [this stackoverflow answer](https://stackoverflow.com/a/5307230)

**Notes:**

 - All whitespace in `to_read.txt` is ignored

 - `NUMBER_OF_KEY_WORDS` is the number of words to use for each key when generating the dictionary

 - At the top of the script there is a variable, `WORD_LIMIT`: this limits the amount of words read from the text file. Change this to however many you want, or set it to `None` to read all the words

## `generate.py`

This script reads `trained.pickle` (the previously created dictionary) and generate a string.

The steps taken to generate this string are:

 - Pick a random key from the dictionary
 - Add those words to a string
 - Get a random word from the dictionary value(s) of that key and add that to the string
 - Use the last `NUMBER_OF_KEY_WORDS` in the string as a new key
 - If there is a value in the dictionary, go back to step 3 with the new key, otherwise, stop and show what has been made

**Notes:**

 - At the top of the script there is a variable, `WORD_LIMIT`: this is the maximum amount of words that can be in a chain

 - Currently it will stop adding to the string if either there is no value for a key, or if the amount of words used goes over `WORD_LIMIT`. This is to stop loops or insanely long chains.

# Resources

A good `to_read.txt` to try is [this shakespear play](https://ocw.mit.edu/ans7870/6/6.006/s08/lecturenotes/files/t8.shakespeare.txt). Before using it, I would remove the copyright warnings (they appear throughout the text)

There are thousands of plaintext books available [here](https://www.gutenberg.org/wiki/Main_Page)

You can find plaintext transcripts of films and TV series [here](https://www.springfieldspringfield.co.uk)
