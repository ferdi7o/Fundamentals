elements = {"shards": 0 , "fragments": 0, "motes": 0}
legendary_item = ""
legendary_items = {"shards": "Shadowmourne",
                   "fragments": "Valanyr",
                   "motes": "Dragonwrath"}
while not legendary_item:
    materials = input().lower().split()

    for sortt in range(0, len(materials), 2):
        quantity = int(materials[sortt])
        material = (materials[sortt + 1])
        if material not in elements.keys():
            elements[material] = quantity
        else:
            elements[material] += quantity
        if material == "shards" or material == "fragments" or material == "motes":
            if elements[material] >= 250:
                legendary_item = legendary_items[material]
                elements[material] -= 250
                break

print(f"{legendary_item} obtained!")
items = [f"{key}: {value}" for key, value in elements.items()]
print(f"\n".join(items))