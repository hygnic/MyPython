print('hello world')

print("Languages:\n\tPython\n\tC\n\tJaveScript")

test1 = 'ada lobe nivii'
print(test1.title())

a = [1,2,3,4,5]
a.insert(-1,8)
print(a)

magicians = ['carolina','alice','kate']
for magician in magicians:
    print(magician.title())

for value in range(0,5):
    print(value)

numbers = list(range(0,7))
print(numbers)

squares = []
for value in range(1,11):
    squares.append(value**2) #P52
print(squares)

asd = [1,2,7,23,3,4]
print(sum(asd))
print(asd[:3])
add = asd[:4]
print(add)

dimensions = (0,1,2,3)  #元组

special = (1,2,3)       #元组列表的数据不可变化，但是其变量能赋予其他值。
special = (1)
print(special)

car = 'audi'
print("is car == audi,I predict ture")
print(car == 'audi')

user_1 = ['carolina','david','kate','marry']
for user_2 in user_1:
    print("\nHello " + user_2.title() +
        ", would you like to see a status report ?")
    if user_2 == 'david':
        print('How are you')

favorite_languages = {
    'jen' : "python",
    'sarah' : 'c',
    'edward' : 'ruby',
}
for name in sorted(favorite_languages.keys()):  #sorted进行了排序
    print('\nHi, ' + name.title())
if 'ludewege' not in favorite_languages.keys():
    print('fuck you')
