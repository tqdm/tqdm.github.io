.PHONY: serve build deploy clean
PYDOCMD=PYTHONPATH=. pydoc-markdown
serve:
	$(PYDOCMD) -s -o
build:
	$(PYDOCMD) --build --site-dir _site
deploy: build
	git checkout gh-pages
	git ls-files -z | xargs -0 git rm
	cp -a build/docs/_site/* .
	echo '/build/' > .gitignore
	echo '/sources/' >> .gitignore
	echo '*.pyc' >> .gitignore
	git add --all
	git commit -m "update static site"
	git push
	git checkout main
	git branch -d gh-pages
clean:
	rm -rf *.pyc sources/releases.md build/
