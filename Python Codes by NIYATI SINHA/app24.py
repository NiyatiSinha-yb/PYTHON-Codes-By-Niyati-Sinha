#weight converter
weight=int(input("Weight: "))
unit=input("(L)bs or (K)bs:")
if unit.upper()=='K':
    print(f"You are {weight/.45} Pound")
elif unit.upper()=="L":
    print(f" You are {weight*.45} Kgs")
else:
    print("wring input")