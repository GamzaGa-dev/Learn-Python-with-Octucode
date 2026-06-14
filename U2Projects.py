a = input("enter two digits\n")
print(len(a))
c = int(a[0])
b = int(a[1])
print(c + b)
#مشرةع المساحة
le = input('enter type length\n')
we = input('enter type wideth\n')
print( 'total area is ' +str( float(le) * float(we)))
#مشروع محاسبة الصنايعي
a = input('type length\n')
b = input('type width\n')
c = input('how much for one meter\n')
a2 = float(a)
b2 = float(b)
d = a2*b2
d2 = str(d)
c2 = float(c)
e = c2*d
e2 = str(e)
print('the total area is ' + d2)
print('give the guy ' +e2)
#مشروع عدد الساعات
se = input('enter number of second')
se2 = float(se)
hou = se2 // 3600
resec = se2 % 3600
minitue = resec // 60
resec2 =  resec % 60
print('there is a ' + str(hou) + ' hours and ' + str(minitue) + ' minitus and ' + str(resec2) + ' seconds')
#مشروع عدد الساعات بأسطر أقل
num = float(input("enter number of second\n "))
hou = num//3600
minitue = (num%3600)//60
sec = (num%3600)%60
print(f'you have {hou} hours and {minitue} minitus and {sec} seconds   ')