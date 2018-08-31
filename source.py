from urllib import request

'''rank_url = 'https://fantasyfootballcalculator.com/adp.php'
qb_url = 'https://www.fantasypros.com/nfl/projections/qb.php?week=draft'
rb_url = 'https://www.fantasypros.com/nfl/projections/rb.php?week=draft'
wr_url = 'https://www.fantasypros.com/nfl/projections/wr.php?week=draft'
te_url = 'https://www.fantasypros.com/nfl/projections/te.php?week=draft'

def get_data(position_url,prefix):
    doc = open(prefix+'.txt','w')
    page = request.urlopen(position_url)
    raw = page.read()
    data = str(raw)
    doc.write(data)
    doc.close()'''

def process_scores(file_name,index,depth):
    doc = open(file_name,'r')
    info = doc.read()
    compressed = str(info).split('mpb-available')
    players = {}
    for x in range(1,depth):
        attr = (compressed[x].split('class'))
        score = float(attr[index][10:14])
        left_half = attr[2].split('>')
        name = left_half[1].split('<')
        players[name[0]] = score
    return players

def process_rank(file_name):
    doc = open(file_name,'r')
    info = doc.read()
    compressed = (str(info)).split('class="adp-player-name')
    players = {}
    for x in range(1,98):
        left_half = compressed[x].split('>')
        name = left_half[1].split('<')
        players[name[0]] = x
    return players

def get_player_list(file_name):
    doc = open(file_name,'r')
    info = doc.read()
    compressed = (str(info)).split('class="adp-player-name')
    players = []
    for x in range(98,0,-1):
        left_half = compressed[x].split('>')
        name = left_half[1].split('<')
        players.append(name[0])
    return players

qb_to_score = process_scores('qb.txt',13,35)#26
rb_to_score = process_scores('rb.txt',11,58)#55
wr_to_score = process_scores('wr.txt',11,61)#50
te_to_score = process_scores('te.txt',8,17)#11

names_to_score = {}
names_to_score.update(qb_to_score)
names_to_score.update(rb_to_score)
names_to_score.update(wr_to_score)
names_to_score.update(te_to_score)

player_to_rank = process_rank('rank.txt')
player_list = get_player_list('rank.txt')
rank_to_player = {v: k for k, v in player_to_rank.items()}

names_to_qb = {k: 'q' for k, v in qb_to_score.items()}
names_to_wr = {k: 'w' for k, v in wr_to_score.items()}
names_to_rb = {k: 'r' for k, v in rb_to_score.items()}
names_to_te = {k: 't' for k, v in te_to_score.items()} #only used for names_to_pos

names_to_pos = {}
names_to_pos.update(names_to_qb)
names_to_pos.update(names_to_wr)
names_to_pos.update(names_to_rb)
names_to_pos.update(names_to_te)

