print("Introduceți numărul de blocuri:")
nr = input()
nr = int(nr)
strat = 1
while nr >= strat:
    nr -= strat
    strat += 1
else:
    print("Piramida are", strat-1, "nivele.\nNu au fost folosite", nr, "blocuri.")