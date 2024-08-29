# from .constants import pi
import math


class EQ1:
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


class EQ2:
    def __init__(self, X_f, X_o, V_o, a, t):
        self.X_f = X_f
        self.X_o = X_o
        self.V_o = V_o
        self.a = a
        self.t = t

    def calculate_Xf(self, X_o, V_o, a, t):
        self.X_f = X_o + (V_o * t) + (0.5 * a * (t**2))
        return self.X_f

    def calculate_Xo(self, X_f, V_o, a, t):
        self.X_o = X_f - (V_o * t) - (0.5 * a * (t**2))
        return self.X_o

    def calculate_Vo(self, X_f, X_o, a, t):
        self.V_o = ((X_f - X_o) - (0.5 * a * t**2)) / t
        return self.V_o

    def calculate_t(self, X_f, X_o, V_o, a):
        a = 0.5 * a
        b = V_o
        c = X_o - X_f
        dis = b * b - 4 * a * c
        sqrt_val = math.sqrt(abs(dis))

        # checking condition for discriminant
        if dis > 0:
            t1 = (-b + sqrt_val) / (2 * a)
            t2 = (-b - sqrt_val) / (2 * a)
            return t1, t2

        elif dis == 0:
            t = -b / (2 * a)
            return t

        # when discriminant is less than 0
        elif dis < 0:
            # print("""'
            aws1 = print(-b / (2 * a), "+i", sqrt_val / (2 * a))
            aws2 = print(-b / (2 * a), "-i", sqrt_val / (2 * a))
            return aws1, aws2
        if a == 0:
            aws1 = print("Input correct quadratic equation")
            return aws1

    def calculate_a(self, X_f, X_o, V_o, t):
        self.a = (2 * ((X_f - X_o) + (V_o * t))) / (t**2)
        return self.a


class EQ1_IN:
    def __init__(self, inp) -> None:
        self.inp = inp

    def EQ1(self):
        if self.inp == 1:
            V_f = EQ1.calculate_Vf(
                int(input("V_o: ")), int(input("a: ")), int(input("t: "))
            )
            return V_f
        if self.inp == 2:
            V_o = EQ1.calculate_Vo(
                int(input("V_f: ")), int(input("a: ")), int(input("t: "))
            )
            return V_o
        if self.inp == 3:
            V_f = EQ1.calculate_a(
                int(input("V_f: ")), int(input("V_o: ")), int(input("t: "))
            )
            return V_f
        if self.inp == 4:
            t = EQ1.calculate_t(
                int(input("V_f: ")), int(input("V_o: ")), int(input("a: "))
            )
            return t


class UI:
    def __init__(self, inp):
        self.inp = inp

    def EQ1(self):
        self.inp = int(
            input(
                """
what value do you wanto to calculate
1) V_f
2) V_o
3) a
4) t
"""
            )
        )
        return EQ1_IN(self.inp).EQ1()


print(UI(1).EQ1())
