class MemberList :
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def info(self):
        age = int(self.age) + 1
        print('氏名：' + self.name)
        print('年齢：' + str(self.age))
        print('来年は' + str(age) + '歳です。')