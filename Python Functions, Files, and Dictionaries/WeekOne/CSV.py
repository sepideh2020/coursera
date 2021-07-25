file_connection = open('SalesJan2009.csv', 'r')
lines = file_connection.readlines()
header = lines[0]
fields_name = header.strip().split(',')[0:3]
print(fields_name)
for line in lines[1:]:
    vals = line.strip().split(',')
    if vals[2] != 'Visa':
        print("{}: {}; {}".format(
            vals[0],
            vals[1],
            vals[2]))

# writing in to a CSV file
olympian = [("John Aalberg", "31," "Cross Country Skiing"),
             ("Minna Maarit Aalto", '30', "Sailing"),
             ("Win Valdemar Aaltonen"," 54", "Art Competitions"),
             ("Wakako Abe", 18, "Cycling")]

outfile = open("reduced_olympics.csv", "w")
outfile.write('Name,Age,Sport')
outfile.write('\n')
for line in olympian:
    row_string = '{},{},{}'.format(olympian[0], olympian[1], olympian[2])
    # row_string = ','.join([olympians[0], olympians[1], olympians[2]])  # age must be str #does not work with join
    outfile.write(row_string)
    outfile.write('\n')
outfile.close()


olympians = [("John Aalberg", 31, "Cross Country Skiing, 15KM"),
             ("Minna Maarit Aalto", 30, "Sailing"),
             ("Win Valdemar Aaltonen", 54, "Art Competitions"),
             ("Wakako Abe", 18, "Cycling")]

outfile = open("reduced_olympics2.csv", "w")
# output the header row
outfile.write('"Name","Age","Sport"')
outfile.write('\n')
# output each of the rows:
for olympian in olympians:
    row_string = '"{}", "{}", "{}"'.format(olympian[0], olympian[1], olympian[2])
    outfile.write(row_string)
    outfile.write('\n')
outfile.close()
