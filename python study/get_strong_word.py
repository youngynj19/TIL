def get_strong_word(A, B):
    numbers_A = 0
    for char in A:
        numbers_A += ord(char)

    numbers_B = 0
    for char in B:
        numbers_B += ord(char)
    
    if numbers_A > numbers_B:
        return A
    else:
        return B

print(get_strong_word('z', 'a')) # => 'z'
print(get_strong_word('tom', 'john')) # => 'john'