from datetime import datetime, timedelta
import random
import csv

num_days = 30
samples_per_day = 4
water_day = 5

data = {}
moisture = 500

for day in range(num_days):
    if day % water_day == 0 and day != 0:
        moisture -= random.randint(100, 400)

    time = datetime.now() + timedelta(days=day)
    
    for i in range(samples_per_day):
        moisture += random.randint(5, 20) 
        time = time + timedelta(hours=6)
        data.update({time.isoformat():moisture})


header = ['Timestamp', 'Resistance']
with open('moisture_data.csv', 'w', newline='') as fn:
    writer = csv.writer(fn)
    writer.writerow(header)
    
    for timestamp, value in data.items():
        row = [timestamp, value]
        writer.writerow(row)