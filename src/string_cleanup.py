
class cleanup:
    """
    This class will be used to clean up any string to a format that we can use with the various ciphers
    """

    def playfair_cleanup(self, file_path, pf_format='5x5'):
        """

        :param file_path: file path of the plain text being enciphered
        :param pf_format: if '5x5', use the standard playfair form where we only consider a 5x5 encryption grid without
                          numerical characters. However, if we have '6x6' we use a larger grid with both 'i' and 'j'
                          characters along with numbers 0 - 9.
        """
        assert pf_format in ['5x5', '6x6'], "Invalid pf_format, please use either '5x5' or '6x6'"
        # Loading the plain text from the txt file
        plain_text = self.load_txt(file_path=file_path)

        # Strip the plain text of any new lines, special characters, and numerical values (depending of pf_format)
        clean_text = self.remove_specials(plain_text=plain_text)

        # Make the plain text completely lowercase
        clean_text = self.make_lowercase(plain_text=clean_text)

        # Remove 'j' characters and replace numerical values if pf_format == '5x5'
        if pf_format == '5x5':
            clean_text = self.format_5x5(plain_text=clean_text)

        return clean_text

    @staticmethod
    def load_txt(file_path):
        assert file_path[-4:] == '.txt', "Please give the file path for a .txt file containing the plain text."
        with open(file_path, 'r') as f:
            return f.read()

    @staticmethod
    def remove_specials(plain_text):
        # Strip any new line characters \n
        plain_text = plain_text.replace('\n', '')
        # Remove any special characters, so any that is not numeric or alphabetical
        plain_text = ''.join(char for char in plain_text if char.isalnum())
        return plain_text

    @staticmethod
    def make_lowercase(plain_text):
        # Make all characters lowercase
        return ''.join(char.lower() for char in plain_text)

    @staticmethod
    def make_uppercase(plain_text):
        # Make all characters lowercase
        return ''.join(char.upper() for char in plain_text)

    @staticmethod
    def format_5x5(plain_text):
        # if pf_format == '5x5', then replace all numerical values with alphabetical spellings, and replace any 'j'
        # character with an 'i' as is generally done in playfair cipher encoding.
        plain_text = plain_text.replace('j', 'i')
        for num, alpha in zip(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
                              ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
            plain_text = plain_text.replace(num, alpha)
        return plain_text

    @staticmethod
    def remove_duplicate_character(plain_text):
        # Remove duplicate characters from a string
        return ''.join(dict.fromkeys(plain_text))


