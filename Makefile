publish:
	quarto render
	git commit -am "Update"
	git push