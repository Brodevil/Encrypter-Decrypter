def encrypt(string, dictionary):
    return '.'.join([dictionary.get(each, each) for each in string])


def decrypt(string, dictionary):
    dictionary = {dictionary[key]: key for key in dictionary}
    decoded = [dictionary.get(each, each) for each in string.split('.')]
    return ''.join(decoded)


if __name__ == '__main__':
    encrypt_data = {"A": '8', "B": '9', "C": '35', "D": '99', "E": '56', "F": '44', "G": '56', "H": '67', "I": '0',
                    "J": '4', "K": '98',
                    "L": '90', "M": '2', "N": '66', "O": '93', 'P': '55', 'Q': '88', 'R': '34', 'S': '98', 'T': '44',
                    'U': '35', 'V': '22', 'W': '78',
                    'X': '46', 'Y': '3', 'Z': '1',
                    'a': '64', 'b': '81', 'c': '1225', 'd': '9801', 'e': '3136', 'f': '1936', 'g': '3136', 'h': '4489',
                    'i': '10',
                    'j': '16', 'k': '9604', 'l': '8100', 'm': '4', 'n': '4356', 'o': '8649', 'p': '3025', 'q': '7744',
                    'r': '1156', 's': '4483',
                    't': '1936', 'u': '1224', 'v': '484', 'w': '6084', 'x': '2116', 'y': '9', 'z': '2',
                    '1': "223", '2': "354", '3': "445", '4': "234", '5': "890", '6': "089", '7': "349", '8': "867",
                    '9': "650", '0': "940",
                    " ": "547", ",": "865", ";": "149", "@": "887", "!": "809", "#": "768", "&": "795", "(": "678",
                    ")": "679", "-": "760", "_": "764"}

    while True:
        try:
            work = int(input("Enter 0 to Encrypt or Enter 1 to Decrypt :\t"))
            if work == 0:
                print("Your Encrypted Data is :\t", encrypt(input("Enter data to Encrypt :\t"), encrypt_data))
            if work == 1:
                print("Your Decrypted Code is :\t",
                      decrypt(input("Enter the Encrypted Data to Decrypt it\t"), encrypt_data))
        except:
            print("Enter the legal input")
