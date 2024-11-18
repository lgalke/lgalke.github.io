s = """\

Name: Lukas Paul Achatius Galke

Position: Assistant Professor of Data Science and Advanced Machine Learning

Affiliation: 
University of Southern Denmark (SDU)
Department of Mathematics and Computer Science (IMADA), Section for Data Science and Statistics
Centre for Machine Learning

Research Interests: 
- Machine learning
- Natural language processing
- Machine communication
- Continual learning
- Learning on graphs

Email: galke@imada.sdu.dk

Website: https://lgalke.github.io/

## Bio

Since 2024, I am an Assistant Professor of Data Science and Advanced Machine Learning. Before that, I was a postdoctoral researcher at the Max Planck Institute for Psycholinguistics in Nijmegen, Netherlands. I've received my B.Sc. (2013), M.Sc. (2017), and PhD degree (2022), all in computer science, from Kiel University, Germany. My research interests lie in machine learning and natural language processing, aiming to make neural network models more interpretable and trustworthy.

## Profiles

- ORCID: [0000-0001-6124-1092](https://orcid.org/0000-0001-6124-1092)
- DBLP: [Lukas Galke](https://dblp.org/pid/200/7830.html)
- Google Scholar: [Lukas Galke](https://scholar.google.de/citations?hl=en&pli=1&user=AHGGdYQAAAAJ)
- GitHub: [lgalke](https://github.com/lgalke)
- Mastodon: [@lpag@sigmoid.social](https://sigmoid.social/@lpag)
- LinkedIn: [Lukas Galke](https://www.linkedin.com/in/lukas-galke-8086b0155/)
- BlueSky: [@lukasgalke.bsky.social](https://bsky.app/profile/lukasgalke.bsky.social)
- X (inactive): [@LukasGalke](https://x.com/LukasGalke)

"""


for file in ["cv.md", "projects.md", "publications.md", "talks.md", "teaching.md"]:
    with open(file, "r") as f:
        s += '\n\n'
        s += f.read()

with open("llms.txt", "w") as f:
    f.write(s)
