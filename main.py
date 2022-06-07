import parser_data
from flask import Flask, render_template
from flask_table import Table, Col

app= Flask(__name__)

class ItemTable(Table):
    col1 = Col('Лига')
    col2 = Col('Матч')
    col3 = Col('TM')
    col4 = Col('O')
    col5 = Col('U')

class ItemTable2(Table):
    col1 = Col('')

class Item(object):
    def __init__(self, col1, col2, col3, col4, col5):
        self.col1 = col1
        self.col2 = col2
        self.col3 = col3
        self.col4 = col4
        self.col5 = col5

class Item2(object):
    def __init__(self, col1):
        self.col1 = col1

@app.route('/')
def data():
    data=parser_data.get_data()
    print(data)
    tmp={}
    tmp[0]=[data[i]['name'] for i in data]
    tmp[1]=[data[i]['teams'] for i in data]
    tmp[2]=[data[i]['factors'] for i in data]
    
    items = []
    items2 = {}
    tmpd = []

    for i in range(len(tmp[2])):
        items2[i]={'f': [Item2(str(y['f'])) for y in tmp[2][i]]}
        items2[i].update({'v': [Item2(str(y['v'])) for y in tmp[2][i]]})
        items2[i].update({'pt': [Item2(str(y['pt'])) for y in tmp[2][i]]})
    
    ff=0
    for i in range(len(tmp[0])):
        print(len(items2[i]['v'][0:100:2]), len(items2[i]['v'][i:][1:100:2]), len(items2[i]['v']))
        if not ff:
            items.append(Item(tmp[0][i], f'{tmp[1][i]["team1"]} - {tmp[1][i]["team2"]}', ItemTable2(items2[i]['pt'][0:100:2]), ItemTable2(items2[i]['v'][0:100:2]), ItemTable2(items2[i]['v'][1:100:2])))
            ff=1
            i+=1
        else:
            ff=0
            
    
    return render_template('index.html', table=ItemTable(items).__html__())
        
app.run(debug=True, host='0.0.0.0')
