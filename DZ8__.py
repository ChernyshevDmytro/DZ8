from datetime import datetime, timedelta

def get_birthdays_per_week(users):
    happy_birthday=dict()
    
    current_time=datetime.now()
    #current_time=datetime(year=2022, month=2, day=15)
    day = [timedelta(days=i) for i in range(5-current_time.weekday(),  12-current_time.weekday())]
    #print(day)
    for k,v in users.items():        
        for i in day:
            #print(f'i{i}')

            if v.month==(current_time+i).month and v.day==(current_time+i).day:
                       
                if happy_birthday.get(f"{(current_time+i).strftime('%A')}: ") is None:
                    happy_birthday[f"{(current_time+i).strftime('%A')}: "] =f'{k}, '
                
                else: happy_birthday[f"{(current_time+i).strftime('%A')}: "]+=f'{k} '
               
    for k,v in happy_birthday.items():
        if k == 'Saturday: ':
            happy_birthday['Monday: ']+=f'{v},'
            
        if k == 'Sunday: ':
            happy_birthday['Monday: ']+=f'{v},'
            

    del(happy_birthday['Saturday: '])
    del(happy_birthday['Sunday: '])

    for k,v in happy_birthday.items():
        print(f'{k},{v}')
  
users_0= {f'Vasya_{i}': datetime(year=2012, month=2, day=i) for i in range(1, 29)}
users_1= {f'Tanya_{i}': datetime(year=2012, month=2, day=i) for i in range(1, 29)}
users=dict(users_1)
users.update(users_0)


get_birthdays_per_week(users)

