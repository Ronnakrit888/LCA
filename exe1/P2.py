"""
Given an average power consumption of a machine p (in Watt) and a number of hours operating it,
write a program to compute the energy consumption (in Watt-hour and in Joules).
[Hint: Energy = power * time; Joules = 3600 * Watt-hour.]
"""


p = float(input('Enter power in watt:'))
t = float(input('Enter operating hours:'))

energy_Wh = p * t
energy_J = energy_Wh * 3600

print("Energy = {:,.2f} Wh or {:,.2f} J".format(energy_Wh, energy_J))


