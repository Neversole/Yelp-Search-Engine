######################################################
# Title: Parse and Insert
# Author: Natalie Eversole
# Date: April 28th, 2022
#
# Description: This code parses JSON datasets and inserts
# the data into the PostgresSQL database.
#######################################################

import json
import psycopg2

def cleanStr4SQL(s):
    return s.replace("'","''").replace("\n"," ")

# Convert integer values to boolean
def int2BoolStr (value):
    if value == 0:
        return 'False'
    else:
        return 'True'

# Retreive attributes from businesses
def getAttributes(attributes):
    L = []
    for (attribute, value) in list(attributes.items()):
        if isinstance(value, dict):
            L += getAttributes(value)
        else:
            L.append((attribute,value))
    return L

# Insert business JSON dataset into the business table within PostgresSQL
def insert2BusinessTable():
    print("Parsing businesses...")
    with open('.//yelp_business.JSON','r') as f:
        line = f.readline()
        i = 0

        try:
            conn = psycopg2.connect("dbname='milestone1db' user='postgres' host='localhost' password='Kate1997'")
        except:
            print('Unable to connect to the database!')
        cur = conn.cursor()

        while line:
            data = json.loads(line)
            business_id = data['business_id'] #business id
            business_str =  \
                            "'" + cleanStr4SQL(data['name']) + "'," + \
                            "'" + cleanStr4SQL(data['address']) + "'," + \
                            "'" + cleanStr4SQL(data['city']) + "'," +  \
                            "'" + data['state'] + "'," + \
                            "'" + data['postal_code'] + "'," +  \
                            str(data['latitude']) + "," +  \
                            str(data['longitude']) + "," + \
                            str(data['stars']) + "," + \
                            str(data['review_count']) + "," + \
                            str(data['is_open'])

            # SQL INSERT statement for the businesses
            sql_str = "INSERT INTO businesstable (business_id, name, address, city, state, postal_code, latitude, longitude, stars, review_count, is_open) VALUES ('" + (data['business_id']) + "','" + cleanStr4SQL(data["name"]) + "','" + cleanStr4SQL(data["address"]) + "','" + cleanStr4SQL(data["city"]) + "','" + cleanStr4SQL(data["state"]) + "','" + cleanStr4SQL(data["postal_code"]) + "'," + str(data["latitude"]) + "," + str(data["longitude"]) + "," + str(data["stars"]) + "," + str(data["review_count"]) + "," + str(data["is_open"]) + ");"

            try:
                cur.execute(sql_str)
            except:
                print("Insert to businessTABLE failed!")
            conn.commit()

            line = f.readline()
            i +=1

        cur.close()
        conn.close()

    print(i)
    f.close()

insert2BusinessTable()

# Insert business attributes into the business category table within PostgresSQL
def insert2BusinessCategoryTable():
    print("Parsing business attributes...")
    with open('.//yelp_business.JSON','r') as f:
        line = f.readline()
        i = 0

        try:
            conn = psycopg2.connect("dbname='milestone1db' user='postgres' host='localhost' password='Kate1997'")
        except:
            print('Unable to connect to the database!')
        cur = conn.cursor()

        while line:
            data = json.loads(line)
            business_id = data['business_id']

            # Process business categories
            for category in data['categories']:
                category_str = "'" + business + "','" + category + "'"
                outfile.write(category_str + '\n')

            sql_str = "INSERT INTO BusinessCategoryTable (business_id, categories) VALUES ('" + (data['business_id']) + "','" + cleanStr4SQL(data["categories"]) + ");"

            try:
                cur.execute(sql_str)
            except:
                print("Insert to businessAttributesTABLE failed!")
            conn.commit()

            line = f.readline()
            i +=1

        cur.close()
        conn.close()

    print(i)
    f.close()

insert2BusinessCategoryTable()

# Insert review dataset into the review table within PostgresSQL
def insert2ReviewTable():
    print("Parsing reviews...")
    with open('.//yelp_review.JSON','r') as f:
        line = f.readline()
        i = 0
        failed_inserts = 0

        try:
            conn = psycopg2.connect("dbname='milestone1db' user='postgres' host='localhost' password='Kate1997'")
        except:
            print('Unable to connect to the database!')
        cur = conn.cursor()

        while line:
            data = json.loads(line)
            review_str = "'" + data['review_id'] + "'," +  \
                         "'" + data['user_id'] + "'," + \
                         "'" + data['business_id'] + "'," + \
                         str(data['stars']) + "," + \
                         "'" + data['date'] + "'," + \
                         "'" + cleanStr4SQL(data['text']) + "'," +  \
                         str(data['useful']) + "," +  \
                         str(data['funny']) + "," + \
                         str(data['cool'])

            sql_str = "INSERT INTO reviewtable (review_id, user_id, business_id, stars, date, text, useful, funny, cool) VALUES ('" + (data["review_id"]) + "','" + (data["user_id"]) + "','" + (data["business_id"]) + "'," + str(data["stars"]) + ",'" + (data["date"]) + "','" + str(data["text"]) + "'," + str(data["useful"]) + "," + int2BoolStr(data["funny"]) + "," + str(data["cool"]) + ");"

            try:
                cur.execute(sql_str)
            except:
                print("Insert to reviewTABLE failed!")
            conn.commit()

            line = f.readline()
            i +=1

        cur.close()
        conn.close()

    print(i)
    f.close()

insert2ReviewTable()

# Insert user dataset into the user table within PostgresSQL
def insert2UserTable():
    print("Parsing user...")
    with open('.//yelp_user.JSON','r') as f:
        line = f.readline()
        i = 0

        try:
            conn = psycopg2.connect("dbname='milestone1db' user='postgres' host='localhost' password='Kate1997'")
        except:
            print('Unable to connect to the database!')
        cur = conn.cursor()

        while line:
            data = json.loads(line)
            user_id = data['user_id']
            user_str = \
                      "'" + user_id + "'," + \
                      "'" + cleanStr4SQL(data["name"]) + "'," + \
                      "'" + cleanStr4SQL(data["yelping_since"]) + "'," + \
                      str(data["review_count"]) + "," + \
                      str(data["fans"]) + "," + \
                      str(data["average_stars"]) + "," + \
                      str(data["funny"]) + "," + \
                      str(data["useful"]) + "," + \
                      str(data["cool"])

            sql_str = "INSERT INTO usertable (user_id, name, yelping_since, review_count, fans, average_stars, funny, useful, cool) VALUES ('" + cleanStr4SQL(data["user_id"]) + "','" + cleanStr4SQL(data["name"]) + "','" + cleanStr4SQL(data["yelping_since"]) + "'," + str(data["review_count"]) + ",'" + str(data["fans"]) + "','" + str(data["average_stars"]) + "'," + str(data["funny"]) + "," + str(data["useful"]) + "," + str(data["cool"]) + ");"

            try:
                cur.execute(sql_str)
            except:
                print("Insert to userTABLE failed!")
            conn.commit()

            line = f.readline()
            i +=1

        cur.close()
        conn.close()

    print(i)
    f.close()

insert2UserTable()

# Insert friends information from the user dataset into the friend table within PostgresSQL
def insert2FriendTable():
    print("Parsing friends...")
    with open('.//yelp_user.JSON','r') as f:
        line = f.readline()
        i = 0

        try:
            conn = psycopg2.connect("dbname='milestone1db' user='postgres' host='localhost' password='Kate1997'")
        except:
            print('Unable to connect to the database!')
        cur = conn.cursor()

        while line:
            data = json.loads(line)
            user_id = data['user_id']
            friend_str = \
                         "'" + user_id + "'," + \
                         "'" + str(data["friends"])

            sql_str = "INSERT INTO friendtable (user_id, friends) VALUES ('" + str(data["user_id"]) + "','" + str(data["friends"]) + ");"

            try:
                cur.execute(sql_str)
            except:
                print("Insert to friendTABLE failed!")
            conn.commit()

            line = f.readline()
            i +=1

        cur.close()
        conn.close()

    print(i)
    f.close()

insert2FriendTable()
