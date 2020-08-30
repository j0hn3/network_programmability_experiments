import datetime 

def gen_timestamp():
#generate a timestamp in the format year-month-day-hour-minute-second
    now = datetime.datetime.now()
    now = now.strftime('%Y-%m-%d-%H-%M-%S')
    return now