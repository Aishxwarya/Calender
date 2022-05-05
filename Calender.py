import tkinter

year=2022
month=5

def cal(year,month):
    month_days=[31,28,31,30,31,30,31,31,30,31,30,31]
    month_days_leap=[31,29,31,30,31,30,31,31,30,31,30,31]
    Day_Name=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
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

    
    loop=0
    global month
    global year
    top = tkinter.Tk(className='Calender')
    top.configure(background='#222222')
    def refp():
        mon_prev()
        top.destroy()
        tin()
    def refn():
        mon_nex()
        top.destroy()
        tin()
    def ui():
        left.grid(row=0,column=0, padx=3,pady=3)
        month_button.grid(row=0, column=1, columnspan=3,padx=3,pady=3)
        year_button.grid(row=0, column=4, columnspan=2,padx=3,pady=3)
        right.grid(row=0, column=6, padx=3,pady=3)


        for a in day:
            a.grid(row=1,column=day.index(a),padx=3,pady=3)

        for b in range(6-count,len(blocks)):
            blocks[b].grid(row=2+int((count-6+b)/7),column=(count+b-6)%7,padx=3,pady=3)





    Days=['Sun','Mon','Tues','Wednes','Thurs','Fri','Satur']
    Months=['January','February','March','April','May','June','July','August','September','October','November','December']
    day=[tkinter.Button(text=i, activebackground='#560000', activeforeground='white',width=5 , background= '#680000', foreground='#AAAAAA', state=tkinter.DISABLED) for i in Days]
    dates=[tkinter.Button(text=i, activebackground='#B0B0AF', width=5, background='#555555', foreground='#BBBBBB') for i in range(1,32)]
    blank=[tkinter.Button(text=' ',background='#222222' ,activebackground='#222222' , width=5, borderwidth=0, relief='solid', state=tkinter.DISABLED) for i in range(1,7)]
    blocks=blank+dates
    count=cal(year,month)           #days left from previous month
    left=tkinter.Button(text='<<', activebackground='#222222', activeforeground='white',width=5 , background= '#333333' , foreground='#999999' , command=refp)
    right=tkinter.Button(text='>>', activebackground='#222222', activeforeground='white',width=5 , background= '#333333' , foreground='#999999', command=refn)
    month_button=tkinter.Button(text=Months[month-1], activebackground='#222222', activeforeground='white',width=25 , background= '#111111' , foreground='#999999' )
    year_button=tkinter.Button(text=year, activebackground='#222222', activeforeground='white',width=15 , background= '#111111' , foreground='#999999' )
    
    
    ui()    
        
    top.mainloop()

tin()