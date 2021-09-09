import tkinter as tk
from tkinter import Menu
from tkinter import ttk
import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
lotto=[]
dates=[]
URL='https://www.lotto.net/canada-lotto-max/numbers/2020'
response =requests.get(URL)
soup=BeautifulSoup(response.content, 'html.parser')

columns=['num1','num2','num3','num4','num5','num6','num7','Bonus']

df=pd.DataFrame(columns=columns)

datetable=soup.find_all('div', attrs={'class':'date'})
table=soup.find_all('div', attrs={'class':'row-2'})
table1=soup.find_all('ul', attrs={'class':'balls'})
for i in table1:
    li_s=i.find_all('span')
    row=[span.text.replace('\n','') for span in li_s]
    df=df.append(pd.Series(row, index=columns), ignore_index=True)

datetable=soup.find_all('div', attrs={'class':'date'})
    
for i in datetable:
    dates.append((i.text).strip())

URL='https://www.lotto.net/canada-lotto-max/numbers/2019'
response =requests.get(URL)
soup=BeautifulSoup(response.content, 'html.parser')


table=soup.find_all('div', attrs={'class':'row-2'})
table1=soup.find_all('ul', attrs={'class':'balls'})
for i in table1:
    li_s=i.find_all('span')
    row=[span.text.replace('\n','') for span in li_s]
    df=df.append(pd.Series(row, index=columns), ignore_index=True)
datetable=soup.find_all('div', attrs={'class':'date'})
    
for i in datetable:
    dates.append((i.text).strip())
    
URL='https://www.lotto.net/canada-lotto-max/numbers/2018'
response =requests.get(URL)
soup=BeautifulSoup(response.content, 'html.parser')


table=soup.find_all('div', attrs={'class':'row-2'})
table1=soup.find_all('ul', attrs={'class':'balls'})
for i in table1:
    li_s=i.find_all('span')
    row=[span.text.replace('\n','') for span in li_s]
    df=df.append(pd.Series(row, index=columns), ignore_index=True)
datetable=soup.find_all('div', attrs={'class':'date'})
    
for i in datetable:
    dates.append((i.text).strip())

URL='https://www.lotto.net/canada-lotto-max/numbers/2017'
response =requests.get(URL)
soup=BeautifulSoup(response.content, 'html.parser')


table=soup.find_all('div', attrs={'class':'row-2'})
table1=soup.find_all('ul', attrs={'class':'balls'})
for i in table1:
    li_s=i.find_all('span')
    row=[span.text.replace('\n','') for span in li_s]
    df=df.append(pd.Series(row, index=columns), ignore_index=True)
datetable=soup.find_all('div', attrs={'class':'date'})
    
for i in datetable:
    dates.append((i.text).strip())

URL='https://www.lotto.net/canada-lotto-max/numbers/2016'
response =requests.get(URL)
soup=BeautifulSoup(response.content, 'html.parser')


table=soup.find_all('div', attrs={'class':'row-2'})
table1=soup.find_all('ul', attrs={'class':'balls'})
for i in table1:
    li_s=i.find_all('span')
    row=[span.text.replace('\n','') for span in li_s]
    df=df.append(pd.Series(row, index=columns), ignore_index=True)
datetable=soup.find_all('div', attrs={'class':'date'})
    
for i in datetable:
    dates.append((i.text).strip())

URL='https://www.lotto.net/canada-lotto-max/numbers/2015'
response =requests.get(URL)
soup=BeautifulSoup(response.content, 'html.parser')


table=soup.find_all('div', attrs={'class':'row-2'})
table1=soup.find_all('ul', attrs={'class':'balls'})
for i in table1:
    li_s=i.find_all('span')
    row=[span.text.replace('\n','') for span in li_s]
    df=df.append(pd.Series(row, index=columns), ignore_index=True)
datetable=soup.find_all('div', attrs={'class':'date'})
    
for i in datetable:
    dates.append((i.text).strip())

URL='https://www.lotto.net/canada-lotto-max/numbers/2014'
response =requests.get(URL)
soup=BeautifulSoup(response.content, 'html.parser')


table=soup.find_all('div', attrs={'class':'row-2'})
table1=soup.find_all('ul', attrs={'class':'balls'})
for i in table1:
    li_s=i.find_all('span')
    row=[span.text.replace('\n','') for span in li_s]
    df=df.append(pd.Series(row, index=columns), ignore_index=True)
datetable=soup.find_all('div', attrs={'class':'date'})
    
for i in datetable:
    dates.append((i.text).strip())

URL='https://www.lotto.net/canada-lotto-max/numbers/2013'
response =requests.get(URL)
soup=BeautifulSoup(response.content, 'html.parser')


table=soup.find_all('div', attrs={'class':'row-2'})
table1=soup.find_all('ul', attrs={'class':'balls'})
for i in table1:
    li_s=i.find_all('span')
    row=[span.text.replace('\n','') for span in li_s]
    df=df.append(pd.Series(row, index=columns), ignore_index=True)
datetable=soup.find_all('div', attrs={'class':'date'})
    
for i in datetable:
    dates.append((i.text).strip())

URL='https://www.lotto.net/canada-lotto-max/numbers/2012'
response =requests.get(URL)
soup=BeautifulSoup(response.content, 'html.parser')


table=soup.find_all('div', attrs={'class':'row-2'})
table1=soup.find_all('ul', attrs={'class':'balls'})
for i in table1:
    li_s=i.find_all('span')
    row=[span.text.replace('\n','') for span in li_s]
    df=df.append(pd.Series(row, index=columns), ignore_index=True)
datetable=soup.find_all('div', attrs={'class':'date'})
    
for i in datetable:
    dates.append((i.text).strip())
    
URL='https://www.lotto.net/canada-lotto-max/numbers/2011'
response =requests.get(URL)
soup=BeautifulSoup(response.content, 'html.parser')


table=soup.find_all('div', attrs={'class':'row-2'})
table1=soup.find_all('ul', attrs={'class':'balls'})
for i in table1:
    li_s=i.find_all('span')
    row=[span.text.replace('\n','') for span in li_s]
    df=df.append(pd.Series(row, index=columns), ignore_index=True)
datetable=soup.find_all('div', attrs={'class':'date'})
    
for i in datetable:
    dates.append((i.text).strip())
    
URL='https://www.lotto.net/canada-lotto-max/numbers/2010'
response =requests.get(URL)
soup=BeautifulSoup(response.content, 'html.parser')


table=soup.find_all('div', attrs={'class':'row-2'})
table1=soup.find_all('ul', attrs={'class':'balls'})
for i in table1:
    li_s=i.find_all('span')
    row=[span.text.replace('\n','') for span in li_s]
    df=df.append(pd.Series(row, index=columns), ignore_index=True)
datetable=soup.find_all('div', attrs={'class':'date'})
    
for i in datetable:
    dates.append((i.text).strip())

URL='https://www.lotto.net/canada-lotto-max/numbers/2009'
response =requests.get(URL)
soup=BeautifulSoup(response.content, 'html.parser')


table=soup.find_all('div', attrs={'class':'row-2'})
table1=soup.find_all('ul', attrs={'class':'balls'})
for i in table1:
    li_s=i.find_all('span')
    row=[span.text.replace('\n','') for span in li_s]
    df=df.append(pd.Series(row, index=columns), ignore_index=True)
datetable=soup.find_all('div', attrs={'class':'date'})
    
for i in datetable:
    dates.append((i.text).strip())
df['Dates']=dates

df.to_csv('LOTTOMAX archive.csv', index=False)

#------------------------------------------------------------------------------

def exit_():
    window.quit()
    window.destroy()
    exit()


def populate_gui(stringname):       
    numb1.set(str(df[['num1','num2','num3','num4','num5','num6','num7','Bonus']].loc[df.Dates==str(stringname)].values)[3:-3])

def count_sequence(ct):
    stquote=('Sequence Played Count: {}'.format(ct))
    samenum1.set(stquote)
    


window=tk.Tk()
window.title('Lotto Max')

menuBar=Menu()
window.config(menu=menuBar)

#Add menu items
fileMenu=Menu(menuBar, tearoff=0)
fileMenu.add_command(label="New")
fileMenu.add_separator()
fileMenu.add_command(label='Exit', command=exit_)
menuBar.add_cascade(label='File', menu=fileMenu)

helpMenu = Menu(menuBar, tearoff=0)
helpMenu.add_command(label="About")
menuBar.add_cascade(label="Help", menu=helpMenu)

tabControl=ttk.Notebook(window)
tab1=ttk.Frame(tabControl)
tabControl.add(tab1,text='Archive')

tab2=ttk.Frame(tabControl)
tabControl.add(tab2,text='Averages')

tab3=ttk.Frame(tabControl)
tabControl.add(tab3,text='# Chart')
tabControl.pack(expand=1, fill="both")


listofdates=ttk.LabelFrame(tab1,text='Dates')
listofdates.grid(column=0, row=1, padx=8, pady=4)
large_width=40
ENTRY_WIDTH=29
smallentry=7
#Sets up the Day combobox in col 0 row 0
# Sets up readonly for input in col 1 and row1
ttk.Label(listofdates,text='Day: ').grid(column=0, row=0, sticky='E')
numb1=tk.StringVar()
numb1Entry=ttk.Entry(listofdates, width=ENTRY_WIDTH, textvariable=numb1, state='readonly')
numb1Entry.grid(column=1, row=1, sticky='W')


#Takes samenum  text from box, turns string into an integer and performs function
ttk.Label(listofdates,text='Sequence(7 #s): ').grid(column=0, row=4, sticky='E')
samenum=tk.StringVar()
samenumEntry=ttk.Entry(listofdates, width=ENTRY_WIDTH, textvariable=samenum)
samenumEntry.grid(column=1, row=4, sticky='W')

samenum2=tk.IntVar()
samenum2Entry=ttk.Entry(listofdates, width=smallentry, textvariable=samenum2, state='readonly')
samenum2Entry.grid(column=4, row=1, sticky='W')
# Puts value into readonly box under Sequence 7
samenum1=tk.StringVar()
samenum1Entry=ttk.Entry(listofdates, width=ENTRY_WIDTH, textvariable=samenum1, state='readonly')
samenum1Entry.grid(column=1, row=5, sticky='W')

#Takes variable from Number Count box
ttk.Label(listofdates,text='Number Count: ').grid(column=3, row=0, sticky='E')
countnumber=tk.StringVar()
countnumberEntry=ttk.Entry(listofdates, width=smallentry, textvariable=countnumber)
countnumberEntry.grid(column=4, row=0, sticky='W')

#Puts value into readonly box under Count
putcount=tk.StringVar()
putcountEntry=ttk.Entry(listofdates, width=smallentry, textvariable=putcount, state='readonly')
putcountEntry.grid(column=4,row=1,sticky='W')


station_id = tk.IntVar()
station_id_combo = ttk.Combobox(listofdates, width=25, textvariable=station_id)    
station_id_combo['values'] = dates
station_id_combo.grid(column=1, row=0)
station_id_combo.current(0)


def _get_station():
    station = station_id_combo.get()
    populate_gui(station)

def _get_ifsame():
    u=df[['num1','num2','num3','num4','num5','num6','num7']].to_numpy().tolist()
    p=[]
    c=0
    used_num=samenum.get()
    l=used_num.split()
    for i in range(len(l)):
        p.append((int(l[i])))
    pp=[str(i) for i in p]
        
    for t in range(len(u)):
        if pp == u[t]:
            c += 1
    count_sequence(c)

#====================================================================================================s
def _get_countnumber():
    took=countnumber.get()
    if int(took) < 51 and int(took) > 0:
        lst1=list(range(1,51))
        ut=df[['num1','num2','num3','num4','num5','num6','num7']].to_numpy().tolist()
        counted=[]
        count=0
        w=1
        while w <= 50:
            for v in range(len(ut)):
                for t in range(0,7):
                    if ut[v][t] == str(w):
                        count += 1
            counted.append(count)
            w += 1
            count=0
        final=counted[int(took)-1]
        putcount.set(final)
    else:
        print('Lotto numbers are between 1 and 50')
#--------------------------------------------------------------------------------------------------

lst1=list(range(1,51))
ut=df[['num1','num2','num3','num4','num5','num6','num7']].to_numpy().tolist()
counted=[]
count=0
w=1
while w <= 50:
    for v in range(len(ut)):
        for t in range(0,7):
            if ut[v][t] == str(w):
                count += 1
    counted.append(count)
    w += 1
    count=0

dlist=counted

store2=0
store3=0
wasg=list(range(1,len(dlist)+1))

for j in range(0,len(dlist)):
    for i in range(len(dlist)):
        if i < len(dlist) -1:
            if dlist[i] < dlist[i+1]:
                store2=dlist[i]
                store3=wasg[i]
                dlist[i]=dlist[i+1]
                wasg[i]=wasg[i+1]
                dlist[i+1]=store2
                wasg[i+1]=store3

print(dlist)
print(wasg)

get_numbers_btn=ttk.Button(listofdates, text='Generate Numbers', command=_get_station).grid(column=2, row=0)
get_samecheck=ttk.Button(listofdates, text='Times Played', command=_get_ifsame).grid(column=2, row=4)
get_countnum=ttk.Button(listofdates, text='Count', command=_get_countnumber).grid(column=5, row=0)


window.mainloop()

