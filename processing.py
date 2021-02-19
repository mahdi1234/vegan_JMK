import json
import os


TAGS = "tags"
VEGAN_KEY = "diet:vegan"
VEGETARIAN_KEY = "diet:vegetarian"

pure_vegan = []
pure_vegetarian_with_vegan_options = []
pure_vegetarian = []
mixed = []
not_sorted = []

RESTAURANTS_WITH_NAMES = {
    "only_vegan": pure_vegan,
    "only_vegetarian": pure_vegetarian,
    "vegetarian_with_vegan_options": pure_vegetarian_with_vegan_options,
    "some_veg_options": mixed,
    "not_sorted": not_sorted,
}


with open("./output/source_data.json") as f:
    source = json.loads(f.read())

restaurants = source["elements"]

for restaurant in restaurants:
    # In some cases a node can contain no tags, skip the record then
    if restaurant.get(TAGS):
        vegan = restaurant[TAGS].get(VEGAN_KEY)
        vegetarian = restaurant[TAGS].get(VEGETARIAN_KEY)

        if vegan == "only":
            pure_vegan.append(restaurant)
        elif vegetarian == "only" and vegan == "yes":
            pure_vegetarian_with_vegan_options.append(restaurant)
        elif vegetarian == "only":
            pure_vegetarian.append(restaurant)
        elif (
            vegetarian == "yes" and vegan == "yes"
            or vegan == "yes"
            or vegetarian == "yes"
        ):
            mixed.append(restaurant)
        else:
            not_sorted.append(restaurant)


for name, restaurants in RESTAURANTS_WITH_NAMES.items():
    # Sort to ensure always a nice diff
    sorted_by_id = sorted(restaurants, key=lambda x: x["id"])
    dest_data = {}
    dest_data["elements"] = sorted_by_id
    with open("./output/" + name + ".json", "w", encoding="utf-8") as f:
        f.write(json.dumps(dest_data, ensure_ascii=False, indent=2))

os.unlink("./output/source_data.json")
