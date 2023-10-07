from tkinter import *
import mysql.connector as mysqlc
import matplotlib.pyplot as plt
m=['2011','2012','2013','2014','2015','2016','2017','2018','2019']
mydb=mysqlc.connect(host='localhost',user='root',passwd='user123',database='mydatabase')
mycursor= mydb.cursor()
mycursor.execute("drop table up_crimes")
mycursor.execute("Create table up_crimes(crimes char(50),year2011 int, year2012 int,year2013 int,year2014 int, year2015 int, year2016 int, year2017 int,year2018 int, year2019 int)")
sql= "insert into up_crimes(crimes,year2011,year2012,year2013,year2014,year2015,year2016,year2017,year2018,year2019) values(%s, %s, %s, %s, %s,%s,%s,%s,%s,%s)"
val= [
    ('Theft','43854','43921','42897','43870','42856','43862','43843','43838','43827'),
    ('Robbery','3673' ,'4637','4462','4244','3352','3547','3457','4343','4243'),
    ('Burglary','25785','24223','23735','23844','24788','24698','25011','24099','23368'), 
    ('Riots','167','252','258','261','154','166','253','259','157'), 
    ('Sexualharrassment','35','38','41','33','36','39','32','31','29'),
    ('Kiddnapping','6181','5184','5187','5174','5192','5868','5365','6462','6247'),
    ('Rape','3870','4167','4468','3779','3663','4066','3953','4599','3855'), 
    ('Murder','4088','3744','3260','2932','2712','2214','2539','2711','2897')
    ]
mycursor.executemany(sql, val)
mydb.commit()
mycursor.execute("Select Year2011,Year2012,Year2013,Year2014,Year2015,Year2016,Year2017,Year2018,Year2019 from up_crimes where crimes='Theft'")
a=myresult= mycursor.fetchall()
print('Crime', '2011', '2012', '2013', '2014','2015','2016','2017','2018','2019')
for p in a:
    print(p)

mycursor.execute("Select Year2011,Year2012,Year2013,Year2014,Year2015,Year2016,Year2017,Year2018,Year2019 from up_crimes where crimes='Robbery'")
b=myresult= mycursor.fetchall()
print('Crime', '2011', '2012', '2013', '2014','2015','2016','2017','2018','2019')
for q in b:
    print(q)
mycursor.execute("Select Year2011,Year2012,Year2013,Year2014,Year2015,Year2016,Year2017,Year2018,Year2019 from up_crimes where crimes='Burglary'")
c=myresult= mycursor.fetchall()
print('Crime', '2011', '2012', '2013', '2014','2015','2016','2017','2018','2019')
for r in c:
    print(r)
mycursor.execute("Select Year2011,Year2012,Year2013,Year2014,Year2015,Year2016,Year2017,Year2018,Year2019 from up_crimes where crimes='Riots'")
d=myresult= mycursor.fetchall()
print('Crime', '2011', '2012', '2013', '2014','2015','2016','2017','2018','2019')
for s in d:
    print(s)

mycursor.execute("Select Year2011,Year2012,Year2013,Year2014,Year2015,Year2016,Year2017,Year2018,Year2019 from up_crimes where crimes='Sexualharrassment'")
e=myresult= mycursor.fetchall()
print('Crime', '2011', '2012', '2013', '2014','2015','2016','2017','2018','2019')
for t in e:
    print(t)
mycursor.execute("Select Year2011,Year2012,Year2013,Year2014,Year2015,Year2016,Year2017,Year2018,Year2019 from up_crimes where crimes='Kiddnapping'")
f=myresult= mycursor.fetchall()
print('Crime', '2011', '2012', '2013', '2014','2015','2016','2017','2018','2019')
for u in f:
    print(u)
mycursor.execute("Select Year2011,Year2012,Year2013,Year2014,Year2015,Year2016,Year2017,Year2018,Year2019 from up_crimes where crimes='Rape'")
g=myresult= mycursor.fetchall()
print('Crime', '2011', '2012', '2013', '2014','2015','2016','2017','2018','2019')
for v in g:
    print(v)
mycursor.execute("Select Year2011,Year2012,Year2013,Year2014,Year2015,Year2016,Year2017,Year2018,Year2019 from up_crimes where crimes='Murder'")
h=myresult= mycursor.fetchall()
print('Crime', '2011', '2012', '2013', '2014','2015','2016','2017','2018','2019')
for w in h:
    print(w)
plt.plot(m,p,'seagreen', label='Theft')
plt.plot(m,q,'rosybrown',label='Robbery')
plt.plot(m,r,'lightcoral',label='Burglary')
plt.plot(m,s,'lightslategrey',label='Riots')
plt.plot(m,t,'lime',label='Sexualharrasment')
plt.plot(m,u,'palevioletred',label='Kidnapping')
plt.plot(m,v,'gold',label='Rape')
plt.plot(m,w,'darkcyan',label='Murder')
plt.title('TOTAL CRIMES OF UTTAR PRADESH')
plt.legend()
plt.show()
def Theft():
    plt.plot(m,p,'seagreen',label='Theft')
    plt.title('Theft')
    plt.legend()
    plt.show()

def Robbery():
    plt.plot(m,q,'rosybrown',label='Robbery')
    plt.title('Robbery')
    plt.legend()
    plt.show()
    
def Burglary():
    plt.plot(m,r,'lightcoral',label='Burglary')
    plt.title('Burglary')
    plt.legend()
    plt.show()
def Riots():
    plt.plot(m,s,'lightslategrey',label='Riots')
    plt.title('Riots')
    plt.legend()
    plt.show()
def Sexualharrassment():
    plt.plot(m,t,'lime',label='Sexualharrasment')
    plt.title('Sexual harrassment')
    plt.legend()
    plt.show()
def Kiddnapping():
    plt.plot(m,u,'palevioletred',label='Kidnapping')
    plt.title('Kiddnapping')
    plt.legend()
    plt.show()
def Rape():
    plt.plot(m,v,'gold',label='Rape')
    plt.title('Rape')
    plt.legend()
    plt.show()
def Murder():
    plt.plot(m,w,'darkcyan',label='Murder')
    plt.title('Murder')
    plt.legend()
    plt.show()
window1 = Tk()
window1.title("CRIME RATE ANALYSIS") 
window1.geometry('350x200') 
lbl = Label(window1, text='''SELECT A CRIME TO VIEW THE GRAPH
RESPECTIVE TO THE CRIME ''') 
lbl.grid(column=0, row=0) 
btn1 = Button(window1, text="Theft",command=Theft,width=15)
btn2 = Button(window1, text="Robbery",command=Robbery,width=15)
btn3 = Button(window1, text="Burglary",command=Burglary,width=15)
btn4 = Button(window1, text="Riots",command=Riots,width=15)
btn5 = Button(window1, text="Sexualharrassment",command=Sexualharrassment,width=15)
btn6 = Button(window1, text="Kiddnapping",command=Kiddnapping,width=15)
btn7 = Button(window1, text="Rape",command=Rape,width=15)
btn8 = Button(window1, text="Murder",command=Murder,width=15)
btn1.grid(column=0, row=2)
btn2.grid(column=0, row=4)
btn3.grid(column=0, row=6)
btn4.grid(column=0, row=8)
btn5.grid(column=0, row=10)
btn6.grid(column=0, row=12)
btn7.grid(column=0, row=14)
btn8.grid(column=0, row=16)
window1.mainloop()




