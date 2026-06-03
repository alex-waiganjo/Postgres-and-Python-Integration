from db_config import get_connection

with get_connection() as conn:
    with conn.cursor() as cur:
        cur.execute("""
        CREATE TABLE IF NOT EXISTS employees(
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    department VARCHAR(80),
                    salary NUMERIC(10,2))
                 """)
    print("Employees Table Created Successfully")
