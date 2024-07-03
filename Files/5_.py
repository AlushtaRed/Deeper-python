from random import randbytes, sample, randint

def create_file(extention, min_len=6, max_len=30, min_bytes=256, max_bytes=4096, count=5):
    for i in range(count):
        name = ''
        vowel = 'qeyuioa'
        consonant = 'wrtpsdfghjklzxcvbnm'
        for i in range(randint(min_len,max_len)):
            if i%2 != 0 and i > 0:
                name += vowel[randint(0,len(vowel)-1)]
            else:
                name += consonant[randint(0,len(vowel)-1)]
        with open(f'{name}.{extention}', 'wb') as f:
            f.write(randbytes(randint(min_bytes,max_bytes)))

def extentions_and (ext_num):
    for i in ext_num:
        create_file(extention=i[0], count=i[1])


extentions_and([('txt', 3),['py',4]])
