all: site


site: _site/index.html _site/publications.html _site/bio.html _site/talks.html


_site/%.html: %.md metadata-file.yaml
	pandoc -t html5 --metadata-file=metadata-file.yaml --standalone $< -o $@


view: site
	open _site/index.html
