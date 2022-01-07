import Playfair.base_playfair


class decryption_playfair(Playfair.base_playfair.base_playfair):
    """
    Carry out the decryption of the cleaned up plaintext using the playfair cipher, essentially the reverse of the
    process in src.encryption_playfair
    """
    def __init__(self, key, pf_format='5x5'):
        super().__init__(key, pf_format)

    def decryption(self, ciphertext):
        # Create a string for the deciphered plaintext
        plaintext = ''

        # Loop through the pairs in the ciphertext
        for index in range(0, ciphertext.__len__(), 2):
            # Get the row and columns of each character in the pair
            r1, c1 = self.character_2_locations[ciphertext[index]]
            r2, c2 = self.character_2_locations[ciphertext[index + 1]]
            # If the two characters are in the same column, then the plaintext character is shifted up one position
            if c1 == c2:
                r1_new, c1_new = (r1 - 1) % self.pf_side, c1
                r2_new, c2_new = (r2 - 1) % self.pf_side, c2
            # If the characters are in the same row, then the new character is shifted left one position
            elif r1 == r2:
                r1_new, c1_new = r1, (c1 - 1) % self.pf_side
                r2_new, c2_new = r2, (c2 - 1) % self.pf_side
            # Otherwise, replace the characters following the rectangle approach
            else:
                r1_new, c1_new = r1, c2
                r2_new, c2_new = r2, c1
            # Append the new characters to cipher_text
            plaintext += (self.locations_2_character[(r1_new, c1_new)] + self.locations_2_character[(r2_new, c2_new)])

        # Remove any 'x' character if the characters on either side are identical
        plaintext_x = plaintext[0]
        for ind_c, char in enumerate(plaintext[1:-1]):
            if char == 'x':
                if plaintext[ind_c] != plaintext[ind_c + 2]:
                    plaintext_x += char
            else:
                plaintext_x += char
        plaintext_x += plaintext[-1]

        # Replace any number that is spelled out by the actual numeric character
        for num, alpha in zip(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
                              ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
            plaintext_x = plaintext_x.replace(alpha, num)

        return plaintext_x



