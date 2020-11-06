import pandas as pd

def write_text(i, j, param):
    global output_file
    output_file.write(2*"\t"+"Rectangle {\n")
    output_file.write(3*"\t"+"id: rectangle"+str(i)+str(j)+"\n")
    output_file.write(3*"\t"+"x: "+str(i)+"\n")
    output_file.write(3*"\t"+"y: "+str(j)+"\n")
    output_file.write(3 * "\t" + "width: 50"+"\n")
    output_file.write(3 * "\t" + "height: 50"+"\n")
    output_file.write(3 * "\t" + "color: \"#cc5a5a\" "+"\n")
    output_file.write(3 * "\t" + "radius: 2"+"\n")
    output_file.write(3 * "\t" + "border.color: \"#4e1010\""+"\n")
    output_file.write(3 * "\t" + "border.width: 2"+"\n")
    output_file.write(2 * "\t" + "}" + "\n")


def write_box(i, j, param):
    pass


input_filename = "primers_cross.csv"
output_filename = "cross.qml"
output_file = open(output_filename, "w")

matrix = pd.read_csv(input_filename, delimiter=';').values.tolist()
size = len(matrix)

# init section

output_file.write("import QtQuick 2.15 \n")
output_file.write("import QtQuick.Window 2.15 \n")
output_file.write("import QtQuick.Controls 2.15 \n")
output_file.write("import QtQuick.Templates 2.15 \n")
output_file.write("import QtQuick.Controls.Universal 2.0 \n\n")
output_file.write("Window { \n")
output_file.write("width: 640 \n")
output_file.write("height: 480 \n")
output_file.write("visible: true \n")
output_file.write("title: \"Cross Matrix\" \n")

for i in range(size):
    for j in range(size):
        write_box(i,j,matrix[i][j])
        write_text(i,j,matrix[i][j])

output_file.write("}")
