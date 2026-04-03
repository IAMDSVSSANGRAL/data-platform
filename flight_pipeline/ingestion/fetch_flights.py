import requests
import pandas as pd

URL = "https://opensky-network.org/api/states/all"


def fetch_flight_data():

    response = requests.get(URL, timeout=10)

    data = response.json()

    states = data.get("states", [])

    if not states:
        print("No flight data received")
        return pd.DataFrame()

    # Correct full column list (17 columns)

    columns = [
        "icao24",
        "callsign",
        "origin_country",
        "time_position",
        "last_contact",
        "longitude",
        "latitude",
        "baro_altitude",
        "on_ground",
        "velocity",
        "true_track",
        "vertical_rate",
        "sensors",
        "geo_altitude",
        "squawk",
        "spi",
        "position_source"
    ]

    df = pd.DataFrame(states, columns=columns)

    # Keep only columns we need

    df = df[
        [
            "icao24",
            "callsign",
            "origin_country",
            "longitude",
            "latitude",
            "baro_altitude",
            "velocity",
            "last_contact"
        ]
    ]

    # Rename to match DB schema

    df = df.rename(
        columns={
            "baro_altitude": "altitude"
        }
    )

    # Drop rows where timestamp is missing

    df = df.dropna(subset=["last_contact"])

    return df