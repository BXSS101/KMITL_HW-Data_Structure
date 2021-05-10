class MyInt :
    def __init__(self, x) :
        self.x = x
    def __add__(self, g,h) :
        return g + h + ((g+h)//2)
    def toRoman(self) :
        txt = ""
        if self.x // 1000 > 0 :
            for i in range(self.x//1000) :
                txt = txt + 'M'
            self.x = self.x -((self.x//1000)*1000)
            #print(self.x)
        if self.x // 900 == 1 :
            txt = txt + 'CM'
            self.x = self.x - 900
            #print(self.x)
        if self.x // 500 == 1 :
            txt = txt + 'D'
            self.x = self.x - 500
            #print(self.x)
        if self.x // 400 == 1 :
            txt = txt + 'CD'
            self.x = self.x - 400
            #print(self.x)
        if self.x // 100 > 1 :
            for i in range(self.x//100) :
                txt = txt + 'C'
            self.x = self.x -((self.x//100)*100)
            #print(self.x)
        if self.x // 90 == 1 :
            txt = txt + 'XC'
            self.x = self.x - 90
            #print(self.x)
        if self.x // 50 == 1 :
            txt = txt + 'L'
            self.x = self.x - 50
            #print(self.x)
        if self.x // 40 == 1 :
            txt = txt + 'XL'
            self.x = self.x - 40
            #print(self.x)
        if self.x // 10 > 1 :
            for i in range(self.x//10) :
                txt = txt + 'X'
            self.x = self.x -((self.x//10)*10)
            #print(self.x)
        if self.x // 9 == 1 :
            txt = txt + 'IX'
            self.x = self.x - 9
            #print(self.x)
        if self.x // 5 == 1 :
            txt = txt + 'V'
            self.x = self.x - 5
            #print(self.x)
        if self.x // 4 == 1 :
            txt = txt + 'IV'
            self.x = self.x - 4
            #print(self.x)
        if self.x // 1 >= 1 :
            for i in range(self.x//1) :
                txt = txt + 'I'
            self.x = self.x -((self.x//1)*1)
            #print(self.x)
        return txt

    
print(" *** class MyInt ***")
m, n = map(int, input("Enter 2 number : ").split(' '))
a = MyInt(m)
b = MyInt(n)
print(m, "convert to Roman : ",end='')
print(a.toRoman())
print(n, "convert to Roman : ",end='')
print(b.toRoman())
print(m,'+',n,'=',a.__add__(m,n))