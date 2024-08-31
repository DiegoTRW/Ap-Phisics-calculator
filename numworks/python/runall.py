import phizrun


a = int(
    input(
        """
what are you trying to run
1) Phisics 

"""
    )
)

if a == 1:
    print(phizrun.phys_run.run())
