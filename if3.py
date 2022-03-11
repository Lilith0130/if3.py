height = input('請輸入身高(cm)： ')
weight = input('請輸入體重(kg)： ')
height = int(height)
weight = int(weight)
height = height / 100 # 換成公尺
bmi = weight / height / height     
if bmi < 18.5:
    print('你的bmi值為', bmi, '屬體重過輕')
elif bmi >= 18.5 and bmi < 24:
    print('你的bmi值為', bmi, '屬正常範圍')
elif bmi >= 24 and bmi < 27:
    print('你的bmi值為', bmi, '稍重')
elif bmi >= 27 and bmi < 30:
    print('你的bmi值為', bmi, '輕度肥胖')
elif bmi >= 30 and bmi < 35:
    print('你的bmi值為', bmi, '中度肥胖')
elif bmi >= 35: # 寫else: 也可以
    print('你的bmi值為', bmi, '重度肥胖')