class My_stack:

    def __init__(self, size):
        self.size = size
        self.arr = [None] * size
        self.top = -1

    def is_empty(self):
        if self.top == -1:
            return True
        else:
            return False

    def is_full(self):
        if self.top == self.size - 1:
            return True
        else:
            return False

    def push(self, item):
        if not self.is_full():
            self.top += 1
            self.arr[self.top] = item
        else:
            print("push 불가")

    def pop(self):
        if not self.is_empty():
            temp = self.arr[self.top]
            self.arr[self.top] = None
            self.top -= 1
            return temp
        else:
            # raise IndexError('범위를 벗어남')
            print("pull 불가")
            return None

s1 = My_stack(5)
print(s1.arr)
print(s1.size)
print(s1.top)
print(s1.is_empty(), s1.is_full())

print('='*30)

s1.push(1)
print(s1.arr, s1.top, s1.is_empty(), s1.is_full())
s1.push(5)
print(s1.arr, s1.top, s1.is_empty(), s1.is_full())
s1.push(4)
print(s1.arr, s1.top, s1.is_empty(), s1.is_full())
s1.push(3)
print(s1.arr, s1.top, s1.is_empty(), s1.is_full())
s1.push(2)
print(s1.arr, s1.top, s1.is_empty(), s1.is_full())

print('='*30)

s1.push(6)
print(s1.arr, s1.top, s1.is_empty(), s1.is_full())

print('='*30)

print(s1.pop(), s1.arr, s1.top, s1.is_empty(), s1.is_full())
print(s1.pop(), s1.arr, s1.top, s1.is_empty(), s1.is_full())
print(s1.pop(), s1.arr, s1.top, s1.is_empty(), s1.is_full())
print(s1.pop(), s1.arr, s1.top, s1.is_empty(), s1.is_full())
print(s1.pop(), s1.arr, s1.top, s1.is_empty(), s1.is_full())
print(s1.pop(), s1.arr, s1.top, s1.is_empty(), s1.is_full())