import calendar
m,d,y=map(int,input().split())
days={0:"MONDAY",1:"Tuesday",2:"Wednesday",3:"Thursday",4:"Friday",5:"Saturday",6:"SUNDAY"}
print(days[calendar.weekday(y,m,d)].upper())
