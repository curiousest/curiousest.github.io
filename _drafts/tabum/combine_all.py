import datetime

base = open("0-minimum-viable-purpose.md", "r")

mvp = open(f"outputs/output-{datetime.date.today()}.md", "w")

def combine(f):
    for line in f.readlines():
        if line[0:2] == "[[":
            f2 = open(line[2:-3] + ".md", "r")
            combine(f2)
            f2.close()
        elif line[0] == "[": continue
        elif "## Notes" in line: return
        else:
            mvp.write(line)

combine(base)

base.close()
mvp.close()
