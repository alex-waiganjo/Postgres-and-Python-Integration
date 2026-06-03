from db_config import get_connection

sql = """
Insert into employees(name, department, salary)
values (%s, %s, %s)
Returning id
"""

with get_connection() as conn:
    with conn.cursor() as cur:
        cur.execute(sql, ("Jenny Murage", "Sales and Marketing", 100000))
        new_id = cur.fetchone()[0]
        conn.commit()
        print(f"New Record Inserted: {new_id}")
