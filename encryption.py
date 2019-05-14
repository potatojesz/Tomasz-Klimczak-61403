ENCRYPT_CIPHER = {'a': 'y', 'A': 'Y',
                  'e': 'i', 'E': 'I',
                  'i': 'o', 'I': 'O',
                  'o': 'a', 'O': 'A',
                  'y': 'e', 'Y': 'E'}
DECRYPT_CIPHER = {'y': 'a', 'Y': 'A',
                  'i': 'e', 'I': 'E',
                  'o': 'i', 'O': 'I',
                  'a': 'o', 'A': 'O',
                  'e': 'y', 'E': 'Y'}


def encrypt(text):
    return run(text, ENCRYPT_CIPHER)


def decrypt(text):
    return run(text, DECRYPT_CIPHER)


def run(text, dictionary):
    result = ''
    for char in text:
        if char in dictionary:
            result += dictionary[char]
        else:
            result += char
    return result
