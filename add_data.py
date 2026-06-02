from db_config import get_connection

sql = """
Insert into students(name, city, score)
values (%s, %s, %s)
Returning id
"""
with get_connection() as conn:
    with conn.cursor() as cur:
        cur.execute(sql, ('Victor','Kisumu',87))
        new_id = cur.fetchone()[0]
        conn.commit()
        print(f"New Record Inserted: {new_id}")