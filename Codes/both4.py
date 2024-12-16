import sympy as sym

class NumericalIntegration:
    def __init__(self):
        pass

    def merge_intervals(self, intervals):
        merged = []
        intervals.sort()
        merged.append(intervals[0])
        for interval in intervals[1:]:
            if interval[0] == merged[-1][1]:
                merged[-1] = (merged[-1][0], interval[1])
            else:
                merged.append(interval)
        return merged

    def is_continuous(self, func, a, b, n):
        x = sym.Symbol('x')

        roots = sym.solve(func.as_numer_denom()[1], x)
        print(roots)
        pz = []
        for p in roots:
            try:
                if p >= a and p <= b:
                    pz.append(p)
            except:
                pz.append(p)

        if pz:
            return False, pz
        else:
            return True, []

    def trapezoid(self, f, a, b, n, p=6):
        x = sym.symbols('x')
        h = (b - a) / n
        xvals = [a + i * h for i in range(n + 1)]
        fvals = [f.subs(x, xi) for xi in xvals]
        isum = (h / 2) * (fvals[0] + 2 * sum(fvals[1:-1]) + fvals[-1])
        result = round(float(isum), p)
        return result

    def simpson(self, f, a, b, n, p=6):
        x = sym.symbols('x')
        h = (b - a) / n

        xvals = [a + i * h for i in range(n + 1)]
        fvals = [f.subs(x, xi) for xi in xvals]

        isum = fvals[0] + fvals[-1]

        for i in range(1, n):
            if i % 2 == 0:
                isum += 2 * fvals[i]
            else:
                isum += 4 * fvals[i]

        isum *= h / 3

        result = round(float(isum), p)
        return result

    def calculate(self):
        lp = True
        while lp:

            a = float(input('Lower Bound: '))
            b = float(input('Upper Bound: '))
            n = int(input('Sub-intervals: '))

            if b <= a:
                print("Error", "'b' must be greater than 'a'.")
                return

            num = NumericalIntegration()
            x = sym.symbols('x')

            inp = input('P for Pre-Defined U for User Defined: ')
            if inp.upper() == "U":
                try:
                    user_func = input("Function: ")
                    f = sym.sympify(user_func)
                except:
                    print("Invalid")
            else:
                f = sym.sympify('1 / (1 + x)')

            print(f)
            cont, noncont = num.is_continuous(f, a, b, n)
            if cont == False:
                print("Not Continuous")
                for point in noncont:
                    print(point.evalf())
            else:
                print("Continuous")
                trapezoid = num.trapezoid(f, a, b, n)
                simpson = num.simpson(f, a, b, n)
                print(f"Trapezoid: {trapezoid}\nSimpson: {simpson}")

            abc = input("Continue? Y/N: ")
            if abc.upper() == 'N':
                lp = False