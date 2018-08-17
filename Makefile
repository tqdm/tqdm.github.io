serve:
	pydocmd serve
build:
	pydocmd build
	sed -ri 's/img\/favicon.ico/https:\/\/raw.githubusercontent.com\/tqdm\/tqdm\/master\/images\/logo.gif/' _build/site/index.html
deploy: build
	git add --all _build/site/
	git commit -m "update static site"
	git push -f origin `git subtree split --prefix _build/site/`:master
clean:
	rm -rf *.pyc _build/
