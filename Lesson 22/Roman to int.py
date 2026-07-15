def romanToInt(romaninput):
    roman={'M':1000,'D':500,'C':100,'L':50,'X':50,'V':5,'I':1}
    resultInteger=0

    for i in range(0,len(romaninput)-1):
        if roman[romaninput[i]<roman[romaninput[i+1]]]:
            resultinteger-=roman[romaninput[i]]
        else:
            resultinteger+=roman[romaninput[i]]
    return resultinteger+roman[romaninput[-1]]

roman=input("Input roman numeral:")

print("Integer equiavelent:", romanToInt(roman))