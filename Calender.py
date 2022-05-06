import tkinter
from tkinter import font
from tkinter.ttk import Button

year=2022
month=5

def cal(year,month):
    month_days=[31,28,31,30,31,30,31,31,30,31,30,31]
    month_days_leap=[31,29,31,30,31,30,31,31,30,31,30,31]
    #Day_Name=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    day_count=1
    leap_flag=0
    init_year=1901
    while init_year<year+1:
        leap_flag=0
        if init_year%4==0:               #leap_flag check
            if init_year%100==0:
                if init_year%400==0:
                    leap_flag=1
                else:
                    leap_flag=0
            else:
                leap_flag=1

        if leap_flag==0:
            for i in month_days:
                day_count+=i
                day_count%=7
        else:
            for i in month_days_leap:
                day_count+=i
                day_count%=7
        
        init_year+=1
    i=0
    if leap_flag == 0:
        while i < month-1:
            day_count=(day_count+month_days[i])%7
            i+=1
    else:
        while i < month-1:
            day_count=(day_count+month_days_leap[i])%7
            i+=1
    if leap_flag == 0:
        return(day_count)
    elif day_count==0:
        return(6)
    else:
        return(day_count-1)

def mon_prev():
    global month
    global year
    if month==1:
        month=12
        year-=1
    else:
        month-=1
def mon_nex():
    global month
    global year
    if month==12:
        month=1
        year+=1
    else:
        month+=1




def tin():
    global month
    global year
    top = tkinter.Tk(className='Calender')
    top.configure(background='#222222')
    
    ft1 = font.Font(family='Ariel', size=14, slant='italic' )
    ft2 = font.Font(family='Ariel', size=11, weight='bold' ,slant='italic' )
    ft3 = font.Font(family='Ariel', size=11, weight='bold' )

    year_new=tkinter.StringVar()

    def refp():
        mon_prev()
        top.destroy()
        tin()
    def refn():
        mon_nex()
        top.destroy()
        tin()

    def go_to():
        global year
        y1=year_new.get()
        if str.isdigit(y1):
            y1=int(y1)
            if y1>1901:
                year=y1
                top.destroy()
                tin()

    def ui():
        left.grid(row=0,column=0, padx=3,pady=3)
        month_button.grid(row=0, column=1, columnspan=3,padx=3,pady=3)
        year_button.grid(row=0, column=4, columnspan=2,padx=3,pady=3)
        right.grid(row=0, column=6, padx=3,pady=3)

        goto.grid(row=1, columnspan=3)
        year_en=tkinter.Entry(top, textvariable=year_new, bg='#111111', bd=0, font=ft1, fg='white')
        year_en.grid(row=1, column=3,columnspan=3)
        check.grid(row=1, column=6)

        





        for a in day:
            a.grid(row=2,column=day.index(a),padx=3,pady=3)
        print(count)
        for b in range(6-count,len(blocks)):
            blocks[b].grid(row=3+int((count-6+b)/7),column=(count+b-6)%7,padx=3,pady=3)





    Days=['Sun','Mon','Tues','Wed','Thurs','Fri','Sat']
    Months=['January','February','March','April','May','June','July','August','September','October','November','December']
    day=[tkinter.Button(text=i, activebackground='#560000', activeforeground='white',width=5 , background= '#680000', foreground='#AAAAAA',font=ft2 , state=tkinter.DISABLED) for i in Days]
    dates=[tkinter.Button(text=i, activebackground='#555555', width=5, background='#111111', foreground='#BBBBBB', font=ft3) for i in range(1,32)]
    blank=[tkinter.Button(text=' ',background='#222222' ,activebackground='#222222' , width=5, borderwidth=0, relief='solid', state=tkinter.DISABLED) for i in range(1,7)]
    blocks=blank+dates
    count=cal(year,month)           #days left from previous month
    left=tkinter.Button(text='<<',font=ft3 ,activebackground='#222222', activeforeground='white',width=5 , background= '#333333' , foreground='#999999' , command=refp)
    right=tkinter.Button(text='>>',font=ft3, activebackground='#222222', activeforeground='white',width=5 , background= '#333333' , foreground='#999999', command=refn)
    month_button=tkinter.Button(text=Months[month-1], activebackground='#222222', activeforeground='white', background= '#111111' , foreground='#999999', font=ft1, width=17)
    year_button=tkinter.Button(text=year, activebackground='#222222', activeforeground='white', background= '#111111' , foreground='#999999', font=ft1, width= 10 )
    goto=tkinter.Label(top, text="Go To Year:")
    goto.config(font=('',14),background='#222222', foreground='#999999')
    check=tkinter.Button(text="Check", command=go_to,activebackground='#222222', activeforeground='white',background= '#333333' , foreground='#999999' )
    ui()    
        
    top.mainloop()

tin()