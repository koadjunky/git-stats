export PYTHONPATH=$PYTHONPATH:$PWD/src

nbstripout:
	nbstripout jupyter/*.ipynb

fetch:
	python src/fetch.py $(root)

data:
	python src/commits.py $(root)
