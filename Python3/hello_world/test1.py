aliens = []
for a_number in range(30):
    new_aliens = {'color': 'green', 'point': 5, 'speed': 'slow'}
    aliens.append(new_aliens)
print(aliens)

aliens = []
for alien_number in range(30):
    new_aliens = {'color': 'green', 'point': 5, 'speed': 'slow'}
    aliens.append(new_aliens)
for alien in aliens[:3]:
    alien['color'] = 'yellow'
    alien['point'] = 10
    alien['speed'] = 'fast'
print(alien)


a_list = ['caroli']
print(len(a_list))

def greet_u():
    print("HEllO")
greet_u()
