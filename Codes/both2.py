import sympy as sym
import math

# Bisection
class Calculator:
    x = 0
    run = True

    def __init__(self) -> None:
        self.loop()

    def loop(self):
        while self.run:
            print("Select a Calculator")
            inp = input("A for Secant, B for Bisection, C for Main Menu: ")

            if inp.upper() == 'A':
                pu = input('P for Pre-Defined, U for User Defined: ')
                if pu.upper() == 'U':
                    f = input("Enter function: ")
                    x0 = float(input("Enter the first initial guess: "))
                    x1 = float(input("Enter the second initial guess: "))
                    choose = input("E for tolerance only, I for iterations only, B for both: ")
                    if choose == 'e' or choose == 'E':
                        tol = float(input("Enter tolerance:"))
                        self.secant(f, x0, x1, tol, max_iter=1000)
                    if choose == 'i' or choose == 'I':
                        iter = int(input("Enter iterations: "))
                        self.secant(f, x0, x1, tol=None, max_iter=iter)
                    if choose == 'b' or choose == 'B':
                        tol = float(input("Enter tolerance:"))
                        iter = int(input("Enter iterations: "))
                        self.secant(f, x0, x1, tol, max_iter=iter)
                    input('Press ENTER to exit')
                else:
                    f = "1 / (1 + x)"
                    x0 = float(input("Enter the first initial guess: "))
                    x1 = float(input("Enter the second initial guess: "))
                    choose = input("E for tolerance only, I for iterations only, B for both: ")
                    if choose == 'e' or choose == 'E':
                        tol = float(input("Enter tolerance:"))
                        self.secant(f, x0, x1, tol, max_iter=1000)
                    if choose == 'i' or choose == 'I':
                        iter = int(input("Enter iterations: "))
                        self.secant(f, x0, x1, tol=None, max_iter=iter)
                    if choose == 'b' or choose == 'B':
                        tol = float(input("Enter tolerance:"))
                        iter = int(input("Enter iterations: "))
                        self.secant(f, x0, x1, tol, max_iter=iter)
                    input('Press ENTER to exit')

            elif inp.upper() == 'B':
                pu = input('P for Pre-Defined, U for User Defined: ')
                if pu.upper() == 'U':
                    fx = input("Enter function: ")
                    a = float(input("Enter left endpoint [: "))
                    b = float(input("Enter right endpoint ]: "))
                    choice = input("E for tolerance only, I for iterations only, B for both: ")
                    if choice == 'e' or choice == 'E':
                        tol = float(input("Enter tolerance:"))
                        self.bisection(fx, a, b, tol)
                    if choice == 'i' or choice == 'I':
                        iter = int(input("Enter iterations: "))
                        self.bisection(fx, a, b, iterations=iter)
                    if choice == 'b' or choice == 'B':
                        tol = float(input("Enter tolerance:"))
                        iter = int(input("Enter iterations: "))
                        self.bisection(fx, a, b, tol, iterations=iter)
                else:
                    fx = '1 / (1 + x)'
                    a = float(input("Enter left endpoint [: "))
                    b = float(input("Enter right endpoint ]: "))
                    choice = input("E for tolerance only, I for iterations only, B for both: ")
                    if choice == 'e' or choice == 'E':
                        tol = float(input("Enter tolerance:"))
                        self.bisection(fx, a, b, tol)
                    if choice == 'i' or choice == 'I':
                        iter = int(input("Enter iterations: "))
                        self.bisection(fx, a, b, iterations=iter)
                    if choice == 'b' or choice == 'B':
                        tol = float(input("Enter tolerance:"))
                        iter = int(input("Enter iterations: "))
                        self.bisection(fx, a, b, tol, iterations=iter)
            else:
                return

    def secant(self, function, x0, x1, tol=None, max_iter=None):
        x = sym.Symbol('x')
        function = sym.parse_expr(function)
        fx0 = function.evalf().subs(x, x0)
        fx1 = function.evalf().subs(x, x1)
        abso = abs(fx1)
        n_iter = 0

        while True:
            y = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
            x0 = x1
            x1 = y
            fx0 = fx1
            fx1 = function.evalf().subs(x, x1)
            n_iter += 1
            abso = abs(fx1)

            if tol is not None and max_iter is not None:
                error = abs(x1 - x0)
                if abso < tol or n_iter >= max_iter:
                    break
            elif tol is not None:
                if abso < tol:
                    break
            elif max_iter is not None:
                if n_iter >= max_iter:
                    error = abs(x1 - x0)
                    break

        if n_iter == 0 and abs(fx1) > tol:
            print("Error: the initial guesses did not produce a valid result.")
        else:
            if tol is not None and max_iter is not None:
                print("\nx0:{a} \nx1:{b} \nfx0:{c} \nfx1:{d} \nIter:{e} \nError:{error} \nabso:{abso}".format(a=x0, b=x1,
                                                                                                            c=fx0, d=fx1,
                                                                                                            e=n_iter,
                                                                                                            error=error,
                                                                                                            abso=abso))
            elif tol is not None:
                print("\nx0:{a} \nx1:{b} \nfx0:{c} \nfx1:{d} \nIter:{e} \nabso:{abso}".format(a=x0, b=x1, c=fx0, d=fx1,
                                                                                              e=n_iter, abso=abso))
            elif max_iter is not None:
                print("\nx0:{a} \nx1:{b} \nfx0:{c} \nfx1:{d} \nIter:{e} \nError:{error}".format(a=x0, b=x1, c=fx0, d=fx1,
                                                                                               e=n_iter, error=error))

    def bisection(self, fx, a, b, e=None, iterations=None):
        self.x += 1
        f = sym.parse_expr(fx)
        x = sym.Symbol('x')
        n_iter = 0
        abso = abs(b - a)

        while True:
            c = (a + b) / 2
            fc = f.subs(x, c)

            if e is None and iterations is not None:
                e = abso * 0.5 ** n_iter

            if e is not None and abso < e and iterations is None:
                break

            if iterations is not None and n_iter == iterations:
                break

            if fc == 0:
                print(c)
                return
            else:
                fa = f.subs(x, a)
                fb = f.subs(x, b)
                if fc * fa < 0:
                    b = c
                else:
                    a = c

            n_iter += 1
            abso = abs(b - a)
            print("\na:{a} \nb:{b} \nc:{c} \niter:{n_iter} \nabso:{abso} \ne:{e} \nfc:{fc}".format(a=a, b=b, c=c, n_iter=n_iter,
                                                                                                  abso=abso, e=e, fc=fc))

            if iterations is not None and n_iter >= iterations:
                print(f"Midpoint: {c} in {n_iter} iterations")
                break