from ingestion.fetch_flights import fetch_flight_data
from database.db_connection import get_connection
from utils.logger import setup_logger

logger = setup_logger()


def insert_data():

    logger.info("Fetching flight data...")

    df = fetch_flight_data()

    logger.info(f"Total records fetched: {len(df)}")

    conn = get_connection()

    cursor = conn.cursor()

    inserted = 0

    for _, row in df.iterrows():

        try:

            cursor.execute(
                """
                INSERT INTO flights (
                    icao24,
                    callsign,
                    origin_country,
                    longitude,
                    latitude,
                    altitude,
                    velocity,
                    last_contact
                )
                VALUES (%s,%s,%s,%s,%s,%s,%s,to_timestamp(%s))
                """,
                (
                    row["icao24"],
                    row["callsign"],
                    row["origin_country"],
                    row["longitude"],
                    row["latitude"],
                    row["altitude"],
                    row["velocity"],
                    row["last_contact"]
                )
            )

            inserted += 1

        except Exception as e:

            logger.error(f"Insert failed: {e}")

    conn.commit()

    cursor.close()
    conn.close()

    logger.info(f"Inserted records: {inserted}")


if __name__ == "__main__":

    insert_data()