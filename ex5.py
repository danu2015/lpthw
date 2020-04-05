name = "Zed A. Shaw"
age = 35 # not a lie
height = 74 # inches
height_cm = height * 2.54
weight_lbs = 180 # lbs
weight = 180
weight_kgs = weight * 0.4535
eyes = "Blue"
teeth = "White"
hair = "Brown"

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {height_cm} cm tall.")
print(f"He's {weight} lbs heavy.")
print(f"He's {weight_kgs} kgs heavy.")
print(f"Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

#this line is tricky, ty to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, {weight} I get {total}.")
