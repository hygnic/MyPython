def get_formatted_name(first_name, last_name, middle_name=" "):
     if middle_name:
         full_name = first_name + ' ' + middle_name + ' ' + last_name
     else:
         full_name = first_name +' '+ last_name
     return full_name.title()
aman = get_formatted_name('john','hooker')
print(aman)
aman = get_formatted_name('john','hooker','lee')
print(aman)

#函数-返回字典
def build_person(name1,name2,age=''):
    person = {'first': name1, 'last': name2}
    if age:
        person['age'] = age
    return person
kate = build_person('kate','kob',27)
print(kate)

#函数-列表传递
def dic_city(cities):
    for city in cities:
        message1 = ("I love my " + city.title())
        print(message1)
a_city = ['london', 'piking']
dic_city(a_city)

#函数-列表修改 方法1
unprinted_designs1 = ['chair', 'axe', 'phone', 'bottom']
completed_models1 = []
while unprinted_designs1:
    current_designs1 = unprinted_designs1.pop()
    completed_models1.append(current_designs1)
print(completed_models1)

#函数-列表修改 方法2（用函数的方法）
def print_models(unprinted_designs,completed_models):
    while unprinted_designs:
        current_designs = unprinted_designs.pop()
        print('printing model: ' + current_designs)
        completed_models.append(current_designs)
def show_completed_models(completed_models):
    print('\nThe following models have been printed:')
    for completed_model in completed_models:
        print(completed_model)
unprinted_designs = ['kite', 'cup', 'car']
completed_models = []
print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)

#函数-组合使用任意数量实参
def pizza_order(size,*toppings):
    print('\nMaking a ' + str(size) + '-inch pizza with following toppings:')
    for topping in toppings:
        print(topping)
pizza_order(18,'mushrooms', 'green peppers', 'extra cheese') 
