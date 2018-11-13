# "Database code" for the DB Forum.


import psycopg2

DBNAME = 'news'


def popular_articles():
    """Return the most popular three articles of all timet."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute('''
                select articles.title, count(path) as views
                from articles, authors, log
                where articles.slug = substr(log.path, length('/article/') + 1)
                AND articles.author = authors.id
                group by articles.title order by views desc limit 3;
            ''')
    result = c.fetchall()
    db.close()
    return result


def popular_authors():
    '''Returns the most popular article authors of all time'''
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute('''
                select authors.name, count(authors.id) as views
                from log, authors, articles
                where articles.slug = substr(log.path, length('/article/') + 1)
                and articles.author = authors.id
                group by authors.name
                order by views desc;
            ''')
    result = c.fetchall()
    db.close()
    return result


def get_errors():
    '''Returns days of more than 1% error requests'''
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute('''
                select to_char(date, 'Month DD, YYYY') as date, percent
                from (select total.date, num, errors,
                round(((errors::numeric / num::numeric) * 100), 1)::decimal
                as percent
                from total, error
                where error.date = total.date
                group by total.date, num, errors) as report
                where percent > 1
                order by percent desc;
            ''')
    result = c.fetchall()
    db.close()
    return result
