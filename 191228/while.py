# Final fight and you are main dealer

kill = 0
voice = ["Slayed an enemy", "Double Kill", "Triple Kill", "Quadra Kill", "Penta Kill"]

while (kill<5): # using <= instead of < makes error
    kill = kill + 1
    print( voice[kill-1] )

print("Enemy has surrendered. Victory!")


kill = 0

for JeffKills in voice :
    print(JeffKills)

print("Enemy has surrendered. Victory!")
