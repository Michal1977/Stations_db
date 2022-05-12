import os


def import_data(csv_file):

    data = []
    if os.path.isfile(csv_file):
        with open(csv_file, "r") as content:
            for line in content:
                line = line.replace("\n", "")
                line = line.replace("\r", "")
                data.append(tuple(line.split(",")))
    else:
        print("File", csv_file, "does not exist!")

    return data




