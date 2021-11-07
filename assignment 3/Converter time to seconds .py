# Convert time to seconds
time = list(input('Please enter your desired time: Example (12:59:59)').split(':'))

h = int(time[0])*3600
m = int(time[1])*60
s = int(time[2])

Convert = s + m + h   

print(Convert)