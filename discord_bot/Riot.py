from riotwatcher import LolWatcher, ApiError


TOKEN = LolWatcher("TOKEN")
region = 'jp1'


def get_summoner_data(summoner_name):
    #辞書型
    try: 
        summoner = TOKEN.summoner.by_name(region, summoner_name)
    except ApiError as err:
        if err.response.status_code == 404: #サモナー情報無し
            return 0
        else:
            return summoner


        
def rank(summoner_name):
    
    if get_summoner_data(summoner_name) == 0:
        return get_summoner_data(summoner_name)
    else:
        data = TOKEN.summoner.by_name(region, summoner_name)
        ranked_stats = TOKEN.league.by_summoner(region, data['id'])
        try:
            ranked_stats= {'rank':ranked_stats[0]['rank'], 'tier':ranked_stats[0]['tier']}
            return ranked_stats
        #ランク情報なし
        except IndexError:
            return 1

def test(summoner_name):
    data = TOKEN.summoner.by_name(region, summoner_name)
    ranked_stats = TOKEN.league.by_summoner(region, data['id'])
    try:
        ranked_stats= {'rank':ranked_stats[0]['rank'], 'tier':ranked_stats[0]['tier']}
        return ranked_stats
    except IndexError:
        return 0







