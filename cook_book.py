with open('recipes.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    cook_book = {}
    i = 0
    while i < len(lines):
        dish_name = lines[i].strip()
        cook_book[dish_name] = []
        ingredients_num = int(lines[i + 1].strip())
        for j in range(i + 2, i + 2 + ingredients_num):
            v = lines[j].strip('\n').split(' | ')
            cook_book[dish_name].append({'ingredient_name': v[0], 'quantity': v[1], 'measure': v[2]})
        i += ingredients_num + 3


dishes_list = ['Фахитос', 'Омлет']


def get_shop_list_by_dishes(dishes, person_count):
    all_ingredients = {}
    for dish in dishes:
        ingredients = cook_book.get(dish)
        for ingredient in ingredients:
            measure = ingredient.get('measure')
            quantity = int(ingredient.get('quantity')) * person_count
            if ingredient['ingredient_name'] in all_ingredients:
                quantity_ = all_ingredients[ingredient['ingredient_name']]['quantity']
                all_ingredients[ingredient['ingredient_name']] = {'quantity': quantity_ + quantity}
            else:
                all_ingredients[ingredient['ingredient_name']] = {'measure': measure, 'quantity': quantity}
    return all_ingredients


print(get_shop_list_by_dishes(dishes_list, 2))
