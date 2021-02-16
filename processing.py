import json

with open("source_data.json") as f:
    whole_data = json.loads(f.read())


restaurants = whole_data["elements"]
tags = "tags"
vegan_key = "diet:vegan"
vegetarian_key = "diet:vegetarian"

pure_vegan = []
pure_vegetarian_with_vegan_options = []
pure_vegetarian = []
mixed = []
errors = []


for restaurant in restaurants:
    # In some cases the restaurant is added as a "type": "way" instead of "node"
    # Then each node of the way doesn't have separate tags
    if restaurant.get(tags):
        vegan_present = restaurant[tags].get(vegan_key)
        vegetarian_present = restaurant[tags].get(vegetarian_key)

        if vegan_present == "only":
            pure_vegan.append(restaurant)
        elif vegetarian_present == "only" and vegan_present == "yes":
            pure_vegetarian_with_vegan_options.append(restaurant)
        elif vegetarian_present == "only":
            pure_vegetarian.append(restaurant)
        elif (
            vegetarian_present == "yes" and vegan_present == "yes"
            or vegan_present == "yes"
            or vegetarian_present == "yes"
        ):
            mixed.append(restaurant)
        else:
            errors.append(restaurant)


sorted_restaurants = [
    pure_vegan,
    pure_vegetarian,
    pure_vegetarian_with_vegan_options,
    mixed,
    errors,
]

names = [
    "t_only_vegan",
    "t_only_vegetarian",
    "t_vegetarian_with_vegan_options",
    "t_some_veg_options",
    "t_errors",
]

for restaurant_list, name in zip(sorted_restaurants, names):
    new_data = {}
    new_data["elements"] = restaurant_list
    with open(name + ".json", "w", encoding="utf-8") as f:
        f.write(json.dumps(new_data, ensure_ascii=False, indent=2))
