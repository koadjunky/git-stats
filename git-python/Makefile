export PYTHONPATH=$PYTHONPATH:$PWD/src

nbstripout:
	nbstripout jupyter/*.ipynb

fetch:
	python src/fetch.py $(root)

pull:
	python src/pull.py $(root)

commits:
	python src/commits.py $(root) $(prefix)

survived:
	python src/survived.py $(root) $(prefix)

merge-commits:
	python src/merge_commits.py
