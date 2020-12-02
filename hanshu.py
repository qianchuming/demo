def move(players, step):
    num = step - 1
    while num > 0:
        tmp = players.pop(0)
        players.append(tmp)
        num = num - 1
    return players
def play(players,step,alive):
    player_list = [i for i in range(1,players+1)]
    while len(player_list)>alive: 
        player_list = move(player_list,step)
        player_list.pop(0) 
    return player_list
players = int(input("请输入参加游戏的人数: "))
step = int(input("请输入淘汰的数字："))
alive = int(input("请输入幸存人数："))

play_result = play(players, step, alive)
print("幸存人数编号为:")
print(play_result)