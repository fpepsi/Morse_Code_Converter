# Ask for a sentence with 26 letters of alphabet and / or arabic numbers
# Split sentence into a list of individual characters. Use list comprehension to replace unknown characters
# with a dollar sign.
# Create a new list where components are lists with each character's morse code
# create a loop to print each list item and generate the sound
import json
import base64
from sound import MorseSound as ms

# retrieves the file containing the Morse code dictionary
with open('code_list.json', 'r') as file:
    encoded_morse_dict = json.load(file)

invalid = True
sentence_chars = []
while invalid:
    # get the user sentence to be translated to Morse code
    sentence = input("What is the sentence you would like to convert to Morse code? ")
    # split the sentence into a list of words and check if all words are in the Morse dictionary
    sentence_chars = [char.lower() for char in sentence]
    invalid_chars = [key for key in sentence_chars if key not in list(encoded_morse_dict.keys()) and key != ' ']
    if len(invalid_chars) == 0:
        invalid = False
    else:
        print("\n The characters below are invalid: \n")
        print(invalid_chars)

# create list with the sentence's morse code values
morse_code_translation = []
for char in sentence_chars:
    morse_code_translation.append(base64.b64decode(encoded_morse_dict[char]).decode('utf-8').replace('\xa0', ' '))

# print and sound the morse code
morse_sound = ms()
morse_sound.play_morse_code(sentence_chars, morse_code_translation)

# decoded_morse_dict = {k: base64.b64decode(v.encode('utf-8')) for k, v in encoded_morse_dict.items()}
# print(decoded_morse_dict['a'], decoded_morse_dict['a'].decode('utf-8'))