import settings
import string_cleanup as sc
from Playfair import decryption_playfair as d_pf, encryption_playfair as e_pf


def run():
    """
    First, we have the encryption and decryption of messages with the Playfair cipher
    """
    # Load and cleanup the plain text.
    message_file = settings.test_case_playfair(1)
    print(sc.cleanup.load_txt(message_file))
    clean_plain = sc.cleanup().playfair_cleanup(message_file)

    # Set the encryption key
    key = 'Playfair Example'

    # Carry out the encryption of the plain text
    cipher_text = e_pf.encryption_playfair(key=key).encryption(plaintext=clean_plain)
    print(cipher_text)

    # Carry out the decryption of the cipher text
    clean_back = d_pf.decryption_playfair(key=key).decryption(ciphertext=cipher_text)
    print(clean_back)




if __name__ == "__main__":
    run()
