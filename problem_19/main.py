def is_leap_year( year ):
	if year%4 == 0 and year%100 != 0:
		return True
	elif year%100 == 0 and year%400 == 0:
		return True
	else:
		return False

def find_leap_years(start_year,end_year):
	
	years=[]
	for i in range( start_year, end_year+1 ):
		if is_leap_year(i):
			years.append((i,1))
		else:
			years.append((i,0))
	
	return years


def turn_years_to_days( years_array ):

	days=0
	for i in years_array:
		if i[1] == 0:
			days+=365
		else:
			days+=366
	days_array=[0]*days
	return days_array


def mark_day(day_start_index,days_array):
	for i in range( 0 , len(days_array)+1 , 7 ):
		days_array[i]+=1

#assumes the first month start is at index 0
def mark_month_start(years,days_array):
	
	index=0
	days_array[index]+=2
	for y in years:
		if y[1] == 1:
			days=[31,29,31,30,31,30,31,31,30,31,30,31]
		else:
			days=[31,28,31,30,31,30,31,31,30,31,30,31]
		
		for d in days:
			index+=d
			try:
				days_array[index]+=2
			except:
				return
			
		


def main():

	#find what day jan1 1901 is
	#1900 is clearly not a leap year
	years=find_leap_years(1900,1900)
	days=turn_years_to_days(years)
	mark_day(0,days)	
	#days.reverse() ##funny old thing BUT marking days in a year is mirrored from the middle!
	#print days.index(1) #it's 0 i.e. monday
	
	#new years day in 1901 is therefore tuesday
	#so sunday is (+5) ([tuesday[0]]wednesday[1],thursday[2],friday[3],saturday[4],Sunday[5])
	
	#create 1901->Dec 2000 days
	full_years=find_leap_years(1901,2000)
	full_days=turn_years_to_days(full_years)
	mark_day(5,full_days)
	mark_month_start(full_years,full_days)
	print full_days.count(3)

	




if __name__=="__main__":
	main()
