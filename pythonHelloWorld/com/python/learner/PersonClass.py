class PersonClass:
    def __init__(self,name):
        self.name=name
    def talk(self):
        print(f'Talking with {self.name}')

personClass=PersonClass("Sanketh")
personClass.talk()

