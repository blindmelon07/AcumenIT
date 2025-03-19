def greet(day="morning", vibe="good", excited="true"):
    output = f"{vibe.title()} {day.title()}"
    if excited == "true":
        output  = f"Good {day}, {vibe} vibes!"
    else:
        output = f"Good {day}, {vibe} vibes."
    return output

print(greet())
print(greet(day="evening", excited="false"))
print(greet( excited="false",vibe="great"))

#keyword parameters
params = {
    "day": "evening",
    "vibe": "great",
    "excited": "false"
}
#add 2 "**" to unpack the dictionary
print(greet(**params))