serve:
	pydocmd serve
build:
	pydocmd build
	@make _build/site/img/favicon.ico
deploy: build
	git add --all _build/site/
	git commit -m "update static site"
	git push -f origin `git subtree split --prefix _build/site/`:master
clean:
	rm -rf *.pyc _build/
_build/site/img/favicon.ico: ../logo.png
	convert "$<" -resize 16x16 "$@"
