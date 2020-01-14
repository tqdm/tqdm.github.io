PYDOCMD=PYTHONPATH=. pydocmd
serve:
	$(PYDOCMD) serve
build:
	GITHUB_API_TOKEN='' python ../wiki/releases.py tqdm/tqdm -o sources/releases.md -d ext
	$(PYDOCMD) build
	sed -ri 's/img\/favicon.ico/https:\/\/raw.githubusercontent.com\/tqdm\/tqdm\/master\/images\/logo.gif/' _build/site/index.html
	cp .README.md _build/site/README.md
deploy: build
	git checkout master
	cp -a _build/site/* .
	git add --all
	git commit -m "update static site"
	git push
	git checkout src
	git branch -d master
clean:
	rm -rf *.pyc sources/releases.md _build/
