
import weaviate
# from weaviate.classes.query import CountQuery, MetadataQuery, Filter
from weaviate.classes.query import Filter
import weaviate
import weaviate.classes as wvc
import os
from weaviate.classes.query import MetadataQuery
from db import connect

collection_name = "Candidates_Data"

client = connect()

# try: 
#     # Define the collection name (replace if different)
#     collection_name = "Candidates_Data"
#     collection = client.collections.get(collection_name)

#     # # Count total candidates
#     response = collection.aggregate.over_all(total_count=True)
#     print(f"Total Object Count: {response.total_count}")
# except:
#     print("Something went wrong!")
# finally:
#     client.close()

def search_candidates(client, query, *kwargs):

    filter_operands = []

    # Location filter
    if "location" in kwargs:
        filter_operands.append({
            wvc.query.Filter.by_property("current_location").equal(kwargs["location"]) 
        })
        # Experience filters
    if "experience_min" in kwargs:
        filter_operands.append({
            wvc.query.Filter.by_property("experience").greater_than(kwargs["experience_min"]) 
        })
    if "experience_max" in kwargs:
        filter_operands.append({
            wvc.query.Filter.by_property("experience").less_than( kwargs["experience_max"])
        })

    # Salary filters
    if "salary_min" in kwargs:
        filter_operands.append({
            wvc.query.Filter.by_property("present_ctc").gt(kwargs["salary_min"])
        })
    if "salary_max" in kwargs:
        filter_operands.append({
            wvc.query.Filter.by_property("present_ctc").lt(kwargs["salary_max"])
        })

    # Company filter
    if "company" in kwargs:
        filter_operands.append({
            wvc.query.Filter.by_property("current_company").equal(kwargs["company"])
        })

    # Designation filter
    if "designation" in kwargs:
        filter_operands.append({
            wvc.query.Filter.by_property("formatted_current_company", "profile").equal(kwargs["designation"])
            
        })

    # Job Description filter
    if "job_description" in kwargs:
        filter_operands.append({
            wvc.query.Filter.by_property("job_description").text.contain(kwargs["job_description"])
            
        })

    # Recruiters filter (assuming recruiters are identified by an array of IDs)
    if "recruiters" in kwargs and isinstance(kwargs["recruiters"], list):
        for recruiter_id in kwargs["recruiters"]:
            filter_operands.append({
                wvc.query.Filter.by_property("accessible_ids").equal(kwargs["recruiter_id"])
                
            })


    if filter_operands:
        # Construct and execute the query with dynamic filters
        where_filter = {"operator": "And", "operands": filter_operands} 
    else:
        None 
        # where_filter = None  #No filter to apply

    candidates = client.collections.get(collection_name)
    response = candidates.query.hybrid(
        query=query,
        # filters=Filter.by_property("points").greater_than(200),
        kwargs=kwargs,
        query_properties=[
                "accessible_ids",
                "age",
                "candidate_id",
                "created_at",
                "creator_name",
                "present_ctc",
                "current_company",
                "current_location",],
        return_metadata=MetadataQuery(score=True, explain_score=True),
        limit=3
    )
    for o in response.objects:
        print(o.properties)
        print(o.metadata.score, o.metadata.explain_score)

# end of search function


# # candidates = client.collections.get("Candidates_Data")
# # response = candidates.query.fetch_objects(
# #     filters=Filter.by_property("round").equal("Double Jeopardy!"),
# #     limit=3
# # )
# #number of candidates matched by the query
# candidates = client.collections.get("Candidates_Data")
# response = candidates.aggregate.over_all(total_count=True)
# print(response.total_count)

kwargs = {
    "present_ctc": 3,
    "experience_max": 8,
    # "salary_min": 70000,
    # "company": "ABC Inc.",
    # "designation": "Senior Software Engineer",
    # "job_description": "Full-stack development",
}


result = search_candidates(client, "software", **kwargs)
# result = search_candidate("software" , experience_min =3, experience_max=8)

print(result)