import collections

class TradeReconciliation:
    def __init__(self):
        self.d = dict()   

    def process(self, line):  

        line_list = line.split(",")
        count = 0
        if line_list[0] != "reconciliation":
            if line_list[0] in self.d:
                self.d[line_list[0]].add(tuple(line_list[0:]))
            else:
                self.d[line_list[0]] = set()
                self.d[line_list[0]].add(tuple(line_list[0:]))
            return line_list[2]
        
        else:
            if line_list[2] not in self.d:
                count = count + len(self.d[line_list[1]])
            elif line_list[1] not in self.d:
                count = count + len(self.d[line_list[2]])
            else:
                for val in self.d[line_list[1]]:
                    if val not in self.d[line_list[2]]:
                        count += 1
            return count

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