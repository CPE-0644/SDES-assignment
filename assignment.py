from sdes import *

sdes = SDES()

# sample use
cipher = sdes.encrypt(key='0010010111', plain='11001101')
plain = sdes.decrypt(key='0010010111', cipher=cipher)
print(cipher, plain)

ciphers =  ['0b11001101','0b11000011','0b10111001','0b11110111','0b1101000','0b10111001','0b11110111','0b111000','0b111000','0b1101000','0b11001101','0b10110110','0b10111001','0b10111001','0b11000011','0b110','0b11000011','0b111000','0b111000','0b10110110','0b1101000','0b110','0b11001101','0b1100011','0b11110111','0b10111001','0b1100011','0b11000011','0b1100011','0b1101000','0b111000','0b10110110','0b10110110','0b1101000','0b111000','0b111000','0b10111001','0b11001101','0b10110110','0b11000011','0b110','0b10111001','0b11001101','0b11110111','0b111000','0b11000011','0b1100011','0b10110110','0b10111001','0b110','0b1101000','0b11001101','0b10110110','0b110','0b1100011','0b11001101','0b11110111','0b110','0b110','0b11110111','0b10110110','0b1010111','0b111000','0b10111001','0b1010111','0b10111001','0b10110110','0b10111001','0b1100011','0b11001101','0b111000','0b11110111','0b10111001','0b110','0b11000011','0b1101000','0b111000', ]
student_number = '590610644'

count_correct_cipher = 0

def fill_character_bit(bit, num):
    if len(num) < bit:
        num = ((bit - len(num)) * '0') + num
    return num

def is_plain_equal_student_number(key, plains):
    return student_number[0] == plains[0] and student_number[1] == plains[1] and student_number[2] == plains[2] and student_number[3] == plains[3] and student_number[4] == plains[4] and student_number[5] == plains[5] and student_number[6] == plains[6] and student_number[7] == plains[7] and student_number[8] == plains[8] 

    
for i in range(1024):
    key = str(bin(i))[2:]
    key = fill_character_bit(10, key)

    # count_correct_cipher = 0
    for j in range(len(student_number)):

        cipher = str(ciphers[0])[2:]
        cipher = fill_character_bit(8, cipher)

        plain = sdes.decrypt(key=key, cipher= cipher)
    
        if str(int(plain,2)) == student_number[j]:
            print('key:', str(key), '->' , str(int(plain,2))  )
            count_correct_cipher+=1

        if(count_correct_cipher == len(student_number)):
            print(key)
    
    # 
    # plains = [
    #     sdes.decrypt(key=key, cipher= fill_character_bit(8, str(ciphers[0])[2:])),
    #     sdes.decrypt(key=key, cipher= fill_character_bit(8, str(ciphers[1])[2:])),
    #     sdes.decrypt(key=key, cipher= fill_character_bit(8, str(ciphers[2])[2:])),
    #     sdes.decrypt(key=key, cipher= fill_character_bit(8, str(ciphers[3])[2:])),
    #     sdes.decrypt(key=key, cipher= fill_character_bit(8, str(ciphers[4])[2:])),
    #     sdes.decrypt(key=key, cipher= fill_character_bit(8, str(ciphers[5])[2:])),
    #     sdes.decrypt(key=key, cipher= fill_character_bit(8, str(ciphers[6])[2:])),
    #     sdes.decrypt(key=key, cipher= fill_character_bit(8, str(ciphers[7])[2:])),
    #     sdes.decrypt(key=key, cipher= fill_character_bit(8, str(ciphers[8])[2:])),
    # ]

    # print(is_plain_equal_student_number(str(int(key,2)), plains))