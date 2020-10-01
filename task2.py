class Textil:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square_pal(self):
        return self.width / 6.5 + 0.5

    def get_square_kost(self):
        return self.height * 2 + 0.3

    @property
    def get_sq_full(self):
        return str(f'Общая площадь ткани: \n'
                   f' {(self.width / 6.5 + 0.5) + (self.height * 2 + 0.3)}')


class Palto(Textil):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_pal = round(self.width / 6.5 + 0.5)

    def __str__(self):
        return f'Площадь на пальто: {self.square_pal}'


class Kostum(Textil):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_kost = round(self.height * 2 + 0.3)

    def __str__(self):
        return f'Площадь на костюм: {self.square_kost}'

palto = Palto(2, 4)
kostum = Kostum(1, 2)
print(palto)
print(kostum)
print(palto.get_sq_full)
print(kostum.get_sq_full)
print(kostum.get_square_pal())
print(kostum.get_square_kost())
