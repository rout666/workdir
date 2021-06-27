from MemberList import MemberList

member_name = input('着任メンバーの名前を入力してください：')
member_age = input('着任メンバーの年齢を入力してください：')

new_member = MemberList(member_name,member_age)
new_member.info()