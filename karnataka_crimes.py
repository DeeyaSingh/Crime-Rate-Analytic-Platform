from tkinter import *
import mysql.connector as mysqlc
import matplotlib.pyplot as plt
m=['2011','2012','2013','2014','2015','2016','2017','2018','2019']
mydb=mysqlc.connect(host='localhost',user='root',passwd='user123',database='mydatabase')
mycursor= mydb.cursor()
mycursor.execute("Drop table karnataka_crimes")
mycursor.execute("Create table karnataka_crimes(crimes char(50),year2011 int, year2012 int,year2013 int,year2014 int, year2015 int, year2016 int, year2017 int,year2018 int, year2019 int)")
sql= "insert into karnataka_crimes(crimes,year2011,year2012,year2013,year2014,year2015,year2016,year2017,year2018,year2019) values(%s, %s, %s, %s, %s,%s,%s,%s,%s,%s)"
val= [
    ('Theft','33025','32862','31653','31972','34183','33187','30196','32456','31787'),
    ('Robbery','3216' ,'5217','5977','5342','4988','3997','4876','4399','6011'),
    ('Burglary','13327','14223','13735','13844','14788','14698','15011','14099','13368'), 
    ('Riots','113','186','175','186','242','165','176','187','112'), 
    ('Sexualharrassment','95','222','185','98','89','136','189','193','217'),
    ('Kiddnapping','2400','2988','2807','2932','2388','2671','2743','2443','2165'),
    ('Rape','1864','2076','1902','1963','2109','2213','1966','2188','2096'), 
    ('Murder','2342','2778','3896','2864','3288','2156','2104','2405','2844')
    ]
mycursor.executemany(sql, val)
mydb.commit()
mycursor.execute("Select Year2011,Year2012,Year2013,Year2014,Year2015,Year2016,Year2017,Year2018,Year2019 from karnataka_crimes where crimes='Theft'")
a=myresult= mycursor.fetchall()
print('Crime', '2011', '2012', '2013', '2014','2015','2016','2017','2018','2019')
for p in a:
    print(p)

mycursor.execute("Select Year2011,Year2012,Year2013,Year2014,Year2015,Year2016,Year2017,Year2018,Year2019 from karnataka_crimes where crimes='Robbery'")
b=myresult= mycursor.fetchall()
print('Crime', '2011', '2012', '2013', '2014','2015','2016','2017','2018','2019')
for q in b:
    print(q)
mycursor.execute("Select Year2011,Year2012,Year2013,Year2014,Year2015,Year2016,Year2017,Year2018,Year2019 from karnataka_crimes where crimes='Burglary'")
c=myresult= mycursor.fetchall()
print('Crime', '2011', '2012', '2013', '2014','2015','2016','2017','2018','2019')
for r in c:
    print(r)
mycursor.execute("Select Year2011,Year2012,Year2013,Year2014,Year2015,Year2016,Year2017,Year2018,Year2019 from karnataka_crimes where crimes='Riots'")
d=myresult= mycursor.fetchall()
print('Crime', '2011', '2012', '2013', '2014','2015','2016','2017','2018','2019')
for s in d:
    print(s)

mycursor.execute("Select Year2011,Year2012,Year2013,Year2014,Year2015,Year2016,Year2017,Year2018,Year2019 from karnataka_crimes where crimes='Sexualharrassment'")
e=myresult= mycursor.fetchall()
print('Crime', '2011', '2012', '2013', '2014','2015','2016','2017','2018','2019')
for t in e:
    print(t)
mycursor.execute("Select Year2011,Year2012,Year2013,Year2014,Year2015,Year2016,Year2017,Year2018,Year2019 from karnataka_crimes where crimes='Kiddnapping'")
f=myresult= mycursor.fetchall()
print('Crime', '2011', '2012', '2013', '2014','2015','2016','2017','2018','2019')
for u in f:
    print(u)
mycursor.execute("Select Year2011,Year2012,Year2013,Year2014,Year2015,Year2016,Year2017,Year2018,Year2019 from karnataka_crimes where crimes='Rape'")
g=myresult= mycursor.fetchall()
print('Crime', '2011', '2012', '2013', '2014','2015','2016','2017','2018','2019')
for v in g:
    print(v)
mycursor.execute("Select Year2011,Year2012,Year2013,Year2014,Year2015,Year2016,Year2017,Year2018,Year2019 from karnataka_crimes where crimes='Murder'")
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
plt.title('TOTAL CRIMES OF KARNATAKA')
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
lbl = Label(window1, text='''SELECT A CRIME TO THE VIEW
THE RESPECTIVE GRAPH:''') 
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
btn2.grid(column=0, row=6)
btn3.grid(column=0, row=10)
btn4.grid(column=0, row=14)
btn5.grid(column=0, row=18)
btn6.grid(column=0, row=22)
btn7.grid(column=0, row=26)
btn8.grid(column=0, row=30)
window1.mainloop()


