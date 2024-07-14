### list 
list_of_bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(list_of_bicycles[1])
print(list_of_bicycles[3])
print("...")

### tuples
dimensions = (250, 0, "test")
print('printing tuples:\n')
for i in dimensions:
      print(i)
print("...")

### dictionary
alien = {'color': 'green', 'points': 5}
print(alien)

alien['x_pos'] = 0
alien['y_pos'] = 25

print(alien['color'])


aliens = []

for alien_number in range(30):
    new_alien = {'color':'green', 'points':5, 'speed':'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)

print("...")

favorite_languages = {
        'jen': ['python','rust'],
        'sarah':['c'],
        'edward':['rust','go'],
        'phil':['python','haskell']
        }

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")
