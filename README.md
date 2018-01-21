cyberlog
========

Hi Hans, I made a docker/django hello-world app for you to play with.

## Instructions on what I did

* [setting up the container](https://docs.docker.com/compose/django/)

* [django hello world page](dfpp.readthedocs.io/en/latest/chapter_01.html)

## How to run it

### Install Docker

[download from here](https://www.docker.com/community-edition)

### Run It

Switch to this directory and run `docker-compose up`.   It should look something like this:

    watson:/src/cyberlog$ docker-compose up
    Starting cyberlog_db_1 ... done
    Starting cyberlog_web_1 ... done
    Attaching to cyberlog_db_1, cyberlog_web_1
    db_1   | 2018-01-21 01:06:23.896 UTC [1] LOG:  listening on IPv4 address "0.0.0.0", port 5432
    db_1   | 2018-01-21 01:06:23.896 UTC [1] LOG:  listening on IPv6 address "::", port 5432
    db_1   | 2018-01-21 01:06:23.899 UTC [1] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
    db_1   | 2018-01-21 01:06:23.913 UTC [23] LOG:  database system was interrupted; last known up at 2018-01-21 01:06:10 UTC
    db_1   | 2018-01-21 01:06:24.069 UTC [23] LOG:  database system was not properly shut down; automatic recovery in progress
    db_1   | 2018-01-21 01:06:24.071 UTC [23] LOG:  invalid record length at 0/1633C68: wanted 24, got 0
    db_1   | 2018-01-21 01:06:24.071 UTC [23] LOG:  redo is not required
    db_1   | 2018-01-21 01:06:24.081 UTC [1] LOG:  database system is ready to accept connections
    web_1  | Performing system checks...
    web_1  | 
    web_1  | System check identified no issues (0 silenced).
    web_1  | 
    web_1  | You have 14 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
    web_1  | Run 'python manage.py migrate' to apply them.
    web_1  | January 21, 2018 - 01:06:26
    web_1  | Django version 2.0.1, using settings 'cyberlog.settings'
    web_1  | Starting development server at http://0.0.0.0:8000/
    web_1  | Quit the server with CONTROL-C.

### Browse

Then browse to [http://localhost:8000](http://localhost:8000)

