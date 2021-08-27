class Fraction:
    def __init__(self , n , d):
        self.numer = n
        self.deno = d
    
    def sum(self , guest):
        result = Fraction(None , None)
        result.numer = self.numer * guest.deno + self.deno * guest.numer
        result.deno = self.deno * guest.deno
        return result
     
    def sub(self , guest):
        result = Fraction(None , None)
        result.numer = self.numer * guest.deno - self.deno * guest.numer
        result.deno = self.deno * guest.deno
        return result

    def mul(self , guest):
        result = Fraction(None , None)
        result.numer = self.numer * guest.numer
        result.deno = self.deno * guest.deno
        return result

    def divide(self , guest):
        result = Fraction(None , None)
        result.numer = self.numer * guest.deno
        result.deno = self.deno * guest.numer
        return result

    def show_ans(self):
        print(self.numer , '/' , self.deno)

numer1 = int(input('Please enter numerator1: '))
deno1 = int(input('Please enter Denominator1: '))
Fraction1 = Fraction(numer1 , deno1)

numer2 = int(input('Pleaseenter numerator2: '))
deno2 = int(input('Please enter Denominator2: '))
Fraction2 = Fraction(numer2 , deno2)

while True:
    print('1- sum of fractions ')
    print('2- subtract of fractions ')
    print('3- multiply of fractions ')
    print('4- divide of fractions ')
    print('5- exit ')
    n = int(input('Choose which one: '))
    if n == 1:
        ans = Fraction1.sum(Fraction2)
        ans.show_ans()
    elif n == 2:
        ans = Fraction1.sub(Fraction2)
        ans.show_ans()
    elif n == 3:
        ans = Fraction1.mul(Fraction2)
        ans.show_ans()
    elif n == 4:
        ans = Fraction1.divide(Fraction2)
        ans.show_ans()
    elif n == 5:
        exit()
    else:
        print('Wrong choice! Try again.')