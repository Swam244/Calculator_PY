RYDBERG_CONSTANT = 1.09677*10**7
g = 9.8 # in m/s^2
c = 2.99792458 * 10**8 # in m/s
K_IN_AIR = 9*10**9
mass_E = 9.11*10**-31# in kg
mass_P = 1.6726219*10**-27 # in kg 0.000000000000000000016726219 kg
mass_N = 1.675*10**-27 # in kg
h_E = 6.626*10**-34  # in Joules #PLANK's Constant
h_L = 1.616255*10**-35  # in m
h_T = 5.39*10**-44  # in seconds
h_M = 2*10**-11  # in kg 0.00000000002
h_Temp = 1 # KELVIN
# max_TEMP = *10**34 # KELVIN
AVOGADRO_CONSTANT = 6.022*10**23 # atoms/mole
G = 6.673*10**-11 # m^2/kg^2
M_EARTH = 6*10**24
M_SUN = 2*10**30
M_MOON = 7.4*10**22

def GRAVITIONAL_FORCE(m1,m2,r):
    Fg = G*m1*m2/r**2
    return str(Fg)+ 'N'

def RESISTANCE(V,I):
    # ohm's law = V=IR V=Voltage,I=Current,R = Resistance
    Resistance = V/I
    # units
    # R = ohm
    # Current = Ampere (A)
    return str(Resistance)+ 'ohm'

def Voltage(I,R):
    # ohm's law V=IR
    V = I*R
    return str(V)+ 'V'

def Current(V,R):
    I = V/R
    return str(I)+ 'A'
