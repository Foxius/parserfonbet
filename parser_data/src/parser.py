import requests
import urllib3

urllib3.disable_warnings()

def get_data():
    out={}
    old=0
    p=[1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5,10.5,11.5,12.5,13.5]
    for i in requests.get('https://line07w.bkfon-resources.com/line/mobile/showEvents?sysId=2&lang=ru&scopeMarket=1600&lineType=live_line&skId=1', verify=False).json()['events']:
        data=requests.get(f'https://line53w.bkfon-resources.com/events/event?lang=en&eventId={i["id"]}&scopeMarket=1600&version=0', verify=False).json()
        for d in data['events']:
            if d['name']=='corners':
                tid=data['sports'][1]['id']
                out[tid]={'name': data["sports"][1]['name']}
                out[tid].update({'teams': {'team1': data['events'][0]['team1'], 'team2': data['events'][0]['team2']}})
                for y in data["customFactors"]:
                    if y['e']==d["id"]:
                        old=d['id']
                        tmp=[]
                        for t in y['factors']:
                            try:
                                if float(t['pt']) in p and str(t['pt'])[0] not in ['-', '+']:
                                    tmp.append(t)
                            except:pass
                        # if not len(tmp): del out[tid]
                        out[tid].update({'factors': tmp})
                        # except:pass
    return(out)
