class a:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return self.x + other.x

    def __sub__(self, other):
        return self.x - other.x

    def __mul__(self, other):
        return self.x * other.x

    def __truediv__(self, other):
        return self.x / other.x

    def __str__(self):
        return 'the number inside is : {}'.format(self.x)
    
temp1 = a(10)
temp2 = a(5)
print(temp1 + temp2)  # Output: 15
print(temp1 - temp2)  # Output: 5
print(temp1 * temp2)  # Output: 50
print(temp1 / temp2)  # Output: 2.0
print(temp1)          # Output: the number inside is : 10
print(temp2)          # Output: the number inside is : 5
