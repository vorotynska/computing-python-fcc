# You are going to build a program that calculates and draws the 
# trajectory of a projectile given the angle, speed and height of the throw.

# Start by importing math, you will use it a lot in this project as it has 
# useful methods like math.radians, math.cos, math.sin and others.

# Also create these variables to have the value of the gravitational 
# acceleration and some special symbols that will be useful later (use copy 
# and paste for these).

import math

GRAVITATIONAL_ACCELERATION = 9.81
PROJECTILE = "∙"
x_axis_tick = "T"
y_axis_tick = "⊣"

class Projectile:
    __slots__ = ('__speed', '__height', '__angle')

    def __init__(self, speed, height, angle):
        self.__speed = speed
        self.__height = height
        self.__angle = angle = math.radians(angle)

    def __str__(self):
        return f'''
Projectile details:
speed: {self.__speed} m/s
height: {self.__height} m
angle: {round(math.degrees(self.__angle))}°
displacement: {round(self.__calculate_displacement(), 1)} m
'''
    
    # A  method that calculates the displacement of the projectile, which is 
    # the horizontal space traveled from the throw to when the projectile touches the ground
    def __calculate_displacement(self):
        horizontal_component = self.__speed * math.cos(self.__angle)
        vertical_component = self.__speed * math.sin(self.__angle)
        squared_component = vertical_component**2
        gh_component = 2 * GRAVITATIONAL_ACCELERATION * self.__height
        sqrt_component = math.sqrt(squared_component + gh_component)
        
        return horizontal_component * (vertical_component + sqrt_component) / GRAVITATIONAL_ACCELERATION
    
    # Calculating the coordinates of the trajectory
    def __calculate_y_coordinate(self, x):
        height_component = self.__height
        angle_component = math.tan(self.__angle) * x
        acceleration_component = GRAVITATIONAL_ACCELERATION * x**2 / (
                2 * self.__speed**2 * math.cos(self.__angle)**2)
        y_coordinate = height_component + angle_component - acceleration_component

        return y_coordinate
    def calculate_all_coordinates(self):
        return [
            (x, self.__calculate_y_coordinate(x))
            for x in range(math.ceil(self.__calculate_displacement()))
        ]
    
    @property
    def height(self):
        return self.__height

    @property
    def angle(self):
        return round(math.degrees(self.__angle))

    @property
    def speed(self):
        return self.__speed

    @height.setter
    def height(self, n):
        self.__height = n

    @angle.setter
    def angle(self, n):
        self.__angle = math.radians(n)

    @speed.setter
    def speed(self, s):
       self.__speed = s

    def __repr__(self):
        return f'{self.__class__}({self.speed}, {self.height}, {self.angle})'
    
class Graph:
    __slots__ = ('__coordinates')

    def __init__(self, coord):
        self.__coordinates = coord

    def __repr__(self):
        return f"Graph({self.__coordinates})"

    def create_coordinates_table(self):
        table = '\n  x      y\n'
        for x, y in self.__coordinates:
            table += f'{x:>3}{y:>7.2f}\n'

        return table
    
    def create_trajectory(self):

        rounded_coords = [(round(x), round(y)) for x, y in self.__coordinates]

        x_max = max(rounded_coords, key=lambda i: i[0])[0]
        y_max = max(rounded_coords, key=lambda j: j[1])[1]

        matrix_list = [[" " for _ in range(x_max + 1)] for _ in range(y_max + 1)]

        for x, y in rounded_coords:
            matrix_list[-1 - y][x] = PROJECTILE

        matrix = ["".join(line) for line in matrix_list]

        matrix_axes = [y_axis_tick + row for row in matrix]
        matrix_axes.append(" " + x_axis_tick * (len(matrix[0])))

        graph = "\n" + "\n".join(matrix_axes) + "\n"

        return graph
    
def projectile_helper(speed, height, angle):
    # Создаём объект Projectile
    ball = Projectile(speed, height, angle)
    
    # Печатаем его характеристики
    print(ball)
    
    # Вычисляем координаты и создаём граф
    coordinates = ball.calculate_all_coordinates()
    graph = Graph(coordinates)
    
    # Печатаем таблицу координат
    print(graph.create_coordinates_table())
    
    # Печатаем траекторию
    print(graph.create_trajectory())

# Вызов функции с примерными значениями
projectile_helper(10, 3, 45)


