"""
CSE212 
(c) BYU-Idaho
06-Prove

It is a violation of BYU-Idaho Honor Code to post or share this code with others or 
to post it online.  Storage into a personal and private repository (e.g. private
GitHub repository, unshared Google Drive folder) is acceptable.
"""

#############
# Problem 1 #
#############

class Translator:
    """
    This class provides the capability of a translator.  A
    Python Dictionary is used to keep track of the mapping 
    of words from one language to another language.  You should 
    assume that there is only one translation for every 
    word (and vice versa).
    """

    def __init__(self):
        """ 
        Initialize the Python Dictionary to store word mappings
        """
        self.words = dict()

    def add_word(self, from_word, to_word):
        """
        Add the translation from 'from_word' to 'to_word'
        For example, in an English to German dictionary:

        my_translator.add_word("book", "buch")
        """
        self.words[from_word] = to_word

    def translate(self, from_word):
        """
        Translate a word and return the result. If the word 
        cannot be translated, then "???" is returned.  
        For example, in an English to German dictionary:

        german_word = my_translator.translate("book")
        """
        if from_word in self.words:
            return self.words[from_word]
        else:
            return "???"


# Sample Test Cases (may not be comprehensive) 
print("\n=========== PROBLEM 1 TESTS ===========")
english_to_german = Translator()
english_to_german.add_word("House", "Haus")
english_to_german.add_word("Car", "Auto")
english_to_german.add_word("Plane", "Flugzeug")
print(english_to_german.translate("Car"))  # Auto
print(english_to_german.translate("Plane"))  # Flugzeug
print(english_to_german.translate("Train"))  # ???


#############
# Problem 2 #
#############

def summarize_degrees(filename):
    """
    Read a census file and summarize the degrees (education)
    earned by those contained in the file.  The summary
    should be stored in a dictionary where the key is the
    degree earned and the value is the number of people that 
    have earned that degree.  The degree information is in
    the 4th column of the file.  There is no header row in the
    file.
    """
    degrees = dict()

    with open(filename) as file_in:
        for line in file_in:
            fields = line.split(",")
            degree = fields[3].strip()  # Extract the degree from the 4th column

            if degree in degrees:
                degrees[degree] += 1
            else:
                degrees[degree] = 1

    return degrees

# Sample Test Cases (may not be comprehensive) 
print("\n=========== PROBLEM 2 TESTS ===========")
print(summarize_degrees("census.txt")) # You might need to add a path for the file
# Results may be in a different order:
# {'Bachelors': 5355, 'HS-grad': 10501, '11th': 1175, 
# 'Masters': 1723, '9th': 514, 'Some-college': 7291, 
# 'Assoc-acdm': 1067, 'Assoc-voc': 1382, '7th-8th': 646, 
# 'Doctorate': 413, 'Prof-school': 576, '5th-6th': 333, 
# '10th': 933, '1st-4th': 168, 'Preschool': 51, 
# '12th': 433}   

#############
# Problem 3 #
#############

def is_anagram(word1, word2):
    # Remove spaces and convert both words to lowercase
    word1 = word1.replace(" ", "").lower()
    word2 = word2.replace(" ", "").lower()

    # Check if the lengths of the words are the same
    if len(word1) != len(word2):
        return False

    # Count the occurrences of each letter in word1
    letter_count = {}
    for letter in word1:
        letter_count[letter] = letter_count.get(letter, 0) + 1

    # Compare the letter counts in word2
    for letter in word2:
        if letter not in letter_count:
            return False
        letter_count[letter] -= 1
        if letter_count[letter] == 0:
            del letter_count[letter]

    # If all letters in word2 have been accounted for, it is an anagram
    return len(letter_count) == 0

# Sample Test Cases
print("\n=========== PROBLEM 3 TESTS ===========")
print(is_anagram("CAT", "ACT"))  # True
print(is_anagram("DOG", "GOOD"))  # False
print(is_anagram("AABBCCDD", "ABCD"))  # False
print(is_anagram("ABCCD", "ABBCD"))  # False
print(is_anagram("BC", "AD"))  # False
print(is_anagram("Ab", "Ba"))  # True
print(is_anagram("A Decimal Point", "Im a Dot in Place"))  # True
print(is_anagram("tom marvolo riddle", "i am lord voldemort"))  # True
print(is_anagram("Eleven plus Two", "Twelve Plus One"))  # True
print(is_anagram("Eleven plus One", "Twelve Plus One"))  # False


#############
# Problem 4 #
#############

class Maze:
    """
    Defines a maze using a dictionary. The dictionary is provided by the
    user when the Maze object is created. The dictionary will contain the
    following mapping:

    (x, y): (left, right, up, down)

    'x' and 'y' are integers and represent locations in the maze.
    'left', 'right', 'up', and 'down' are booleans and represent valid directions.

    If a direction is False, then we can assume there is a wall in that direction.
    If a direction is True, then we can proceed.

    If there is a wall, then display "Can't go that way!". If there is no wall,
    then the 'curr_x' and 'curr_y' values should be changed.
    """

    def __init__(self, maze_map):
        """
        Initialize the map. We assume that (1,1) is a valid location in
        the maze.
        """
        self.maze_map = maze_map
        self.curr_x = 1
        self.curr_y = 1

    def move_left(self):
        """
        Check to see if you can move left. If you can, then move. If you
        can't move, then display "Can't go that way!"
        """
        if self.maze_map[(self.curr_x, self.curr_y)][0]:
            self.curr_x -= 1
            print("Going left!")
        else:
            print("Can't go that way!")

    def move_right(self):
        """
        Check to see if you can move right. If you can, then move. If you
        can't move, then display "Can't go that way!"
        """
        if self.maze_map[(self.curr_x, self.curr_y)][1]:
            self.curr_x += 1
            print("Going right!")
        else:
            print("Can't go that way!")

    def move_up(self):
        """
        Check to see if you can move up. If you can, then move. If you
        can't move, then display "Can't go that way!"
        """
        if self.maze_map[(self.curr_x, self.curr_y)][2]:
            self.curr_y -= 1
            print("Going up!")
        else:
            print("Can't go that way!")

    def move_down(self):
        """
        Check to see if you can move down. If you can, then move. If you
        can't move, then display "Can't go that way!"
        """
        if self.maze_map[(self.curr_x, self.curr_y)][3]:
            self.curr_y += 1
            print("Going down!")
        else:
            print("Can't go that way!")

    def show_status(self):
        print("Current location (x={}, y={})".format(self.curr_x, self.curr_y))


# Sample Test Cases (may not be comprehensive)
map = {(1, 1): (False, True, False, True),
       (1, 2): (False, True, True, False),
       (1, 3): (False, False, False, False),
       (1, 4): (False, True, False, True),
       (1, 5): (False, False, True, True),
       (1, 6): (False, False, True, False),
       (2, 1): (True, False, False, True),
       (2, 2): (True, False, True, True),
       (2, 3): (False, False, True, True),
       (2, 4): (True, True, True, False),
       (2, 5): (False, False, False, False),
       (2, 6): (False, False, False, False),
       (3, 1): (False, False, False, False),
       (3, 2): (False, False, False, False),
       (3, 3): (False, False, False, False),
       (3, 4): (True, True, False, True),
       (3, 5): (False, False, True, True),
       (3, 6): (False, False, True, False),
       (4, 1): (False, True, False, False),
       (4, 2): (False, False, False, False),
       (4, 3): (False, True, False, True),
       (4, 4): (True, True, True, False),
       (4, 5): (False, False, False, False),
       (4, 6): (False, False, False, False),
       (5, 1): (True, True, False, True),
       (5, 2): (False, False, True, True),
       (5, 3): (True, True, True, True),
       (5, 4): (True, False, True, True),
       (5, 5): (False, False, True, True),
       (5, 6): (False, True, True, False),
       (6, 1): (True, False, False, False),
       (6, 2): (False, False, False, False),
       (6, 3): (True, False, False, False),
       (6, 4): (False, False, False, False),
       (6, 5): (False, False, False, False),
       (6, 6): (True, False, False, False)}

print("\n=========== PROBLEM 4 TESTS ===========")
maze = Maze(map)
maze.show_status()  # Should be at (1,1)
maze.move_up()  # Error: Can't go that way!
maze.move_left()  # Error: Can't go that way!
maze.move_right()
maze.move_right()  # Error: Can't go that way!
maze.move_down()
maze.move_down()
maze.move_down()
maze.move_right()
maze.move_right()
maze.move_up()
maze.move_right()
maze.move_down()
maze.move_left()
maze.move_down()  # Error: Can't go that way!
maze.move_right()
maze.move_down()
maze.move_down()
maze.move_right()
maze.show_status()  # Should be at (6,6)


#############
# Problem 5 #
#############

import requests

def earthquake_daily_summary():
    """
    This function will read JSON (Javascrip Object Notation) data from the 
    United States Geological Service (USGS) consisting of earthquake data.
    The data will include all earthquakes in the current day.
    
    JSON data is organized into a dictionary.  After reading the data using
    the 'requests' library, this function will print out a list of all
    earthquake locations ('place' attribute) and magnitudes ('mag' attribute).
    Additional information about the format of the JSON data can be found 
    at this website:  

    https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php
        
    To install the requests library, run:
       If using virtual environment: pip install requests
       If using Windows: py -m pip install requests
       If using Mac: pip3 install requests
    """    
    req = requests.get("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson")
    data = req.json() # The .json() function will convert the json data from the server to a dictionary

    # Extract earthquake information and print
    features = data['features']
    for feature in features:
        properties = feature['properties']
        place = properties['place']
        mag = properties['mag']
        print(f"{place} - Mag {mag}")

# Sample Test Cases (may not be comprehensive) 
print("\n=========== PROBLEM 5 TESTS ===========")
earthquake_daily_summary()

# Sample output from the function.  Number of earthquakes, places, and magnitudes will vary.

# 1km NE of Pahala, Hawaii - Mag 2.36
# 58km NW of Kandrian, Papua New Guinea - Mag 4.5
# 16km NNW of Truckee, California - Mag 0.7
# 9km S of Idyllwild, CA - Mag 0.25
# 14km SW of Searles Valley, CA - Mag 0.36
# 4km SW of Volcano, Hawaii - Mag 1.99







