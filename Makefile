.PHONY: serve build deploy clean
PYDOCMD=PYTHONPATH=. pydoc-markdown
serve:
	$(PYDOCMD) -s -o
sources/releases.md:
	GITHUB_API_TOKEN='' python ../wiki/releases.py tqdm/tqdm -o sources/releases.md -d ext
build: sources/releases.md
	$(PYDOCMD) --build --site-dir _site
	cp .README.md build/docs/_site/README.md
deploy: build
	git checkout master
	git ls-files | xargs git rm
	cp -a build/docs/_site/* .
	echo '/build/' > .gitignore
	echo '/sources/' >> .gitignore
	echo '*.pyc' >> .gitignore
	git add --all
	git commit -m "update static site"
	git push
	git checkout src
	git branch -d master
clean:
	rm -rf *.pyc sources/releases.md build/
