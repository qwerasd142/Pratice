
def std_weight(height, gender):
    if gender == '남자':
         return height * height * 22
    elif gender == '여자':
         return height * height * 21
        
height = 185
gender = '남자'
weight = round(std_weight(height / 100, gender),2)
print("키 {0} {1}의 표준 체중은 {2}Kg 입니다.".format(height,gender,weight))