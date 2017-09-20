`docker run -it --rm jupyter/scipy-notebook python`

this has sqlalchemy, pandas, and requests
but not psycopg2
OK because using sqlite right now


run with:
`docker run -v $(pwd):/home/jovyan --rm jupyter/scipy-notebook python scrape.py`

Actually that's been updated to `./run.sh`

Crontab installation:
`*/10 * * * * cd "/datadrive/citibike-stations-scraper" && ./run.sh;`