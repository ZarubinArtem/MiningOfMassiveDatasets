#

flat = "CS341 Project in Mining Massive Data Sets is an advanced project based course. Students work on data mining and machine learning algorithms for analyzing very large amounts of data. Both interesting big datasets as well as computational infrastructure (large MapReduce cluster) are provided by course staff. Generally, students first take CS246 followed by CS341."

d = {}
for i in flat.split(" "):
    i.rstrip(".")
    i.rstrip(",")
    if i not in d:
        d.setdefault(str(i), 1)
    else:
        pass
print(d)
