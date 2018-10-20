PYDOCMD=PYTHONPATH=. pydocmd
serve:
	$(PYDOCMD) serve
build:
	$(PYDOCMD) build
	sed -ri 's/img\/favicon.ico/https:\/\/raw.githubusercontent.com\/tqdm\/tqdm\/master\/images\/logo.gif/' _build/site/index.html
deploy: build
	git checkout master
	cp -a _build/site/* .
	git add --all
	git commit -m "update static site"
	git push
	git checkout src
clean:
	rm -rf *.pyc _build/
