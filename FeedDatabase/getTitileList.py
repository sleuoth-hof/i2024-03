import csv


def get_title_list(csv_file_name):
    title_list = []
    with open(csv_file_name, 'r', encoding='utf-8', newline='') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        next(csv_reader, None)
        try:
            for row in csv_reader:
                if len(row) > 1:
                    title_list.append(row[1])
        except:
            pass
    return title_list