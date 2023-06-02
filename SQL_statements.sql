/*
Title: SQL Statements
Author: Natalie Eversole
Date: April 28th, 2022

Description: SQL statements used in PostgreSQL
*/

CREATE TABLE BusinessTable (
  business_id VARCHAR(30),
  name VARCHAR(100),
  address VARCHAR (100),
  city VARCHAR(100),
  state CHAR(2),
  postal_code CHAR(10),
  latitude FLOAT,
  longitude FLOAT,
  stars FLOAT,
  review_count VARCHAR(100000),
  is_open CHAR(1),
  PRIMARY KEY (business_id)
)

CREATE TABLE ReviewTable (
	review_id VARCHAR(30),
	user_id VARCHAR(30),
	business_id VARCHAR(30),
	stars CHAR(1),
	date DATE,
	text VARCHAR(10000000),
	useful BOOLEAN,
	funny BOOLEAN,
	cool BOOLEAN,
	PRIMARY KEY (review_id),
	FOREIGN KEY(business_id) REFRENCES business(business_id),
	FOREIGN KEY(user_id) REFRENCES User(user_id)
)

CREATE TABLE CheckInTable(
  business_id VARCHAR(30),
  dayofweek VARCHAR(9),
  hour TIME,
  count VARCHAR(1000),
  FOREIGN KEY(business_id) REFRENCES Business(business_id)
)

CREATE TABLE userTable (
	user_id VARCHAR(30),
	name VARCHAR(1000),
	yelping_since DATE,
	review_count CHAR(100000),
	fans CHAR(100000),
	average_stars FLOAT,
	useful CHAR(100000),
	funny CHAR(100000),
	cool CHAR(100000),
	PRIMARY KEY (user_id)
)

CREATE TABLE friendTable(
	user_id VARCHAR(30),
	friend VARCHAR(30)
)

CREATE TABLE BusinessCategoryTable(
  business_id VARCHAR(30),
  categories VARCHAR[]
)

CREATE TABLE zipcodeData (
  zipcode CHAR(10),
  medianIncome VARCHAR(1000000),
  meanIncome VARCHAR(1000000),
  population CHAR(1000000)
)

CREATE TABLE averagerating AS
SELECT business_id, AVG(stars)
FROM reviewtable;

SELECT business_id, AVG(stars)
FROM reviewtable
GROUP BY business_id;

CREATE TABLE review_count AS (SELECT business_id, COUNT(business_id) FROM reviewtable GROUP BY business_id);

ALTER TABLE review_count ALTER COLUMN review_count TYPE VARCHAR(1000)
