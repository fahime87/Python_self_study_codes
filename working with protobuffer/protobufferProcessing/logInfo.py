
class log():
    list_=[]
    def __init__(self,type,date,module,action,message,):
        self.type=type
        self.message=str(message)
        self.date=date
        self.action=action
        self.module=module
        self.show_log()
        self.logToDB()
    def show_log(self):
        print(self.type,self.date,self.module,self.action,self.message,sep="|")
    def logToDB(self):
        self.list_.append((self.type, self.module, self.action, self.date, self.message))





