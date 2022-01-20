def get_secret_number(A):
    numbers = 0
    for char in A:
        numbers += ord(char)
    return numbers
get_secret_number('tom') # => 336