from db_connection import get_connection


def create_flights_table():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS flights (
            id SERIAL PRIMARY KEY,
            icao24 VARCHAR(10),
            callsign VARCHAR(20),
            origin_country VARCHAR(50),
            longitude FLOAT,
            latitude FLOAT,
            altitude FLOAT,
            velocity FLOAT,
            last_contact TIMESTAMP,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)

    conn.commit()

    cursor.close()
    conn.close()

    print("Flights table created successfully!")


if __name__ == "__main__":
    create_flights_table()