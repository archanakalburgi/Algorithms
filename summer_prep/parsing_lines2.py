import collections

class TradeReconciliation:
    def __init__(self):
        self.company = set()

    def process(self, line):  

        line_list = line.split(",")
        if line_list[0] != "reconciliation":
            if line_list[0] in self.company:
                if line_list[1][line_list[1]] != line_list[1][line_list[1]]:
                    line_list[0].add(tuple(line_list[0:]))
            else:
                line_list[0] = dict()
                line_list[0][line_list[0]] = set()
                if line_list[1][line_list[1]] != line_list[1][line_list[1]]:
                    line_list[0][line_list[0]].add(tuple(line_list[0:]))
            return line_list[2]   
        
        else:
            return len(line_list[0]) 
            

lines =[ 
    "akuna,a,10,12:01:00",
    "akuna,b,-15,12:05:00",
    "reconciliation,akuna,exchange1",
    "reconciliation,exchange1,akuna",
    "exchange1,b,-15,12:05:00",
    "exchange1,b,-20,12:07:00",
    "reconciliation,akuna,exchange1",
    "reconciliation,exchange1,akuna",
    "reconciliation,exchange2,akuna" ]


tr = TradeReconciliation()
for line in lines:
    print(tr.process(line)) 