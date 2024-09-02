import kinematics


class PhysRun:
    def __init__(self):
        pass

    def run():
        en = int(
            input(
                """
what are calculating
1) Kinematics
9) end
"""
            )
        )

        if en == 1:
            return PhysRun.Kin_UI()

        if en == 9:
            return "Program ended"

    def Kin_UI():
        ent = int(
            input(
                """
Which equation are you using?
1) V_i = V_o + at
2) ΔX = V_o*t + 0.5*a*t^2
3) V_f^2 = V_o^2 + 2*a*ΔX
4) back
"""
            )
        )
        if ent == 1:
            print(kinematics.UI().EQ1_ui())
        if ent == 2:
            print(kinematics.UI().EQ2_ui())
        if ent == 3:
            print(kinematics.UI().EQ3_ui())
        if ent == 4:
            PhysRun.run()


# print(PhysRun.run())
