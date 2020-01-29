# Given a dictionary of how many questions a person 
# has completed of each difficulty, return how many experience points they'll have.

# Create a function that sums a indiividuals exp.
# Input(s): Dictionary
# return: Count (string+XP) ex. "450XP"

def get_xp(d):
	XPsum = 0
	multiplyer = 5
	for points in d.values():
		val = points*multiplyer
		XPsum+= val
		multiplyer*=2

	# XPsum = 0
	# XPsum+= (d.get("Very Easy")*5)
	# XPsum+= (d.get("Easy")*10)
	# XPsum+= (d.get("Medium")*20)
	# XPsum+= (d.get("Hard")*40)
	# XPsum+= (d.get("Very Hard")*80)


	return(str(XPsum)+"XP")

d1 = {
  "Very Easy" : 89,
  "Easy" : 77,
  "Medium" : 30,
  "Hard" : 4,
  "Very Hard" : 1
}

d2 = {
  "Very Easy" : 254,
  "Easy" : 32,
  "Medium" : 65,
  "Hard" : 51,
  "Very Hard" : 34
  }

d3 = {
  "Very Easy" : 11,
  "Easy" : 0,
  "Medium" : 2,
  "Hard" : 0,
  "Very Hard" : 27
}

print(get_xp(d1))