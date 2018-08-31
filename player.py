import source
import permutation

q_stack = []
r_stack = []
w_stack = []
t_stack = []

def fill_position_stacks():
    for x in source.player_list:
        position = source.names_to_pos[x]
        if position == 'q':
            q_stack.append(x)
        elif position == 'w':
            w_stack.append(x)
        elif position == 'r':
            r_stack.append(x)
        else:
            t_stack.append(x)

fill_position_stacks()

three_wr_set = ['w','w','w','r','r','t','q']
three_rb_set = ['w','w','r','r','r','t','q']
no_te_three_wr = ['w','w','w','r','r','q']
no_te_three_rb = ['r','r','r','w','w','q']
no_teqb_three_wr = ['r','r','w','w','w']
no_teqb_three_rb = ['w','w','r','r','r']

draft_orders = list(permutation.perm_unique(three_wr_set))
second_half = list(permutation.perm_unique(three_rb_set))
for x in second_half:
    draft_orders.append(x)

no_te_orders = list(permutation.perm_unique(no_te_three_wr))
no_te_second_half = list(permutation.perm_unique(no_te_three_rb))
for x in no_te_second_half:
    no_te_orders.append(x)

no_teqb_orders = list(permutation.perm_unique(no_teqb_three_wr))
no_teqb_second_half = list(permutation.perm_unique(no_teqb_three_rb))
for x in no_teqb_second_half:
    no_teqb_orders.append(x)

def draft(spot,positions):
    roster = []
    round = 1
    pick = 1
    q_copy = q_stack[:]
    r_copy = r_stack[:]
    w_copy = w_stack[:]
    t_copy = t_stack[:]
    list_copy = source.player_list[:]
    wraparound_spot = 13-spot #second half of snake, even rounds
    odd_round = (round % 2 == 1)
    while (round <= 5):#6 for no te
        while (pick <= 12):
            if ( (pick != spot and odd_round)
                or (pick != wraparound_spot and not odd_round)):
                    taken = list_copy.pop()
                    pos = source.names_to_pos[taken]
                    eval(pos+'_copy').remove(taken)
            else:
                pos = positions[round-1] #round 1 uses 0th index
                choice = (eval(pos+'_copy').pop())
                list_copy.remove(choice)
                roster.append(choice)
            pick += 1
        round += 1
        pick = 1
    return roster

def get_score(team):
    score = 0
    for x in team:
        score += (source.names_to_score[x])
    return score

def find_best(draft_orders):
    max_score = 0
    best_team = []
    score = 0
    for y in range(1,13):
        for x in draft_orders:
            team = draft(y,x)
            score = get_score(team)
            if (score > max_score):
                max_score = score
                best_team = team
        print(best_team,max_score)
        max_score = 0

find_best(no_teqb_orders)