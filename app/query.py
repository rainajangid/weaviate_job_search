from db import connect
from filters import filters
import traceback
from filters import filters


client = connect()
collection_name = "Candidates_Data"

# this gets you all the candidates in dataset
def get_total_candidates(client):
    collection = client.collections.get(collection_name)
    response = collection.aggregate.over_all(total_count=True) # count all elements
    print(f"Total number of candidates: {response.total_count}")


# this lets you run hybrid query with filter options. Also, prints number of candidates in search
def hybrid_query(client, query, limit, *kwargs):

    where_filter = filters(kwargs)

    print("Here are hybrid query results:")

    candidates = client.collections.get(collection_name)
    response = candidates.query.hybrid(
        query=query,
        filters=where_filter,  # Pass the constructed filter
        limit=limit
    )

    # uncomment that out if you want objects to print
    for o in response.objects:
        print(o.properties)

    print(f"Number of candidates in search: {len(response.objects)}")
    return response


# NOTE: while debugging make sure you run query out of try except
try:  
    # query 1  
    get_total_candidates(client)
    
    kwargs = {
    "present_ctc": 3,
    "experience_max": 8,
    # "salary_min": 70000,
    # "company": "ABC Inc.",
    # "designation": "Senior Software Engineer",
    # "job_description": "Full-stack development",
    }
    
    # query 2
    hybrid_query(client, "Social world machine", 3, kwargs)
except Exception as e:
    print("Error:", e)
    traceback.print_exc()
finally:
    client.close()