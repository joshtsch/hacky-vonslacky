<p align="center">
  <img width="200" height="200" src="./img/hacky.png">
</p>

# Hacktorious VonSlackbot

A slack bot programmed to provide updates on new and trending hackathon topics.

## Local Development

### Create/Activate virtualenv

`source bin/setup.sh`

### Install Dependencies

`python setup.py develop`

### Execute

`python src/hacky.py`

## Run Tests

This project uses pytest for executing tests

`python setup.py test`

## Todo

- Authentication (OAuth2)
- Refactor hacky.py
- Needs more test (any even)
- Add interactivity through slack commands
- Set up feed on a cron
