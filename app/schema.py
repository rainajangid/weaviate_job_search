from properties import properties
import weaviate.classes.config as wvc 
from db import connect
import traceback
from weaviate.classes.config import Configure
from fields import fields

client = connect()

collection_name = "Candidates_Data"

# delete a collection
def delete_schema(client):
    try:
        client.collections.delete(collection_name)
        print("Successfully collection deleted!")
    except Exception as e:
        client.close()
        print("Error:", e)
        traceback.print_exc()

# create a collection
def create_schema(client):
    try:
        client.collections.create(
        name=collection_name,
        properties=properties,
        vectorizer_config=Configure.Vectorizer.multi2vec_clip(text_fields=fields)
        )
        print("Schema successfully created!")
    except:
        print(f"Schema already exists: {client.collections.exists(collection_name)}")
    finally:
        client.close()

# ideally these should be put under try and except block unless you are debugging
try:
    # delete_schema(client) # don't use this liberally
    create_schema(client)
except:
    pass
finally:
    client.close()