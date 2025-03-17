#list slicing 
heroes = [
    "SUperman", #0
    "Saitama",  #1
    "Deku",     #2
    "Ironman",  #3
    "Gagamboy", #4
    "Darna",    #5
    
]
# print(heroes[2:4])
# print(heroes[2:len(heroes)])
# print(heroes[0:4])
# print(heroes[0:len(heroes):2])


# print(heroes[2:])
# print(heroes[:4])
# print(heroes[::2])
# print(heroes[1::4])




# # print(heroes[:-2])
# print(heroes)
# print(heroes[-2:])



heroes2 = heroes[:]
heroes2 = list(heroes)
heroes2.append("Spiderman")

print(heroes)
print(heroes2)