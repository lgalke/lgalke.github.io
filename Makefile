all: site

site: _site/index.html _site/publications.html _site/bio.html _site/talks.html _site/lpag.css

_site/%.html: %.md metadata-file.yaml lpag.css
	mkdir -p _site
	pandoc -t html5 --metadata-file=metadata-file.yaml --css=lpag.css --standalone $< -o $@


_site/lpag.css: lpag.css
	cp lpag.css _site/lpag.css

clean:
	rm -rf _site


view: site
	open _site/index.html
