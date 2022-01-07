import os

# Directories
root = os.path.expanduser('~') + '/Desktop/Weird Codes/Cryptography/'
test_playfair_direc = root + 'test_cases/Playfair/'


# Test cases
def test_case_playfair(test):
    return test_playfair_direc + 'test_{}.txt'.format(test)

