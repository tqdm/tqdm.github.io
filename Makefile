.PHONY: serve build deploy clean
PYDOCMD=pydoc-markdown
serve:
	$(PYDOCMD) -s -o
build:
	GITHUB_API_TOKEN='' python ../wiki/releases.py tqdm/tqdm -o sources/releases.md -d ext
	$(PYDOCMD) --build --site-dir _site
	sed -ri 's/img\/favicon.ico/https:\/\/raw.githubusercontent.com\/tqdm\/tqdm\/master\/images\/logo.gif/' build/docs/_site/index.html
	cp .README.md build/docs/_site/README.md
deploy: build
	git checkout master
	cp -a build/docs/_site/* .
	echo -e '/build/\n/sources/' > .gitignore
	git add --all
	git commit -m "update static site"
	git push
	git checkout src
	git branch -d master
clean:
	rm -rf *.pyc sources/releases.md build/
