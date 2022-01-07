import settings
import numpy as np
import string
from string_cleanup import cleanup


class base_playfair:
    def __init__(self, key, pf_format='5x5'):
        # Load the basic parameters of the playfair key and cipher setup
        self.key = key
        self.pf_format = pf_format
        assert self.pf_format in ['5x5', '6x6'], "Invalid pf_format, please use either '5x5' or '6x6'"

        # Initializing the playfair square
        if self.pf_format == '5x5':
            self.pf_square = np.chararray(shape=(5, 5))
            self.remaining_alpha = string.ascii_lowercase.replace('j', '')
            self.pf_side = 5
        else:
            self.pf_square = np.chararray(shape=(6, 6))
            self.remaining_alpha = string.ascii_lowercase + string.digits
            self.pf_side = 6
        # Creating the playfair square
        self.character_2_locations, self.locations_2_character = self.fill_pf_square()

    def fill_pf_square(self):
        # First, we need to clean up the key, and remove all these characters from self.remaining_alpha
        self.key, self.remaining_alpha = self.clean_key()

        # Next, we need to fill up the playfair square with the characters
        fill_order = self.key + self.remaining_alpha
        for row in range(self.pf_square.shape[0]):
            for column in range(self.pf_square.shape[1]):
                self.pf_square[row, column] = fill_order[0]
                fill_order = fill_order[1:]

        # Saving a tuple of each character's position within the self.pf_square as (row, column)
        character_2_locations, locations_2_character = {}, {}
        for index_char, char in enumerate(self.key + self.remaining_alpha):
            character_2_locations[char] = (index_char // self.pf_side, index_char % self.pf_side)
            locations_2_character[character_2_locations[char]] = char

        return character_2_locations, locations_2_character

    def clean_key(self):
        # First, remove any special characters such as spaces
        self.key = cleanup.remove_specials(self.key)

        # Next, make sure the entire key is lowercase
        self.key = cleanup.make_lowercase(self.key)

        # If self.pf_format == '5x5', replace the 'j' with 'i' and replace any numerals with alphabetical spelling
        if self.pf_format == '5x5':
            self.key = cleanup.format_5x5(self.key)

        # Remove any duplicate characters from the key
        self.key = cleanup.remove_duplicate_character(self.key)

        # Remove any characters that are in the key from self.remaining_alpha
        for char in set(self.key):
            self.remaining_alpha = self.remaining_alpha.replace(char, '')

        return self.key, self.remaining_alpha


