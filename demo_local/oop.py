# Euclid's algorithm 

def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n




class Fraction:

    def __init__(self,top,bottom):

        self.num = top
        self.den = bottom
    
    

    def __add__(self,otherfraction):
        newnum = self.num*otherfraction.den + self.den*otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum,newden)
        return Fraction(newnum//common,newden//common)
  

    def __mul__(self, otherfraction):
        newnum  = self.num*otherfraction.den 
        newden = self.den * otherfraction.den

        return Fraction(newnum, newden)

    def subtract():
        pass

    def divide():
        pass 

    def show(self):
        print(self.num ,'/' , self.den)

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum == secondnum

    def __str__(self) -> str:
        return str(self.num)+'/'+ str(self.den)

class complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    def __str__(self):
        return str(self.real) + " + i * " + str(self.imag)
    
    def __add__(self, other):
        return complex(self.real + other.real, self.imag + other.imag)
    
    def __mul__(self, other):
        new_real = self.real*other.real - self.imag*other.imag
        new_imag = self.real*other.imag + self.imag*other.real
        return complex(new_real, new_imag)



 

class Creature:
    
    def __init__(self,name) -> None:
        self.name = name 
        print("Creature " + self.name + " created. ")

    def speak(self):
        return 'My name is ' + self.name + ' and I am ' + type(self).__name__ + self.makeSound()
    
    def makeSound(self):
        return ". "

class dog(Creature):
    def __init_subclass__(cls) -> None:
        return super().__init_subclass__()
    
    def makeSound(self):
        return " and I say woof!"

class cow:
    pass 


a = Creature('bob')
print(a.speak())


b = dog('Daisy')
print(b.speak())
# myfraction = Fraction(3,5)
# print(myfraction)
# myfraction.show()

# print(gcd(20,10))


# f1=Fraction(1,4)
# f2=Fraction(1,2)
# f3=f1+f2
# print(f3)


# x = Fraction(1,2)
# y = Fraction(2,3)
# print(x+y)
# print(x == y)


# x = Fraction(1,2)
# y = Fraction(2,3)
# print(x*y)


# x = complex(1,2)
# y = complex(2,3)
# print(x)
# print(y)
# print(x+y)
# print(x*y)

