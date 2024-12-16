import sympy as sym

class Numerical:
    
    def __init__(self):
        pass
    
    def derivative(self, eq, n):
        b = eq
        while n > 0:
            n = n - 1
            b = sym.diff(b)
            #print("b", b)
            #print("n", n)
        return b
    
    def taylor(self, f, n, point=None, approx=None):
        x = sym.Symbol('x')
        a = sym.Symbol('a')
        z = 1
        ans = sym.parse_expr(f)
        while z <= n:
            diff = self.derivative(f, z)
            y = (diff / sym.factorial(z)) * (a - x) ** z
            #print("y", y)
            ans = ans + y
            z = z + 1
        
        return ans.subs(x, point).subs(a, approx).evalf() if approx is not None and point is not None else ans.subs(x, 0)
    '''
    def taylor(self, equation, degree:int, point, approx = None):
        print("Please wait... Computation may take a while...")
        z = 0 # counter
        x = sym.Symbol('x')
        a = sym.Symbol('a')

        f = sym.parse_expr(equation)
        ans = f

        while z <= degree:
            y = (f.diff(x,z) / sym.factorial(z)) * (x - a) ** z
            ans = ans + y
            z = z + 1
        return ans.subs(a, point) if approx != None else ans.subs(x, approx).doit()
    '''
    def error(self, type:int, p, ps):
        p = sym.parse_expr(p).evalf()
        ps = sym.parse_expr(ps).evalf()
        x = sym.Symbol('x')
        if (type == 0):
            return abs(p - ps)
        else:
            return abs(((p - ps) / p) * 100)

    def chop(self, num, n):
        n = int(n)
        integer = int(num * (10**n))/(10**n)
        return float(integer)

    def round(self, num, places:int):
        return round(num, places)
    
def process():
    while True:
        te = input("a.) Error Propagation b.) Taylor's Polynomial: c.) Main Menu ")
        if te.upper() == 'B':
            pu = input("P for Pre-Defined, U for User-Defined: ")
            if pu.upper() == 'U':
                f = input("Function: ")
                n = int(input("Degree: "))
                pt = float(input("f(a): "))
                approx = None
                pnxy = input("Do you have approximate value? (y/n) ")
                if (pnxy == 'y' or pnxy == 'Y'):
                    approx = float(input("Approx: "))
                num = Numerical()
                tayl = num.taylor(f, n, pt) if pnxy not in ['y', 'Y'] else num.taylor(f, n, pt, approx)
                pls = int(input('Places: '))
                print(tayl)
                if (pnxy == 'y' or pnxy == 'Y'):
                    print('Chopped: ', num.chop(tayl, pls))
                    print('Rounded: ', num.round(tayl, pls))
            else:
                x = sym.Symbol('x')
                f = 1 / (1 + x)
                n = int(input("Degree: "))
                pt = float(input("f(a): "))
                approx = None
                pnxy = input("Do you have approximate value? (y/n) ")
                if (pnxy == 'y' or pnxy == 'Y'):
                    approx = float(input("Approx: "))
                num = Numerical()
                tayl = num.taylor(str(f), n, pt) if pnxy not in ['y', 'Y'] else num.taylor(str(f), n, pt, approx)
                pls = int(input('Places: '))
                print(tayl)
                if (pnxy == 'y' or pnxy == 'Y'):
                    print('Chopped:', num.chop(tayl, pls))
                    print('Rounded:', num.round(tayl, pls))
        elif te.upper() == 'B':
            ar = input("a.) Absolute Error b.) Relative Error: ")
            tv = input("p: ")
            av = input("p*: ")
            bb = None
            if ar == 'a' or ar == 'A':
                num = Numerical()
                bb = num.error(0, tv, av)
            else:
                num = Numerical()
                bb = num.error(1, tv, av)
            pls = int(input('Places: '))
            print(bb)
            print("chop: ", num.chop(bb, pls))
            print("round: ", num.round(bb, pls))
        else:
            return

'''
Function: function ofc
Degree: Always given, with to the
f(a): Usually c
Approximate value: Pn(x), the x
Places: Decimal places

p = TV, given
ps = AV, given
'''