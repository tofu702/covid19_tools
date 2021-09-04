#!/bin/bash

curl https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv > /tmp/us-states.csv

cd COVID-19
git pull
cd ..

python build_db_style_csv.py COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv /tmp/global_deaths.csv
