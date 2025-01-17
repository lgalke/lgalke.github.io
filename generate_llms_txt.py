s = "# Lukas Paul Achatius Galke"

for file in ["about.md", "cv.md", "projects.md", "publications.md", "talks.md", "teaching.md"]:
    with open(file, "r") as f:
        s += '\n\n'
        s += f.read()

with open("llms.txt", "w") as f:
    f.write(s)
