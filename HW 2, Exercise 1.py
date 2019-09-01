class Chat:

    def connect_human(Human):
        print(Human.name+" Connected.")

    def connect_Robot(Robot):
        print(Robot.name+" Connected.")

    l=[]
    def add(self,string):
        self.l.append(string)

    def show_human_dialogue(self):
        for i in self.l:
            print(i)

    def show_robot_dialouge(self):
        strr=""
        for i in self.l:
            for k in i:
                if k=="a" or k=="e" or k=="o" or k=="u" or k=="i":
                    strr+="0"
                else:
                    strr+="1"

        print(strr)


class Human(Chat):
    def __init__(self, name):
        self.name = name

    def send(self,string):
        string= self.name+" said: "+string
        self.add(string)
        print(string)

class Robot(Chat):
    def __init__(self, name):
        self.name = name

    def send(self, string):
        string=self.name + " said: " + string
        self.add(string)
        print(string)

chat=Chat()
adnan=Human("Adnan")
robot=Robot("Robo123")
Chat.connect_human(adnan)
Chat.connect_Robot(robot)
adnan.send("Hi")
robot.send("hey bro")
print("\nHuman Dialouge:\n")
chat.show_human_dialogue()
print("\nRobot Dialouge:\n")
chat.show_robot_dialouge()

