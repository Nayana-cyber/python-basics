character=[]

for ch in 'TutorialsPoint':
    if ch not in 'aeiou' :
        character.append(ch)
        print(character)

        #or list comprehension

chars = [x for x in 'TutorialPoints' if x not in 'aeiou']
print(chars)

# squares

squares = [x*x for x  in range(1,11)]
print(squares)