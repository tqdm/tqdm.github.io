serve:
	pydocmd serve
build:
	pydocmd build
	@make _build/site/img/favicon.ico
deploy: build
	git subtree push --prefix _build/site origin master
clean:
	rm -rf *.pyc _build/
_build/site/img/favicon.ico: ../logo.png
	convert "$<" -resize 16x16 "$@"
