import Playfair.base_playfair


class encryption_playfair(Playfair.base_playfair.base_playfair):
    """
    Carry out the encryption of the cleaned up plaintext using the playfair cipher
    """
    def __init__(self, key, pf_format='5x5'):
        super().__init__(key, pf_format)

    def encryption(self, plaintext):
        # Loop through plaintext and insert an 'x' between any repeating characters
        plaintext_x = ''
        for ind_c, char in enumerate(plaintext[:-1]):
            if char != plaintext[ind_c + 1]:
                plaintext_x += char
            else:
                plaintext_x += char + 'x'
        plaintext_x += plaintext[-1]

        # If the message does not have an even number of characters, add another x
        if plaintext_x.__len__() % 2 == 1:
            plaintext_x += 'x'

        # Creating a string for the cipher text
        cipher_text = ''

        # Loop through the pairs of characters
        for index in range(0, plaintext_x.__len__(), 2):
            # Get the row and columns of each character in the pair
            r1, c1 = self.character_2_locations[plaintext_x[index]]
            r2, c2 = self.character_2_locations[plaintext_x[index + 1]]
            # If the two characters are in the same column, then the new character is shifted down one position
            if c1 == c2:
                r1_new, c1_new = (r1 + 1) % self.pf_side, c1
                r2_new, c2_new = (r2 + 1) % self.pf_side, c2
            # If the characters are in the same row, then the new character is shifted right one position
            elif r1 == r2:
                r1_new, c1_new = r1, (c1 + 1) % self.pf_side
                r2_new, c2_new = r2, (c2 + 1) % self.pf_side
            # Otherwise, replace the characters following the rectangle approach
            else:
                r1_new, c1_new = r1, c2
                r2_new, c2_new = r2, c1
            # Append the new characters to cipher_text
            cipher_text += (self.locations_2_character[(r1_new, c1_new)] + self.locations_2_character[(r2_new, c2_new)])

        return cipher_text


