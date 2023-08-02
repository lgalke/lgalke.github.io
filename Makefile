preview:
	quarto preview


public:
	quarto render
	git add docs
	git commit -am "Update" && git push || echo "Nothing to do"
