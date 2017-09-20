> docker run -it --rm jupyter/scipy-notebook python

has sqlalchemy, pandas, and requests
but not psycopg2
OK because using sqlite right now


run with:
`docker run -v $(pwd):/home/jovyan --rm jupyter/scipy-notebook python scrape.py`