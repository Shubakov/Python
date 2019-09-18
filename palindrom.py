word_separators = ["!", "@", "#" "$", "^", "&", "*", "(", ")", "/", "?", ".", ">", ",", "<", ";", ":", "'", '"', "+", " ", "    "]
def is_palindrom(number):
    for separator in word_separators:
        number = "".join(number.split(separator))
    return number == number[-1::-1]
print(is_palindrom('ффф1z   .,/;:!@#$  2     3 2......      ,,/***+z1ффф'))

