file = open(r'day3_data.txt', 'r')

class Player:
    def __init__(self, right, down):
        self.x = 0
        self.y = 0
        self.trees = 0
        self.right = right
        self.down = down

class GameMap:
    def __init__(self, content):
        self.content = content
        #x length 31
        self.width = len(content[0])
        #y length 323
        self.height = len(content)

def getEncounter(player, gameMap):
    return gameMap.content[player.x][player.y]

def run(player, gameMap):
    while player.x < gameMap.width:
        player.x += player.right
        player.y += player.down

        if getEncounter(player, gameMap) == '#':
            player.trees += 1
        print('# of trees: ', player.trees)
 
player = Player(3, 1)
gameMap = GameMap(file.read().splitlines())

run(player, gameMap)
