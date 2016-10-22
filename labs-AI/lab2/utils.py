
def init(n,m):
    state_initial = [n] + [1] * m
    state_current = state_initial
    state_final = [n] * (m + 1)
    return state_initial, state_current, state_final


def valid_transition(currentState, tower_i, tower_j):
    k = 0
    t = 0

    if tower_i == tower_j: # same tower not allowed
        return False

    for i in range(1,len(currentState)):
        if currentState[i]==tower_i:
            k = i

    if k == 0:
        return False

    for j in range(1,len(currentState)):
        if currentState[j]==tower_j:
            t = j

    if k > 0 and k < t:
        return False
    return True


def transition(currentState, tower_i, tower_j):
    if valid_transition(currentState, tower_i, tower_j):
        for i in range(1, len(currentState)):
            if currentState[i] == tower_i:
                k = i
        currentState[k] = tower_j

    return currentState


def is_final_state(currentState, n, m):
    if currentState == [n] * (m + 1):
        return True
    return False

