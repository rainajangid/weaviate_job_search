import traceback
import re
from db import connect
from data import DataGenerator
import json
from pprint import pprint
from weaviate.util import generate_uuid5

# Initialize Weaviate client
client = connect()
collection_name = "Candidates_Data"

def delete_collection(client):
    # NOTE: create schema again after collection has been deleted to reload.
    client.collections.delete(collection_name)
    print("Collection Deletion Success!")

def load(client):
    # Generate data
    num_samples = 100
    generator = DataGenerator()
    data = generator.generate_data(num_samples)

    # Define collection name
    collection_name = "Candidates_Data"

    print("Vectorizing text...." + "\n")

    print("This will take sometime!" + "\n")

    # Push data to Weaviate -- BATCH
    with client.batch.dynamic() as batch:
        for data_row in data:
            try:
                batch.add_object(
                    collection=collection_name,
                    properties=data_row,
                    uuid=generate_uuid5(data_row)
                )
            except Exception as add_exception:
                print("Error adding object:", add_exception)
                traceback.print_exc()

    print("Data Import Successful!" + "\n")

    # Load one object at a time
    # collection = client.collections.get(collection_name)
    # for datum in data:
    #     collection.data.insert(
    #     properties=datum,
    #     uuid=generate_uuid5(datum)
    # )

    # Get total count of objects in the collection
    collection = client.collections.get(collection_name)
    total_count = collection.aggregate.over_all(total_count=True).total_count
    print(f"Total Count: {total_count}")

# For debugging, run load outside of try except block
try:
    load(client)
except Exception as e:
    print("Error:", e)
    traceback.print_exc()
finally:
    # Close the Weaviate client connection
    client.close()

