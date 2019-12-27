# darius R simualtor

# Rlevel = 2
# Hstack = 4
# BonusAD = 150
#
# Rdamage = Rlevel*100 +BonusAD*0.75
# BonusPercentage = Hstack*0.2
#
# TeemoHealth = 700
# TeemoRemainHealth =  TeemoHealth - Rdamage*(1+BonusPercentage)
#
# if (TeemoRemainHealth < 0):
#     print("Mushrooms...")
# else :
#     print("^오^ Never underestimate the power of the scout's code!")
#     print(TeemoRemainHealth)

#tiergenerator
# lp = 1950
# if (lp<=400):
#     print ("Iron")
# if (lp>400 and lp<=600):
#     print ("Bronze")
# if (lp>600 and lp<=800):
#     print ("Silver")
# if (lp>800 and lp<=1000):
#     print ("Gold")
# if (lp>1000 and lp<=1200):
#     print ("Platinum")
# else :
#     print ("Higher than Platinum")

lp = 750
if (lp<=400):
    print ("Iron")
elif (lp<=600):
    print ("Bronze")
elif (lp<=800):
    print ("Silver")
elif (lp<=1000):
    print ("Gold")
elif (lp<=1200):
    print ("Platinum")
else :
    print ("Higher than Platinum")
