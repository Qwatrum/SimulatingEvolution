import random

# i call the animals 'plics', i dont know why...

plics = []
cs = []
AMOUNT_OF_PLICS = 10
ODDS_OF_MUTATION = 100
AMOUNT_OF_KILLS_IN_PERCENT = 50  # max 50
START_C = 0
AMOUNT_OF_ROUNDS = 250


class Plic():
    def __init__(self, c) -> None:
        self.c = c # c stands for their skin color. 100 -> the same as the background | 0 -> really good visible

def create_new_plic(parent_c):
    if random.randrange(0,ODDS_OF_MUTATION) == 0:
        if parent_c != 100:
            parent_c+=2
    cs.append(parent_c)
    return Plic(parent_c)
    

def kill_visible_ones():
    
    times_of_rep = round(len(plics)*AMOUNT_OF_KILLS_IN_PERCENT/100)
    
    for i in range(times_of_rep):
        plics.pop(cs.index(min(cs)))
        cs.remove(min(cs))
    

def reproduce():

    new_plics = []
    for e in plics:
        new_plics.append(create_new_plic(e.c))
    
    for f in new_plics:
        plics.append(f)
    


def setup():
    for i in range(AMOUNT_OF_PLICS):
        plics.append(Plic(START_C))
        cs.append(START_C)

def start():
    setup()
    for i in range(AMOUNT_OF_ROUNDS):
        kill_visible_ones()
        reproduce()
        
    print("Finished!")
    print(f"Highest c is {max(cs)}")
    print(f"Average is {sum(cs) / len(cs)}")
    print(cs)


start()