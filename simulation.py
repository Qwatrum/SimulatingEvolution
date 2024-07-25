import random
import matplotlib.pyplot as plt


# i call the animals 'plics', i dont know why...

round_saves = []
plics = []
cs = []
AMOUNT_OF_PLICS = 80
ODDS_OF_MUTATION = 70
AMOUNT_OF_KILLS_IN_PERCENT = 50  # max 50
START_C = 0
AMOUNT_OF_ROUNDS = 1000


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
    global round_saves
    setup()
    round_saves.append(cs.copy())
    for i in range(AMOUNT_OF_ROUNDS):

        kill_visible_ones()
        reproduce()
        
        round_saves.append(cs.copy())
        

    
    
    print("Finished!")
    print(f"Highest c is {max(cs)}")
    print(f"Average is {sum(cs) / len(cs)}")

    plot_data()
    

def plot_data():
    max_data = []
    avergae_data = []
    
    for i in round_saves:
        
        max_data.append(max(i))
        avergae_data.append(sum(i) / len(i))
    
    plt.plot(max_data, "b-", label="Max")
    plt.plot(avergae_data, "y-", label="Average")
    plt.xlabel("Rounds / Generations")
    plt.ylabel("Amount")
    plt.legend(loc="upper left")
    
    plt.text(AMOUNT_OF_ROUNDS+2, max_data[-1], str(max_data[-1]))
    plt.text(AMOUNT_OF_ROUNDS+2, avergae_data[-1], str(avergae_data[-1]))


    plt.show()
    

start()