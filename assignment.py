from sdes import *

def attacking_sdes():

    sdes = SDES()

    # sample use
    # cipher = sdes.encrypt(key='1111011010', plain='01001101')
    # plain = sdes.decrypt(key='1111011010', cipher='01101001')
    # print(cipher, plain)

    ciphers =  ['0b11001101','0b11000011','0b10111001','0b11110111','0b1101000','0b10111001','0b11110111','0b111000','0b111000','0b1101000','0b11001101','0b10110110','0b10111001','0b10111001','0b11000011','0b110','0b11000011','0b111000','0b111000','0b10110110','0b1101000','0b110','0b11001101','0b1100011','0b11110111','0b10111001','0b1100011','0b11000011','0b1100011','0b1101000','0b111000','0b10110110','0b10110110','0b1101000','0b111000','0b111000','0b10111001','0b11001101','0b10110110','0b11000011','0b110','0b10111001','0b11001101','0b11110111','0b111000','0b11000011','0b1100011','0b10110110','0b10111001','0b110','0b1101000','0b11001101','0b10110110','0b110','0b1100011','0b11001101','0b11110111','0b110','0b110','0b11110111','0b10110110','0b1010111','0b111000','0b10111001','0b1010111','0b10111001','0b10110110','0b10111001','0b1100011','0b11001101','0b111000','0b11110111','0b10111001','0b110','0b11000011','0b1101000','0b111000', ]
    student_number = '590610644'

    da_key = 0

    print('Cipher text: ')
    for cipher in ciphers:
        print(cipher, end=' ')

    # brute-force key
    for i in range(1024):
        key = str(bin(i))[2:]
        key = key.zfill(10)

        cipher_list = []
        count_correct_cipher = 0

        # generate number(0-9) cipher by that key 
        for num in range(10):

            plain = bin(ord(str(num)))[2:]
            plain = plain.zfill(8)

            cipher = sdes.encrypt(key=key, plain= plain)
            cipher_list.append(cipher)

        # check if those ciphers are related with student_number
        for index,number in enumerate(student_number):
            if(cipher_list[int(number)] == ciphers[index][2:].zfill(8)):
                count_correct_cipher += 1
            else: 
                break
        # all correct -> get key
        if(count_correct_cipher >= 9):
            da_key = str(bin(i))[2:].zfill(10)
            print('\n\nFounded key:', da_key)

    plain_text = []

    # use the key to decrypt the cipher text
    for cipher in ciphers:
        cipher = str(cipher[2:].zfill(8))
        plain = sdes.decrypt(key = da_key, cipher = cipher)
        
        plain = chr(int(plain,2))

        plain_text.append(plain)


    print('\nPlain text:')
    for text in plain_text:
        print(text, end=' ')

if __name__ == '__main__':
    attacking_sdes()