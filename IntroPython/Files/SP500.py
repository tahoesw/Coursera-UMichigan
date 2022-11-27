import datetime
fileconnection = open("../data/SP500.txt", 'r')
lines = fileconnection.readlines()
n = 0
mean_SP = 0.0
max_interest = 0.0
header = lines[0]
field_names = header.strip().split(',')
print(field_names)
for row in lines[1:]:
    vals = row.strip().split(',')
    date_str = vals[0]
    format_str = '%m/%d/%Y'  # The format
    datetime_obj = datetime.datetime.strptime(date_str, format_str)
    date = str(datetime_obj.date())
    if date >= "2016-06-01" and date <= "2017-05-01":
        n += 1
        mean_SP += float(vals[1])
        if max_interest < float(vals[5]):
            max_interest = float(vals[5])
        if vals[5] != "NA":
            print("{}: {}; {}".format(vals[0], vals[1], vals[5]))
mean_SP /= n
print(mean_SP, max_interest)

