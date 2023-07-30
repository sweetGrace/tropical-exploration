import math
class Num():



    # Init
    def __init__(self, val) -> None:
        self.val = val
    
    # Elements
    zero_elem = None
    def Zero(): # unit element for adding
        if not hasattr(Num, 'Zero_elem'):
            Num.zero_elem = Num(0)
        return Num.zero_elem
    # Relations
    def __lt__(self, other):
        if isinstance(other, Num):
            if other is Num.Zero():
                return False
            elif self is Num.Zero():
                return True
            else:
                return self.val < other.val
        return self.val < other

    def __gt__(self, other):
        if isinstance(other, Num):
            if other is Num.Zero():
                return True
            elif self is Num.Zero():
                return False
            else:
                return self.val > other.val
        return self.val > other

    def __le__(self, other):
        return self < other or self == other

    def __ge__(self, other):
        return self > other or self == other

    def __eq__(self, other):
        if isinstance(other, Num):
            if other is Num.Zero() or self is Num.Zero():
                return self is other
            else:
                return self.val == other.val
        return self.val == other
    
    def __ne__(self, other):
        if isinstance(other, Num):
            return self.val != other.val
        return self.val != other
    
    # Unary operators
    def __neg__(self):
        return Num(-self.val)
    
    def __pos__(self):
        return Num(+self.val)

    def __invert__(self):
        return Num(~self.val)
    
    def __bool__(self):
        return self.val == 0

    def __abs__(self):
        return Num(abs(self.val))

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return str(self.val)

    def __float__(self):
        return float(self.val)

    
    # Binary operators
    def __add__(self, other):
        if isinstance(other, Num):
            return Num(min(self.val, other.val))
        return Num(min(self.val, other))

    def __radd__(self, other):
        if isinstance(other, Num):
            return Num(min(self.val, other.val))
        return Num(min(self.val, other))

    def __sub__(self, other):
        if isinstance(other, Num):
            return Num(max(self.val, other.val))
        return Num(max(self.val, other))
    
    def __rsub__(self, other):
        if isinstance(other, Num):
            return Num(max(self.val, other.val))
        return Num(max(self.val, other))


    def __mul__(self, other):
        if isinstance(other, Num):
            return Num(self.val + other.val)
        return Num(self.val + other)

    def __rmul__(self, other):
        if isinstance(other, Num):
            return Num(self.val + other.val)
        return Num(self.val + other)

    def __pow__(self, other):
        if isinstance(other, Num):
            return Num(self.val * other.val)
        return Num(self.val * other)

    def __truediv__(self, other):
        if isinstance(other, Num):
            return Num(self.val - other.val)
        return Num(self.val - other)

    def __floordiv__(self, other):
        if isinstance(other, Num):
            return Num(math.floor(self.val - other.val))
        return Num(math.floor(self.val - other))
    
    # Special
    def realdivideby(self, other):
        if isinstance(other, Num):
            return Num(self.val / other.val)
        return Num(self.val / other)
    
    def realdivisor(self, other):
        if isinstance(other, Num):
            return Num(other.val / self.val)
        return Num(other / self.val)
 
    # Other
    def __hash__(self):
        return hash(self.val)


