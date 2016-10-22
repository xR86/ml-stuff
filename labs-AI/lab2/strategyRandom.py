
from random import randint
import utils as ut


def random(n):
    tower_i = randint(1, n)
    tower_j = randint(1, n)
    return tower_i, tower_j

def solve_random(n,m):
    file_out = open('output.txt', 'w')

    initial, current, final = ut.init(n,m)
    last_sol = m
    print('states: ', initial, current, final)
    counter = 0

    while not ut.is_final_state(current,n,m):
        # alege i,j
        tower_i, tower_j = random(n)
        print('towers: ', tower_i, tower_j)

        if ut.valid_transition(current, tower_i, tower_j) is True:
            print('is valid')
            current = ut.transition(current, tower_i, tower_j)


            s = '(%d, %d)\n' % (tower_i, tower_j)
            file_out.write(s)
            counter = 0

            #if current[last_sol] == n:
                #last_sol -= 1

        if counter == 100:
            break

        current = ut.transition(current, tower_i, tower_j)
        counter += 1

    print('states: ', initial, current, final)
    file_out.close()
