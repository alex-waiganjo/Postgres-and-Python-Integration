from db_config import get_connection

def view_employees():
    sql = """ SELECT * FROM employees
              order by salary desc;
              """
    
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql)
            results = cur.fetchall()

            for row in results:
                print(row)
        
view_employees()
    