from sqlite3 import connect


# adding parameter as an argument here
# the * makes it so that any number of parameters can be accepted
# this syntax is needed when adding an argument to get_supplier_products()
def query(query_text, *param):
    conn = connect('Northwind_large.sqlite')
    cur = conn.cursor()
    # added param
    cur.execute(query_text, param)

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
    , Id
    FROM Supplier
    ORDER BY CompanyName ASC
    """)

# Using Python logic to control what SQL is being run, 
# but this makes it possible for hackers to inject malicious SQL code
# def get_supplier_products(supplier_id):
    # return query(f"""
    #     SELECT * 
    #     FROM Product
    #     WHERE SupplierId = {supplier_id}
    # """)

# SQLite Python wrapper knows that the '?' is something we want to plugin a value here
def get_supplier_products(supplier_id):
    return query("""
        SELECT * 
        FROM Product
        WHERE SupplierId = ? 
    """
    , supplier_id)


# to keep track of the supplier's name when redirecting to a new page
def get_supplier(supplier_id):
    return query("""
        SELECT CompanyName 
        FROM Supplier
        WHERE Id = ? 
    """
    , supplier_id)