from faker import Factory
from random import randint

def create_data(fake):
	""""""
	print "patient_id,date,hour,minute,second,heart_rate,bp_systolic,bp_diastolic,drink_coffee,eating,sleeping,exercise"
	for i in range(3000):
		timestamp = str(fake.date_time_between(start_date="-30d", end_date="now"))
		hour = randint(0,23)
		minute = randint(0,59)
		second = randint(0,59)

		## coffee_time = ['07:1','07:2','07:3''07:4']
		coffee_time = ['07']
		sleeping_time = ['23','00','01','02','03','04','05']
		##eating_time = ['06','12','18']
		eating_time = ['06','12','18']
		exercise_time = ['20'] 
		
		drink_coffee = 0
		eating = 0
		sleeping = 0
		exercise = 0
		bp_systolic = randint(110,140)
		bp_diastolic = randint(75,85)
		
		# Normal heart rate
		bpm = randint(60,100)

		# Drink coffee time!
		if str(hour).zfill(2) in coffee_time:
			drink_coffee = 1
			# After drinking coffee heart rate 
			bpm = randint(110,160)
		# Sleeping time
		elif str(hour).zfill(2) in sleeping_time:
			sleeping = 1
			bpm = randint(50,65)
		elif str(hour).zfill(2) in eating_time:
			eating = 1
		elif str(hour).zfill(2) in exercise_time:
			exercise = 1
			bpm = randint(105,180)

 		print "1,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s" % (timestamp[0:10],str(hour).zfill(2),str(minute).zfill(2),str(second).zfill(2),bpm,bp_systolic,bp_diastolic,drink_coffee,eating,sleeping,exercise)
		
if __name__ == "__main__":
	fake = Factory.create()
	create_data(fake)
