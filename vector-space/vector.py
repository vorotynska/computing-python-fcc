#A vector can be defined by two coordinates, x and y, in the Euclidean plane. 
# The distance between the origin of the axes and the point (x, y) will be 
# its length, or norm. And the vector direction will point towards (x, y).

class R2Vector:
    def __init__(self, *, x, y,) :
        self.x = x
        self.y = y
    
    def norm(self):
        return sum(val**2 for val in vars(self).values())**0.5
    
    def __str__(self):
        return str(tuple(getattr(self, i) for i in vars(self)))
    
    def __repr__(self):
        arg_list = [f'{key}={val}' for key,val in vars(self).items()]
        args = ", ".join(arg_list)
        return f'{self.__class__.__name__}({args})'
    
    def __add__(self, other):
        if type(self) != type(other):
            return NotImplemented
        kwargs = {i: getattr(self, i) + getattr(other, i) for i in vars(self)}
        return self.__class__(**kwargs)
    
    def __sub__(self, other):
        if type(self) != type(other):
            return NotImplemented
        kwargs = {i: getattr(self, i) - getattr(other, i) for i in vars(self)}
        return self.__class__(**kwargs)
    
    def __mul__(self, other):
        if type(other) in (int, float):
            kwargs = {i: getattr(self, i) * other for i in vars(self)}
            return self.__class__(**kwargs)
        elif type(self) == type(other):
            args = [getattr(self, i) * getattr(other, i) for i in vars(self)]
            return sum(args)
        return NotImplemented
    
    def __eq__(self, other):
        if type(self) != type(other):
            return NotImplemented
        return all(getattr(self, i) == getattr(other, i) for i in vars(self))
    
    # method is called under the hood when the != operator is used.
    def __ne__(self, other):
        return not self == other
    
    #  method is called under the hood when the < operator is used 
    # to compare an object with something else.
    def __lt__ (self, other):
        if type(self) != type(other):
            return NotImplemented
        return self.norm() < other.norm()
    
    # method is called under the hood when the > operator 
    # is used to compare an object with something else.
    def __gt__(self, other):
        if type(self) != type(other):
            return NotImplemented
        return self.norm() > other.norm()
    
    def __le__(self, other):
        return not self > other
    
    # called when the >= is used to compare two objects.
    def __ge__(self, other):
        return not self < other
   
    
class R3Vector(R2Vector):
    def __init__(self, *, x, y, z):
        super().__init__(x=x, y=y)
        self.z = z

    def cross(self, other):
        if type(self) != type(other):
            return NotImplemented
        kwargs ={
            'x': self.y * other.z - self.z * other.y,
            'y': self.z * other.x - self.x * other.z,
            'z': self.x * other.y - self.y * other.x
        }
        return self.__class__(**kwargs)
    
v1 = R2Vector(x=2, y=3)
v2 = R3Vector(x=2, y=2, z=3)

print(f'v1 = {v1}')
print(f'v2 = {v2}')

v3 = v1 + v2
print(f'v1 + v2 = {v3}')
v4 = v1 - v2
print(f'v1 - v2 = {v4}')
v5 = v1 * 3
print(f'v1 * 3 = {v5}')
print(v1 == R2Vector(x=2, y=3))
v6 = v1.cross(v2)
print(f'v1 x v2 = {v6}')

