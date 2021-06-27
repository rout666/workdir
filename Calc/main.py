from calc import Calc

intDataA = int(input('整数(A)を入力してください==>'))
intDataB = int(input('整数(B)を入力してください==>'))
print('計算方法を選択してください')
intWork = int(input('1:加算　2:減算　3:乗算　4:除算　5:剰余==>'))

main = Calc(intDataA,intDataB,intWork)
print(main.main())
