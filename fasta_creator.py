name_in = "/Users/marek/primers/primers3_selected.csv"
name_out = "/Users/marek/primers/TF_test_data.fst"

file_in = open(name_in,"r")
file_out = open(name_out,"w")

for line in file_in:
    file_out.write(">\n")
    primer = line.split(";")[0]
    file_out.write(primer+"\n")

file_in.close()
file_out.close()


