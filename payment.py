import random
random.seed(1059453)


class payment():

    def __init__(self,name=None,amount=None,day=None):
        if name==None and amount==None and day==None:

            self.generate()
        else:
            self.name=name
            self.amount=amount
            self.day=day


    
    def generate(self):
        self.amount=random.randrange(20,100)
        self.day=random.randrange(0,6) #0=monday-6=saturday
        karta=list("1234567890123456")
        char=list("ABCD")

        while(len(char)!=0):
            pointer=random.randrange(0,15)
            try:
                int(karta[pointer])
                karta[pointer]=char.pop()
                
            except: 
                pass

        self.name=''.join(str(i) for i in karta)


