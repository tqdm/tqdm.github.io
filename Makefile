serve:
	pydocmd serve
build:
	pydocmd build
	@make _build/site/img/favicon.ico

_build/site/img/favicon.ico: ../logo.png
	convert "$<" -resize 16x16 "$@"
