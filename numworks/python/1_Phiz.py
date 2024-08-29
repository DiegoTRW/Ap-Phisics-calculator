import kinematics


def main():
    i = input(
        print(
            int(
                """
    what do you want to calculates
    1) mechanics               
                """
            )
        )
    )
    if i == 1:
        mechanics()


def mechanics():
    a = int(
        input(
            """
1) V_i = V_o + at
2) ΔX_i = V_o*t + 0.5*a*t^2
3) V_i^2 = V_o^2 + 2*a*ΔX_i
"""
        )
    )
    if a == 1:
        kinematics.UI(a).EQ1()


mechanics()
