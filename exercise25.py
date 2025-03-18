heroes = [
    ["SUperman", 9000], #0
    ["Saitama",  10000],#1
    ["Deku",  8000],   #2
    ["Ironman",11111],  #3
    ["Gagamboy",3333], #4
    ["Darna",   5555], #5
    
]

for i, hero in enumerate(heroes):
    print(f"{i}: {hero}")
    
for i, hero in enumerate(heroes):
    print(f"{i + 1}: {hero}")
    ####
for i, hero in enumerate(heroes, start=1):
    print(f"{i + 1}: {hero}")