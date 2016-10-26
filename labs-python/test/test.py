'''
8.25-8.50
    for i in text:
        if
    for i in caractere:
        if text.find(i)
    print text, caractere
'''

print '################Exe 1'
#Exe 1
def numara_caractere(text, caractere):
    sum = 0
    for i in range(len(text)):
        if text[i] in caractere:
            sum += 1
    return sum



print numara_caractere(text="hello world", caractere=("h", "l", "o"))
print numara_caractere(text="Python is awesome", caractere=("o", "e"))



print '################Exe 2'
#Exe 2
def gaseste_asemanari(a, b):
    a = set(a)
    b = set(b)

    intersection = a & b
    print 'intersection is', intersection
    return intersection


print gaseste_asemanari([1,2],[1]) #=> [1]
print gaseste_asemanari([1,2],[1,2]) #=> [1,2]
print gaseste_asemanari([1,2,1],[1,2]) #=> [1,2]
print gaseste_asemanari([1,2],[1,2,1]) #=> [1,2]
print gaseste_asemanari(["1", 2, None, None, True, "3"], ["None", None, True, 1, "1"]) #=>["1", None, True]
print gaseste_asemanari([1,2,3,4,5,6,5,4,3,2,1], [1,1,2,2,3,3,4,5])
    #=> [1,2,3,4,5] # desi 3, 2, 1 apar de doua ori in ambele liste, in rezulat apar o singura data.



print '################Exe 3'
#Exe 3
def rezolva_pattern(template, context):
    template = template.split(" ")
    print template, 'und das ist context.keys: ', context.keys()

    for i in range(len(template)):
        print 'stubs ', template[i][:1], template[i][-2:-1]
        if template[i][:1] == '#' and template[i][:-1] == '#':
            template[i] = template[i][1:-1]

    '''for i in template:
        if i in context.keys():
            print 'ja', i, context.keys()
    '''
    for i in range(len(template)):
        temp = '#' + template[i] + '#'
        if temp in context.keys():
            print 'ja'

    pass

rezolva_pattern(template="hello #who#", context={"who": "world"}) #=> "hello world'
rezolva_pattern(template="I am #action# #language#", context={"action": "learning","language": "Python"}) #=> 'I am learning Python'
rezolva_pattern(template="Dont {{do}} this #do#", context={"do": ", seriously"}) #=>'Don't {{do}} this , seriously