#data type: set
dc = ["batman", "superman", "wonder woman", "aquaman", "cyborg"]
marvel = ["iron man", "captain america", "black panther", "black widow", "thor"]    
dc = set(dc)
marvel = set(marvel)    
print(dc)
print(marvel)

print("=======")
print(dc.union(marvel))
print(dc.intersection(marvel))
print(dc.difference(marvel))
print(marvel.difference(dc))
print(dc.symmetric_difference(marvel))



print(dc | marvel)
print(dc & marvel)
print(dc - marvel)
print(marvel - dc)
print(dc ^ marvel)


print("=======")


heroes = dc | marvel
for hero in heroes:
    print(hero)

print("=======")

# print(heroes[1])

print(list(heroes)[1])
print(len(heroes))

print("batman" in heroes)
print("thanos" not in heroes)