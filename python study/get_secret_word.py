#print(ord('A'), chr(83))

def get_secret_word(A):
    char = ''
    for i in A:
        char += chr(i)
    return char

get_secret_word([83, 115, 65, 102, 89]) # => 'SsAfy'