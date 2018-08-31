from urllib import request

team_stats = 'http://www.nfl.com/stats/categorystats?tabSeq=2&offensiveStatisticCategory=GAME_STATS&conference=ALL&role=TM&season=2015&seasonType=POST&d-447263-s=TOTAL_YARDS_GAME_AVG&d-447263-o=2&d-447263-n=1'

def webpage_to_csv(url):
    response = request.urlopen(url)
    csv = str(response.read())
    csv_lines = csv.split('\\n')
    dest = r'nfl.csv'
    fw = open(dest,'w')
    for line in csv_lines:
        fw.write(line+'\n')
    fw.close()

webpage_to_csv(team_stats)

import whatevers