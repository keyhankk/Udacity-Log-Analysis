#!/usr/bin/env python

import psycopg2

DBNAME = "news"

query1 = (" SELECT title, count(*) AS view_number FROM articles,log "
          " WHERE articles.slug = substring(log.path, 10) "
          " GROUP BY title ORDER BY view_number DESC LIMIT 3; ")

query2 = (" SELECT authors.name, count(*) AS view_number FROM authors, articles, log "
          " WHERE articles.slug = substring(log.path, 10) AND articles.author = authors.id AND log.status LIKE '200 OK' "
          " GROUP BY authors.name ORDER BY view_number DESC; ")

query3 = (" WITH T1 AS"
          " ( SELECT date(time) AS date1, round(100.0*sum(case log.status when '200 OK'  then 0 else 1 end)/count(log.status),3) "
          " AS error_number FROM log "
          " GROUP BY date(time) ORDER BY error_number DESC ) "
          " SELECT date1, error_number"
          " FROM T1"
          " WHERE error_number > 1"
          " ORDER BY error_number DESC")

def Perform_Query(query_string):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query_string)
    return c.fetchall()
    db.close()
    
def Print_Query(result):
    for row in result:
        print("\t" + "%s - %d" % (row[0], row[1]) + " views ")
        
def Print_Query2(result):
    for row in result:
        print("\t" + "%s - %10.2f" % (row[0], row[1]) + " errors ")


print('\n 3 Most Popular Articles of all Time: \n')
Print_Query(Perform_Query(query1))
print('\n The most popular article authors of all time: \n')
Print_Query(Perform_Query(query2))
print('\n Days with more than 1% of requests lead to errors: \n')
Print_Query2(Perform_Query(query3))
