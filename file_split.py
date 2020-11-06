name_in = "/Users/marek/primers/primers.csv"
name_out = "/Users/marek/primers/primers_train.csv"

start =2
stop = 1002

file_in = open(name_in, "r")
file_out = open(name_out, "w")

i = 0
while i < start-1:
    line = file_in.readline()
    i = i + 1

i = start-1
while i < stop:
    file_out.write(file_in.readline())
    i = i+1

file_in.close()
file_out.close()

