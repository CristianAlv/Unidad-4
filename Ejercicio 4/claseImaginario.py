class Imaginario:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    # Sobrecarga del operador +
    def __add__(self, other):
        return Imaginario(self.real + other.real, self.imag + other.imag)

    # Sobrecarga del operador -
    def __sub__(self, other):
        return Imaginario(self.real - other.real, self.imag - other.imag)

    # Sobrecarga del operador *
    def __mul__(self, other):
        return Imaginario(self.real * other.real - self.imag * other.imag, self.real * other.imag + self.imag * other.real)

    # Sobrecarga del operador /
    def __truediv__(self, other):
        denom = other.real ** 2 + other.imag ** 2
        return Imaginario((self.real * other.real + self.imag * other.imag) / denom, (self.imag * other.real - self.real * other.imag) / denom)

    def __str__(self):
        if self.imag == 0:
            return f"{self.real}"
        else:
            return f"{self.real} {self.imag}i"