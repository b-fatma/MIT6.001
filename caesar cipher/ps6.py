import string


def load_words(file_name):
    '''
    Returns: a list of valid words(lowercase).
    '''
    print('Loading word list from file...')
    # inFile: file
    in_file = open(file_name, 'r')
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
    print('  ', len(word_list), 'words loaded.')
    in_file.close()
    return word_list


def is_word(word_list, word):
    '''
    Returns: True if word is in word_list, False otherwise
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


def get_story_string():
    """
    Returns: a joke in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story


WORDLIST_FILENAME = 'words.txt'


class Message(object):
    def __init__(self, text):
        '''
        Initializes a Message object
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    def get_message_text(self):
        return self.message_text

    def get_valid_words(self):
        return self.valid_words[:]
        
    def build_shift_dict(self, shift):
        '''
        0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (encrypted).
        '''
        cipher = dict()
        for letter in string.ascii_lowercase:
            cipher[letter] = chr(((ord(letter) - 97 + shift) % 26) + 97)
        for letter in string.ascii_uppercase:
            cipher[letter] = chr(((ord(letter) - 65 + shift) % 26) + 65)
        return cipher

    def apply_shift(self, shift):
        '''
        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        ls = []
        for letter in self.message_text:
            if letter in string.ascii_letters:
                ls.append(self.build_shift_dict(shift)[letter])
            else:
                ls.append(letter)
        return ''.join(ls)


class PlaintextMessage(Message):
    def __init__(self, text, shift):
        Message.__init__(self, text)
        self.shift = shift
        self.encrypting_dict = Message.build_shift_dict(self, self.shift)
        self.message_text_encrypted = Message.apply_shift(self, self.shift)


    def get_shift(self):
        return self.shift

    def get_encrypting_dict(self):
        self.encrypting_dict = Message.build_shift_dict(self, self.shift)
        self.message_text_encrypted = Message.apply_shift(self, self.shift)
        '''
        Returns: a COPY of self.encrypting_dict
        '''
        return self.encrypting_dict.copy()

    def get_message_text_encrypted(self):
        return self.message_text_encrypted


    def change_shift(self, shift):
        '''
        Changes self.shift
        '''
        self.shift = shift


class CiphertextMessage(Message):
    def __init__(self, text):
        Message.__init__(self, text)

    def decrypt_message(self):
        '''
        Note: if multiple shifts are  equally good such that they all create 
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        max_number_of_words = 0
        shift = 0
        for i in range(1, 27):
            words = 0
            for word in self.apply_shift(26 - i).split():
                if is_word(self.valid_words, word):
                    words += 1
            if words > max_number_of_words:
                decrypted_message = self.apply_shift(26 - i)
                shift = 26 - i
                max_number_of_words = words
        return (shift, decrypted_message)


def decrypt_story():
    text = CiphertextMessage(get_story_string())
    return text.decrypt_message()


plaintext = PlaintextMessage('hello', 2)
print('Expected Output: jgnnq')
print('Actual Output:', plaintext.get_message_text_encrypted())

ciphertext = CiphertextMessage('jgnnq')
print('Expected Output:', (24, 'hello'))
print('Actual Output:', ciphertext.decrypt_message())






