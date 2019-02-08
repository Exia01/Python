inventory = {'croissant': 19, 'bagel': 4, 'muffin': 8, 'cake': 1}

#update and remove items from inventory

stock_list = {"cookie": 18}
# could also add after creating blank
# stock_list['cookie'] = 18

stock_list.update(inventory)

stock_list.pop('cake')
