def simulate(input, days):
    
    state = {}
    for i in range(9):
        state[i] = 0
    
    with open(input, 'r') as fp:
        data = fp.read()
        data = [int(n) for n in data.split(',')]
    
    for value in data:
        state[value] += 1
    

    state = {k: v for k, v in sorted(state.items())}

    for i in range(days):
        #print(f'day {i} state: {state}')
        newfish = 0
        for j in range(9):
            if j == 0:
                newfish = state[j]
            else:
                state[j-1] = state[j]

        
        state[6] += newfish
        state[8] = newfish

        state = {k: v for k, v in sorted(state.items())}
    
    sum = 0
    for key in state:
        sum += state[key]

    print(sum)
    

simulate('input', 80)

simulate('input', 256)

