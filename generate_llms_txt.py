import yaml

# Load config
with open("_config.yml", "r") as f:
    config = yaml.safe_load(f)

# Extract relevant fields
title = config.get("title", "")
tagline = config.get("tagline", "")
description = config.get("description", "").replace("<br/>", ", ").strip()
mission = config.get("mission", "").strip()
url = config.get("url", "")

# Build header from config
s = f"# {title}\n\n"
s += f"> {tagline}\n\n"
s += f"{description}\n\n"
s += f"**Mission:** {mission}\n\n"
s += f"**Website:** {url}\n"

# Append content from markdown files
for file in [ "cv.md", "projects.md", "publications.md", "talks.md", "teaching.md", "about.md",]:
    with open(file, "r") as f:
        s += '\n\n'
        s += f.read()

with open("llms.txt", "w") as f:
    f.write(s)
