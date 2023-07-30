
'''

ex:
[in1]:
import GaloisField as gf
import Tropical as tro
gf8 = 8
[in2]:
x = tro.Num(gf.Num(14, gf8))
print(x)
[out1]:
6
[in3]:
a = gf.Num(4, gf8)
b = gf.Num(5, gf8)
print(a*b)
c = tro.Num(a)
d = tro.Num(b)
print(c+d)
[out2]:
0 4
'''    
class Num():

    card = 0

    def set_card(card):
        Num.card = card
        return Num.card
    def Card():
        return Num.card
    
    def __init__(self, val):
        self.val = val % Num.card

    # Relations
    def __lt__(self, other):
        if isinstance(other, Num):
            return self.val < other.val
        return self.val < other % Num.card

    def __gt__(self, other):
        if isinstance(other, Num):
            return self.val > other.val
        return self.val > other % Num.card

    def __le__(self, other):
        if isinstance(other, Num):
            return self.val <= other.val
        return self.val <= (other % Num.card)

    def __ge__(self, other):
        if isinstance(other, Num):
            return self.val >= other.val
        return self.val >= (other % Num.card)

    def __eq__(self, other):
        if isinstance(other, Num):
            return self.val == other.val
        return self.val == (other % Num.card)
    
    def __ne__(self, other):
        if isinstance(other, Num):
            return self.val != other.val
        return self.val != (other % Num.card)
    
    # Unary operators
    def __neg__(self):
        return Num(-self.val, Num.card)
    
    def __pos__(self):
        return Num(+self.val, Num.card)

    def __invert__(self):
        return Num(~self.val % Num.card)
    
    def __bool__(self):
        return self.val == 0

    def __abs__(self):
        return Num(abs(self.val % Num.card))

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return str(self.val) + ".GF_" + str(Num.card)

    def __float__(self):
        return float(self.val)

    

    # Binary operators
    def __add__(self, other):
        if isinstance(other, Num) :
            return Num((self.val + other.val) % Num.card)
        return Num((self.val + other % Num.card) % Num.card)  

    def __radd__(self, other):
        if isinstance(other, Num) :
            return Num((self.val + other.val) % Num.card)
        return Num((self.val + other % Num.card) % Num.card) 
    
    def __sub__(self, other):
        if isinstance(other, Num) :
            return Num((self.val - other.val) % Num.card)
        return Num((self.val - other % Num.card) % Num.card)  

    def __rsub__(self, other):
        if isinstance(other, Num) :
            return Num((self.val - other.val) % Num.card)
        return Num((self.val - other % Num.card) % Num.card) 

    def __mul__(self, other):
        if isinstance(other, Num) :
            return Num((self.val * other.val) % Num.card)
        return Num((self.val * (other % Num.card)) % Num.card) 

    def __rmul__(self, other):
        if isinstance(other, Num) :
            return Num((self.val * other.val) % Num.card)

        return Num((self.val * (other % Num.card)) % Num.card) 

    def __pow__(self, other):
        if isinstance(other, Num) :
            return Num(pow(self.val, other.val, Num.card), Num.card)
        return Num((pow(self.val, other, Num.card), Num.card))
                   
    def __mod__(self, other):
        if isinstance(other, Num):
            return self.val % other.val % Num.card
        return self.val % other % Num.card
    def __truediv__(self, other):
        if isinstance(other, Num) :
            return Num((self.val / other.val) % Num.card)
        return Num((self.val / (other % Num.card)) % Num.card) 

    def __floordiv__(self, other):
        if isinstance(other, Num) :
            return Num((self.val // other.val) % Num.card) 
        return Num((self.val // (other % Num.card)) % Num.card) 
	
	# Other
    def __hash__(self):
        return hash((self.val))
    