import csv


def getDB (csv_file_name):
    DB = []
    with open(csv_file_name, 'r', encoding='utf-8', newline='') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        next(csv_reader, None)
        for row in csv_reader:
            if len(row) > 1:
                DB.append(row)
    return DB