import pickle

class Hero():
    def __init__(self, ig_id, rarity):
        self.id = ig_id
        self.rarity = rarity
        self.state='Rest'
        self.hp_percentage=1
    def infos(self):
        print(self.id+' | '+self.rarity+' | '+self.state+' | '+str(self.hp_percentage))

    def change_state(self,new_state):
        self.state=new_state
        print('New state is:'+str(self.state))
    
    
def save_Heroes():
    Heroes=[]
    with open('heroes.pkl', 'wb') as outp:
        Heroes.append(Hero('2513640','Common'))
        Heroes.append(Hero('1283966','Common'))
        Heroes.append(Hero('1283922','Common'))
        Heroes.append(Hero('1283901','Common'))
        Heroes.append(Hero('1283824','Common'))
        Heroes.append(Hero('1283734','Common'))
        Heroes.append(Hero('1283600','Common'))
        Heroes.append(Hero('1283599','Common'))
        Heroes.append(Hero('1283598','Epic'))
        Heroes.append(Hero('1283597','Common'))
        Heroes.append(Hero('1283596','Common'))
        Heroes.append(Hero('1283594','Common'))
        Heroes.append(Hero('1283593','Common'))
        Heroes.append(Hero('1283592','Common'))
        Heroes.append(Hero('1283591','Common'))
        for hero in Heroes:
            pickle.dump(hero, outp, pickle.HIGHEST_PROTOCOL)

def load_Heroes():
    Heroes=[]
    with open('heroes.pkl', 'rb') as inp:
        for i in range(15):
            Heroes.append(pickle.load(inp))
            Heroes[i].infos()