print("Introduceți numărul de blocuri:")
nr = input()
nr = int(nr)
strat = 1
while nr >= strat:
    nr -= strat
    strat += 1

print("Piramida are", strat-1, "nivele.")
print("Nu au fost folosite", nr, "blocuri.")
