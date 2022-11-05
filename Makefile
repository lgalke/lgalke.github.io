preview:
	quarto preview


public:
	quarto render
	git commit -am "Update"
	git add docs
	git push
