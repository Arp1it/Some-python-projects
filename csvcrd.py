import csv

def create():
    with open("data.csv", "w", newline="") as obj:
        wobj = csv.writer(obj)

        wobj.writerow(["Roll no.", "Name", "Present"])
        wobj.writerow([1, "arpit", "yes"])


def read():
    with open("data.csv", "r") as obj:
        robj = csv.reader(obj)

        for ro in robj:
            print(ro)


create()
read()