import os
from evtx import PyEvtxParser
import json


def extract_events(evtx_path, output_folder, min_event_id=40000, max_event_id=65000):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    binary_data_list = []  # List to hold binary data for all events
    parser = PyEvtxParser(evtx_path)
    records = []

    for record in parser.records_json():
        jd = json.loads(record["data"])

        # event_id = record["event_record_id"]
        try:
            event_id = jd["Event"]["System"]["EventID"]["#text"]
        except TypeError:
            event_id = jd["Event"]["System"]["EventID"]
        # provider = record["provider_name"]
        provider = jd["Event"]["System"]["Provider"]["#attributes"]["Name"]
        if min_event_id <= event_id <= max_event_id:
            if provider == "Mslnstaller":
                binary_data = jd["Event"]["EventData"]["Binary"]
                if binary_data:
                    records.append((event_id, bytes.fromhex(binary_data)))

    records.sort(key=lambda x: x[0])
    binary_data_list = [data for _, data in records]

    output_file = os.path.join(output_folder, "combined_events.mp4")
    with open(output_file, "wb") as f:
        for data in binary_data_list[::-1]:
            f.write(data)


evtx_file_path = r"Application.evtx"
output_directory = r"Palimpsest"
extract_events(evtx_file_path, output_directory)
