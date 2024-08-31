import math
import polynomial


class EQ1_math:
    def __init__(self, V_f, V_o, a, t):
        self.V_f = V_f
        self.V_o = V_o
        self.a = a
        self.t = t

    def calculate_Vf(V_o, a, t):
        V_f = V_o + a * t
        return V_f

    def calculate_Vo(V_f, a, t):
        V_o = V_f - (a * t)
        return V_o

    def calculate_a(V_f, V_o, t):
        a = (V_f - V_o) / t
        return a

    def calculate_t(V_f, V_o, a):
        t = (V_f - V_o) / a
        return t


class EQ2_math:
    def __init__(self, X_f, X_o, V_o, a, t):
        self.X_f = X_f
        self.X_o = X_o
        self.V_o = V_o
        self.a = a
        self.t = t

    def calculate_Xf(X_o, V_o, a, t):
        X_f = X_o + (V_o * t) + (0.5 * a * (t**2))
        return X_f

    def calculate_Xo(X_f, V_o, a, t):
        X_o = X_f - (V_o * t) - (0.5 * a * (t**2))
        return X_o

    def calculate_Vo(X_f, X_o, a, t):
        V_o = ((X_f - X_o) - (0.5 * a * t**2)) / t
        return V_o

    def calculate_t(X_f, X_o, V_o, a):
        a = 0.5 * a
        b = V_o
        c = X_o - X_f
        return polynomial.roots(a, b, c)

    def calculate_a(X_f, X_o, V_o, t):
        a = (2 * ((X_f - X_o) + (V_o * t))) / (t**2)
        return a


class EQ3_math:
    def __init__(self, V_f, V_o, a, X_o, X_i):
        self.V_f = V_f
        self.V_o = V_o
        self.a = a
        self.X_o = X_o
        self.X_i = X_i

    def calculate_Vf(V_o, a, X_f, X_o):
        V_f = math.sqrt((V_o**2) + (2 * a * (X_f - X_o)))
        return V_f

    def calculate_Vo(V_f, a, X_f, X_o):
        V_o = math.sqrt((V_f**2) - (2 * a * (X_f - X_o)))
        return V_o

    def calculate_a(V_f, V_o, X_f, X_o):
        a = ((V_f**2) - (V_o**2)) / (2 * (X_f - X_o))
        return a

    def calculate_Xo(V_f, V_o, a, X_f):
        X_o = -(((V_f**2) - (V_o**2)) / (2 * a)) + (X_f)
        return X_o

    def calculate_Xf(V_f, V_o, a, X_o):
        X_f = (((V_f**2) - (V_o**2)) / (2 * a)) + (X_o)
        return X_f


class EQ1_IN:
    def __init__(self, inp) -> None:
        self.inp = inp

    def EQ1(self):
        if self.inp == 1:
            print("V_f = V_o + a * t")
            V_f = EQ1_math.calculate_Vf(
                int(input("V_o: ")), int(input("a: ")), int(input("t: "))
            )
            return V_f
        if self.inp == 2:
            print("V_o = V_f - (a * t)")
            V_o = EQ1_math.calculate_Vo(
                int(input("V_f: ")), int(input("a: ")), int(input("t: "))
            )
            return V_o
        if self.inp == 3:
            print("a = (V_f - V_o) / t")
            a = EQ1_math.calculate_a(
                int(input("V_f: ")), int(input("V_o: ")), int(input("t: "))
            )
            return a
        if self.inp == 4:
            print("t = (V_f - V_o) / a")
            t = EQ1_math.calculate_t(
                int(input("V_f: ")), int(input("V_o: ")), int(input("a: "))
            )
            return t
        if 5 == self.inp:
            pass


class EQ2_IN:
    def __init__(self, inp):
        self.inp = inp

    def EQ2(self):
        if self.inp == 1:
            print("X_f = X_o + (V_o * t) + (0.5 * a * t^2)")
            X_f = EQ2_math.calculate_Xf(
                int(input("X_o: ")),
                int(input("V_o: ")),
                int(input("a: ")),
                int(input("t: ")),
            )
            return X_f
        if self.inp == 2:
            print("X_o = X_f - (V_o * t) - (0.5 * a * t^2)")
            X_o = EQ2_math.calculate_Xo(
                int(input("X_f: ")),
                int(input("V_o: ")),
                int(input("a: ")),
                int(input("t: ")),
            )
            return X_o
        if self.inp == 3:
            print("V_o=((X_f - X_o) - (.5*a*t^2))/t")
            V_o = EQ2_math.calculate_Vo(
                int(input("X_f: ")),
                int(input("X_o: ")),
                int(input("a: ")),
                int(input("t: ")),
            )
            return V_o
        if self.inp == 4:
            print("quadratic eq")
            t = EQ2_math.calculate_t(
                int(input("X_f: ")),
                int(input("X_o: ")),
                int(input("V_o")),
                int(input("a: ")),
            )
            return t
        if self.inp == 5:
            print("a = 2((X_f - X_o) - (V_o * t))/t^2")
            a = EQ2_math.calculate_a(
                int(input("X_f: ")),
                int(input("X_o: ")),
                int(input("V_o: ")),
                int(input("t: ")),
            )
            return a
        if self.inp == 6:
            pass


class EQ3_IN:
    def __init__(self, inp):
        self.inp = inp

    def EQ3(self):
        if self.inp == 1:
            print("V_f = sqrt((V_o^2) + (2*a*ΔX))")
            V_f = EQ3_math.calculate_Vf(
                int(input("V_o: ")),
                int(input("a: ")),
                int(input("X_f: ")),
                int(input("X_o: ")),
            )
            return V_f
        if self.inp == 2:
            print("V_o = sqrt((V_f^2) - (2*a*ΔX))")
            V_o = EQ3_math.calculate_Vo(
                int(input("V_f: ")),
                int(input("a: ")),
                int(input("X_f: ")),
                int(input("X_o: ")),
            )
            return V_o
        if self.inp == 3:
            print("a = (V_f^2 - V_o^2)/2ΔX")
            a = EQ3_math.calculate_a(
                int(input("V_f: ")),
                int(input("V_o: ")),
                int(input("X_f: ")),
                int(input("X_o: ")),
            )
            return a
        if self.inp == 4:
            print("X_o = -(((V_f^2) - (V_o^2)) / (2 * a)) + (X_f)")
            X_o = EQ3_math.calculate_Xo(
                int(input("V_f: ")),
                int(input("V_o: ")),
                int(input("a: ")),
                int(input("X_f: ")),
            )
            return X_o
            # V_f, V_o, a, X_f
        if self.inp == 5:
            print("X_f= (((V_f**2) - (V_o**2)) / (2 * a)) + (X_o)")
            X_f = EQ3_math.calculate_Xf(  # V_f, V_o, a, X_o
                int(input("V_f: ")),
                int(input("V_o: ")),
                int(input("a: ")),
                int(input("X_o: ")),
            )
            return X_f
        if self.inp == 6:
            pass
        # if self.inp != 1 or 2 or 3 or 4 or 5 or 6:
        #     print("invalid input")
        #     return EQ3_IN.EQ3


class UI:
    def __init__(self):
        pass

    def EQ1_ui(self):  # this EQ1_ui is for the user interface of the EQ1 class
        inp = int(
            input(
                """
what value do you wanto to calculate
1) V_f
2) V_o
3) a
4) t
5)quit
"""
            )
        )
        return EQ1_IN(inp).EQ1()  # this send the value to eq1_in logic class

    def EQ2_ui(self):  # this EQ2_ui is for the user interface of the EQ2 class
        inp = int(
            input(
                """
what value do you wanto to calculate
1) X_f
2) X_o
3) V_o
4) t
5) a
6) quit
"""
            )
        )
        return EQ2_IN(inp).EQ2()  # this send the value to eq2_in logic class

    def EQ3_ui(self):  # this EQ3_ui is for the user interface of the EQ3 class
        inp = int(
            input(
                """
1)V_i
2)V_o
3)a
4)X_f
5)X_o
5)quit
"""
            )
        )
        return EQ3_IN(inp).EQ3()  # this send the value to eq3_in logic class
