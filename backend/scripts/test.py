import json
import os

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))

def generate_category():
    with open(os.path.join(CURRENT_DIR, "mocks", "pho21", "pho21.json"), 'r') as fp:
        json_data = json.load(fp)
        menu_categories = json_data['menu_categories']
        for item in menu_categories:
            del item['items']
            del item['id']

        with open(os.path.join(CURRENT_DIR, "mocks", "pho21", "categories.json"), 'w') as p:
            json.dump(menu_categories, p, indent=2)

def generate_add_on_group():
    with open(os.path.join(CURRENT_DIR, "mocks", "pho21", "pho21.json"), 'r') as fp:
        json_data = json.load(fp)
        addOnGroups = json_data['modifier_categories']
        myGroups = []
        for item in addOnGroups:
            g = {
                "name": item['name'],
                "minQuantity": item['min_qty'],
                "maxQuantity": item['max_qty']
            }
            myGroups.append(g)

        with open(os.path.join(CURRENT_DIR, "mocks", "pho21", "addOnGroups.json"), 'w') as p:
            json.dump(myGroups, p, indent=2)

def generate_recipe():
    with open(os.path.join(CURRENT_DIR, "mocks", "pho21", "pho21.json"), 'r') as fp:
        json_data = json.load(fp)
        menu_categories = json_data['menu_categories']
        my_menu_categories = {}
        for c in menu_categories:
            recipes = []
            if c == 'Party Tray':
                continue
            for idx, item in enumerate(c['items']):
                try:
                    r = {
                        "name": item['name'],
                        "description": item['description'],
                        "price": item['price'],
                        "size": item['size'],
                        "imageUrl": "",
                        "active": True,
                        "isTaxable": True,
                        "taxRate": item['tax_rate'],
                    }
                    recipes.append(r)
                except Exception as e:
                    pass
            group = {c['name']: recipes}
            my_menu_categories.update(group)

        with open(os.path.join(CURRENT_DIR, "mocks", "pho21", "recipes.json"), 'w') as p:
            json.dump(my_menu_categories, p, indent=2)

def generate_add_on():
    with open(os.path.join(CURRENT_DIR, "mocks", "pho21", "pho21.json"), 'r') as fp:
        json_data = json.load(fp)
        addsOnGroup= {}
        # {
        #     "Select Noodle Type | Pho": [{Pho tuoi, name, price} . {Pho thuong, name, price}]
        # }

        venderIdToNameGroupMapping = {}

        for item in json_data['modifier_categories']:
            addsOnGroup[item['name']] = []
            #map each vender add-on id to group name
            # import pdb; pdb.set_trace()
            for addon_id in item['modifiers']:
                venderIdToNameGroupMapping[addon_id] = item['name']
            #{63334: slect noodle},{12111: select noodle}
        for addon in json_data['modifiers']:
            a = {
                "name": addon['name'],
                "price": addon['price'],
                "description": addon['description'],
                "isTaxable": addon['is_taxable'],
            }
            group_name = venderIdToNameGroupMapping[addon['id']]
            addsOnGroup[group_name].append(a)


        with open(os.path.join(CURRENT_DIR, "mocks", "pho21", "addsOn.json"), 'w') as p:
            json.dump(addsOnGroup, p, indent=2)

def generate_recipe_to_add_on_group():
    with open(os.path.join(CURRENT_DIR, "mocks", "pho21", "pho21.json"), 'r') as fp:
        json_data = json.load(fp)
        recipeToGroup = {}
        venderIdToNameGroupMapping = {}
        for group in json_data['modifier_categories']:
            venderIdToNameGroupMapping[group['id']] = group['name']


        for c in json_data['menu_categories']:
            if c == 'Party Tray':
                continue
            for idx, recipe in enumerate(c['items']):

                # import pdb; pdb.set_trace()
                recipeToGroup[recipe['name']] = []

                if "Party Tray" in recipe['name']:
                    continue

                if 'modifier_categories' not in recipe:
                    print(idx, recipe)
                for g_id in recipe['modifier_categories']:
                    if venderIdToNameGroupMapping[g_id]:
                        recipeToGroup[recipe['name']].append(venderIdToNameGroupMapping[g_id])
                    else:
                        raise Exception("group {} not found".format(g_id))


        with open(os.path.join(CURRENT_DIR, "mocks", "pho21", "recipeToAddOnGroup.json"), 'w') as p:
            json.dump(recipeToGroup, p, indent=2)



if __name__ == "__main__":
    generate_category()
    generate_add_on_group()
    generate_recipe()
    generate_add_on()
    generate_recipe_to_add_on_group()
