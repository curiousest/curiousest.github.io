import datetime
import pypandoc

base = open("0-minimum-viable-purpose.md", "r")

file_name = f"outputs/output-{datetime.date.today()}.md"
mvp = open(file_name, "w")

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
pypandoc.convert_file(file_name, 'docx', outputfile=file_name.replace(".md", ".docx"), extra_args = [
'-V',
'mainfont="Times New Roman"',
#'-f',
#'commonmark_x',
'--lua-filter',
'/Users/Douglas.Hindson/workspace/pagebreak/pagebreak.lua'
])

base.close()
mvp.close()
