#unpacking


heroes = [
    ["SUperman", 9000], #0
    ["Saitama",  10000],#1
    ["Deku",  8000],   #2
    ["Ironman",11111],  #3
    ["Gagamboy",3333], #4
    ["Darna",   5555], #5
    
]
template = "{} has a power of  {}"

for hero in heroes:
    name, power = hero
   
    print(template.format(name, power))
    
    
##### short hand
for name, power in heroes:
    print(template.format(name, power))
