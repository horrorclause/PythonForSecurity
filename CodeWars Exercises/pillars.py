#!/usr/bin/python3

def pillars(num_pill, dist, width):
    try:
        if num_pill == 1 or num_pill == 0:   # If only 1 pillar is supplied, distance is 0
            return 0
        elif num_pill == 2:
            return dist*100
        else:
            aggregateDist = ((num_pill - 1)*dist)*100  # Takes distance b/w pillars only
            pillarWidth = (num_pill-2) * width
    except Exception as e:
        print(e)
        pass
    return (aggregateDist + pillarWidth)
