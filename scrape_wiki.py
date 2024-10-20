# Scrape Wikipedia using beautiful soup and store characters and respective code
# on a dictionary where the key is the character and the value is a list of
# Morse code chars. Run it directly from this module in case the file "code_list.json"
# does not exist or is corrupted.

import requests
from bs4 import BeautifulSoup
import json
import base64

# URL of the Wikipedia page
url = "https://en.wikipedia.org/wiki/Morse_code"
excluded_chars = ['ⓘ', '[h]', 'digraph', 'Slash', 'prosign', 'Prosign', 'Hyphen', '[i]']

# Send a GET request to the page
response = requests.get(url)

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find the table with class "wikitable sortable jquery-tablesorter"
table = soup.find("table", {"class": ["wikitable", "sortable", "jquery-tablesorter"]})

# Initialize an empty list to store the text values
morse_source_list = []

# Check if the table is found
if table:
    # Find all anchor (<a>) tags inside the table
    for a_tag in table.find_all("a"):
        # Get the text of each anchor and strip any extra whitespace
        chars = a_tag.get_text(strip=True)
        # test if list of latin characters ended
        if chars == 'Prosigns':
            break
        # exclude unwanted characters
        elif chars in excluded_chars:
            pass
        else:
            if chars.find('[') != -1:
                index = chars.find('[')
                chars = chars[index + 1]
            else:
                # split all characters and keep the lower-case/digit or character
                chars = chars.split(', ')[-1]
            morse_source_list.append(chars)

# creates a dictionary with characters as keys and morse codes as values
key_list = [char for char in morse_source_list if morse_source_list.index(char) % 2 == 0]
value_list = [char.encode('utf-8') for char in morse_source_list if morse_source_list.index(char) % 2 != 0]
char_dict = {k: base64.b64encode(v).decode('utf-8') for k, v in zip(key_list, value_list)}
char_dict[' '] = ' '

# store the resulting list on json file
with open('code_list.json', 'w') as file:
    json.dump(char_dict, file)


