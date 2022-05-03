from sqlite3 import connect


def query(query_text):
    conn = connect('Northwind_large.sqlite')
    cur = conn.cursor()
    cur.execute(query_text)

    column_names = []

    for column in cur.description:
        column_names.append(column[0])
    rows = cur.fetchall()

    dicts = []

    for row in rows: 
        d = dict(zip(column_names, row))
        dicts.append(d)

    conn.close()

    return dicts


# list of dictionaries for each row ...
# each dict contains { column name : data }
def get_name_city_country():
    return query("""
    Select CompanyName
    , City
    , Country 
    FROM Supplier
    ORDER BY CompanyName ASC
    """)
