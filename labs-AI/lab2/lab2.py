import sys
import strategyRandom as sr
import strategyHillclimbing as shc
import strategyBacktracking as sbt
import strategyAstar as sastar

def hanoi_solve(filename, strategy):
    """
        Main function for solving the problem
    :param filename: file where n and m are found (no of towers, no of disks)
    :return:
    """

    if len(sys.argv) == 3:  # passed parameters at cmd line
        n = int(sys.argv[1])
        m = int(sys.argv[2])
    elif filename:     # passed filename at function call
        file_in = open(filename, 'r')
        file_in_text = file_in.read().split(' ')
        # print(file_in_text)
        n = int(file_in_text[0])
        m = int(file_in_text[1])
        # print('m is ', m, '| n is ', n, m + n)
    else:
        raise ValueError('No cmdline args or filename specified... Aborting operation.')

    if strategy == 'random':
        sr.solve_random(n,m)
    elif strategy == 'hillclimbing':
        shc.solve_hillclimbing(n,m)
    elif strategy == 'backtracking':
        sbt.solve_backtracking(n,m)
    elif strategy == 'a*':
        sastar.solve_a_star(n,m)

hanoi_solve('input.txt','random')
