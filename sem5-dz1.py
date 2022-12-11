# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

abv = 'Напишите абв напиабв програбвмму программу, удаляющую из \
    этого абв текста все вабвс слова, содерабващие содержащие "абв"'

def del_some_words(abv):
    abv = list(filter(lambda x: 'абв' not in x, abv.split()))
    return " ".join(abv)

abv = del_some_words(abv)
print(abv)