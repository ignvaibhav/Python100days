class ToDoList:
    def __init__(self):
        self.tasks = []
        
    def displaying(self):
        print(f"Here are all the tasks for today : \n")
        for i in self.tasks:
            for j,k in i.items():
                if j == "status":
                    if k == False:
                        s = "📛"
                    elif k == True:
                        s = "✅"
                else:
                    print(f"{s} {j}")
                    print(f"{k}\n")
                
    
    def adding(self, task_name, desc, currentStatus=False):
        newTask = {"status" : currentStatus, task_name : desc}
        self.tasks.append(newTask)
    
    def removing(self, task_name):
        for i in self.tasks:
            for j,k in i.items():
                if j == task_name:
                    self.tasks.remove(i)
                    break
                
    def update(self, taskname, currentStatus):
        for i in self.tasks:
            for j in i.keys():
                if j == taskname:
                    i["status"] = currentStatus
