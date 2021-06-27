class MemberList :
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def info(self):
        age = int(self.age) + 1
        print('氏名：' + self.name)
        print('年齢：' + str(self.age))
        print('来年は' + str(age) + '歳です。')


member_name = input('着任メンバーの名前を入力してください：')
member_age = input('着任メンバーの年齢を入力してください：')

new_member = MemberList(member_name,member_age)
new_member.info()
