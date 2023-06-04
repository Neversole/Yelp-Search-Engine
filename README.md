# Yelp Review Search Engine
-------------------------

This repo contains a project that was completed in the early years of my studies. This project uses Yelp business and review metadata to produce a graphical user interface search engine. The user interface enables users to view details about Yelp business after selecting a business category or a state, city and/or zip code.

-------------------------

# Files
### Data Folder
* yelp_business.JSON - Contains information about the business on Yelp such as business ID, business name, city, state, zipcode, number of stars, and number of reviews.
* yelp_review.JSON - Contains information regarding Yelp reviews such as review ID, business ID, user ID, star rating given, date of review, and the text of the review.
* yelp_user.JSON - Contains information on Yelp users such as uer ID, user name, number of reviews provided, number of fans, average star rating.

### ParseAndInsert.py
This code parses JSON files and inserts the data into the PostgresSQL database.

### SQL_statements.sql
The SQL statements used in PostgreSQL to create and alter the data tables.

### Seach_Engine_App.py
This code creates the application for the search engine using Python and PyQt.







version https://git-lfs.github.com/spec/v1
oid sha256:4740516364b39d7013729c02dc8d0db457438f1a54c88b77d47457e2526e2285
size 21
