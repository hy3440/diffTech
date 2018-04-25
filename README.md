This is a django project hosted on heroku.

The database is hosted on Heorku, to access the database:
1. install heroku cli on your computer.
2. log in to Heorku account
3. open difftech
4. click Heorku Postgres
5. click Settings
6. under Settings, click view crendentials and copy the Heorku CLI command to paste on your cmd and run
7. then you will be connected to the database

Database description:
1. 'relations.txt' data is stored in the table djangotest_relations
2. 'tagpair_db.txt' data is stored in the table djangotest_tagpair
3. note that the database has a limit of 10000 rows for storage, so make sure you store them in the format of the existing rows in the database

To change the website:
1. html files is under templates
2. the logic and interaction with database is control by views
