class card():
    def __init__(self,item):
        self.name=item.name
        self.days=[item.day]
        self.amount=item.amount
        self.visits=0
    
    def addData(self,amount,day):
        self.days.append(day)
        self.amount+=amount
        self.visits+=1
