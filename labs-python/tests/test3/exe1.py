
f = open('input2.txt', 'r')
g = open('output.txt', 'w')

def is_palindrome(count):
    if count > 10:
        if str(count) == str(count)[::-1]:
            return True
        return False

count = 0
for line in f.readlines():
    if 'pythoN' in line and is_palindrome(count):
        print count, ' ', str(count)[::-1]
        print line

    count += 1