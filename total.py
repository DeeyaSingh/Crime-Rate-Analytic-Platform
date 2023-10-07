import mysql.connector as mysqlc
import matplotlib.pyplot as plt
total1=0
total2=0
total3=0
mydb=mysqlc.connect(host='localhost',user='root',passwd='user123',database='mydatabase')
mycursor= mydb.cursor()
mycursor.execute("Select year2019 from nagaland_crimes ")
nagaland=mycursor.fetchall()
for z1 in range(0,8):
     total1=total1+int(nagaland[z1][0])
print(total1)
mycursor.execute("Select year2019 from up_crimes ")
up=mycursor.fetchall()
for z2 in range(0,8):
     total2=total2+int(up[z2][0])
print(total2)
mycursor.execute("Select year2019 from karnataka_crimes ")
karnataka=mycursor.fetchall()
for z3 in range(0,8):
     total3=total3+int(karnataka[z3][0])
print(total3)
total_crimes = [total1,total2,total3]
locations = ['nagaland', 'uttar pradesh','karnataka']
colors = ['lavender', 'plum','mediumpurple']
plt.pie(total_crimes, labels=locations, colors=colors, autopct='%.1f%%')
plt.show()
    
