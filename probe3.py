class Buiding:
    total = 0
    def __init__(self):
        for i in range(1, 41):
            Buiding.total = self.total + 1
            print('New building', i)

new_building = Buiding()

print('Number of building ', Buiding.total)