import csv

def formatCSV(input_file):
    all_data = csv.reader(open(input_file)) # Here your csv file
    lines = list(all_data)

    for i in range(len(lines)):
        for j in range(4):
            if (i % 2 == 0):
                if (j == 0 and lines[i][j] == "1"):
                    lines[i][0] = "A"
                elif (j == 1 and lines[i][j] == "1"):
                    lines[i][0] = "B"
                elif (j == 2 and lines[i][j] == "1"):
                    lines[i][0] = "C"
                elif (j == 3 and lines[i][j] == "1"):
                    lines[i][0] = "D"
            if (i % 2 == 1):
                if (j == 0 and lines[i][j] == "1"):
                    lines[i][0] = "E"
                elif (j == 1 and lines[i][j] == "1"):
                    lines[i][0] = "F"
                elif (j == 2 and lines[i][j] == "1"):
                    lines[i][0] = "G"
                elif (j == 3 and lines[i][j] == "1"):
                    lines[i][0] = "H"

    for i in range(len(lines)):
        for j in range(3):
            lines[i][j+1] = ""

    writer = csv.writer(open('new_file.csv', 'w'))
    writer.writerows(lines)