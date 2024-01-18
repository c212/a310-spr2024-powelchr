# 6 coins

# you roll three dice, what is the chance the sum is not a prime number

import numpy as np 

prime_numbers = [2, 3, 5, 7, 11, 13, 17]
games = 10000 
counter = 0 

for i in range(games):
    game = np.random.choice([1,2,3,4,5,6],3)
    sum_game = sum(game)
    if sum_game not in prime_numbers:
        counter += 1

print(counter/games)

#throw a coin 100 times what is the chance for six (heads or tails) in a row

counter = 0 
exp = 10000

for i in range(exp):
    game = np.random.choice(['0','1'], 100)
    a = ''.join(game)
    #print(a)
    if '0'*6 in a or '1'*6 in a:
        counter +=1 
print(counter/exp)



#solve the lockers problem that is stated here (discussed Wed Jan 10 in class)

# locker 12 
# passed 1 and 12
# passsed 2 and 6 
# passed 3 and 4


# sqaured lockers 81 
# 9 by 9 

class complex:

    def __init__(self, real, imag):
        self.real = real 
        self.imag = imag 

    def __str__(self):
        return str(self.real) + ' + ' + str(self.imag) + ' * i'
    
    def __add__(self, other):
        new_real = self.real + other.real 
        new_imag = self.imag + other.imag
        return complex(new_real, new_imag)

    # (a+bi)(c+di) = (ac-bd) + i(ad+bc)
    def __mul__(self, other):
        new_real = (self.real*other.real) - (self.imag * other.imag)
        new_imag = (self.real*other.imag) + (self.imag * other.real)
        return complex(new_real, new_imag)

a = complex(2,3)
b = complex(1,2)
print(a)
print(b)
c = a+b
print(c)
print(a*b)

class creature:
    def __init__(self, name) -> None:
        self.name = name
        print('Creature created')

    def talk(self):
        return "My name is " + self.name + " and I am a " + type(self).__name__ + self.makeSound()

    def makeSound(self):
        return ". "

class dog(creature):
    def __init_subclass__(cls) -> None:
        return super().__init_subclass__()
    
    def makeSound(self):
        return ", and I say woof. "
    
a = creature('bob')
print(a.talk())

a = dog('daisy')
print(a.talk())