

all_players = {"J1": (15, 60),"J2": (15, 55),"J3": (27, 55),"J4": (29, 72),"J5": (32, 38)}
my_data_list = list(all_players.items())

champion=[]
all_champions=[]
younger_players=[]

def get_player_to_compare(list_of_players):
        player_to_compare = list_of_players[0]
        print("player I compare", player_to_compare)
        print("my list of players",list_of_players)
        list_of_players.pop(0)
        print("my list of players without the one I compare", list_of_players)
        #get smaller players than the player we compare:
        for i in list_of_players:
            if i[1][0] <= player_to_compare[1][0]:
                younger_players.append(i)
                print("younger players :",younger_players)
        #check if elem of smaller players have an higher score:
        for i in younger_players:
            if i[1][1] <= player_to_compare[1][1] and player_to_compare not in champion:
                champion.append(player_to_compare)
                if champion not in all_champions:
                    all_champions.append(champion)
        list_of_players.append(player_to_compare)
        print("next players list:",list_of_players)
        print("Go to champion list :", champion)
        
        
        if list_of_players[0][0] == 'J1':
            print('stop function')
            return
        else :
            print('keep going')                    
            get_player_to_compare(list_of_players)

                
        
get_player_to_compare(my_data_list)
print("All champions are: ", all_champions)



    

 
        
    
   
