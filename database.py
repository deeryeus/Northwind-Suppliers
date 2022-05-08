from sqlite3 import connect


def query(query_text, *param):
    conn = connect('Northwind_large.sqlite')
    cur = conn.cursor()

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


# added product count to display the number of products
# offered by suppliers
def get_supplier_info():
    return query("""
    SELECT s.Id
    , s.CompanyName
    , COUNT(p.Id) AS 'ProductCount'
    , s.City
    , s.Country
    FROM Product p
    INNER JOIN Supplier s
        ON p.SupplierId = s.Id
    GROUP BY s.CompanyName
    ORDER BY CompanyName ASC
    """)


def get_supplier_products(supplier_id):
    return query("""
        SELECT p.ProductName
        , p.SupplierId
        , s.CompanyName
        , p.QuantityPerUnit
        , p.UnitPrice
        , p.CategoryId
        , c.CategoryName
        FROM Product p
        INNER JOIN Supplier s
            ON p.SupplierId = s.Id
        INNER JOIN Category c
            ON p.CategoryId = c.Id
        WHERE p.SupplierId = ?
    """, supplier_id)


# added to view categories such as beverages, condiments, etc.
# along with the number of products within that category
def get_categories():
    return query("""
        SELECT c.Id
        , c.CategoryName
        , c.Description
        , COUNT(p.CategoryId) AS 'CategoryCount'
        FROM Category c
        INNER JOIN Product p
            ON c.Id = p.CategoryId
        GROUP BY c.CategoryName
        ORDER BY c.CategoryName ASC
    """)

def get_category_info(category_id):
    return query("""
        SELECT c.Id
        , c.CategoryName
        , p.ProductName
        , p.SupplierId 
        , s.CompanyName
        , p.CategoryId
        FROM Product p
        INNER JOIN Supplier s
            ON p.SupplierId = s.Id
        INNER JOIN Category c
            ON p.CategoryId = c.Id
        WHERE c.Id = ?
        ORDER BY s.CompanyName ASC
    """
    , category_id)