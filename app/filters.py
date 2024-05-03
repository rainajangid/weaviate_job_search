# For more filter options see here: https://weaviate.io/developers/weaviate/search/filters
from weaviate.classes.query import Filter
import weaviate.classes as wvc

collection_name = "Candidates_Data"

# filters = (
#     Filter.by_property("age").less_than(35) and 
#     Filter.by_property("experience").greater_than(40) and  
#     Filter.by_property("present_ctc").greater_than(100000)
# )

# def query(client, query, *kwargs):

#     filter_operands = []

#     if "location" in kwargs:
#         filter_operands.append({
#             wvc.query.Filter.by_property("current_location").equal(kwargs["location"]) 
#         })
    
#     # Experience filters
#     if "experience_min" in kwargs:
#         filter_operands.append({
#             wvc.query.Filter.by_property("experience").greater_than(kwargs["experience_min"]) 
#         })
#     if "experience_max" in kwargs:
#         filter_operands.append({
#             wvc.query.Filter.by_property("experience").less_than( kwargs["experience_max"])
#         })

#     # Salary filters
#     if "salary_min" in kwargs:
#         filter_operands.append({
#             wvc.query.Filter.by_property("present_ctc").gt(kwargs["salary_min"])
#         })
#     if "salary_max" in kwargs:
#         filter_operands.append({
#             wvc.query.Filter.by_property("present_ctc").lt(kwargs["salary_max"])
#         })

#     # Company filter
#     if "company" in kwargs:
#         filter_operands.append({
#             wvc.query.Filter.by_property("current_company").equal(kwargs["company"])
#         })

#     # Designation filter
#     if "designation" in kwargs:
#         filter_operands.append({
#             wvc.query.Filter.by_property("formatted_current_company", "profile").equal(kwargs["designation"])
            
#         })

#     # Job Description filter
#     if "job_description" in kwargs:
#         filter_operands.append({
#             wvc.query.Filter.by_property("job_description").text.contain(kwargs["job_description"])
            
#         })

#     # Recruiters filter (assuming recruiters are identified by an array of IDs)
#     if "recruiters" in kwargs and isinstance(kwargs["recruiters"], list):
#         for recruiter_id in kwargs["recruiters"]:
#             filter_operands.append({
#                 wvc.query.Filter.by_property("accessible_ids").equal(kwargs["recruiter_id"])
                
#             })

    
#     where_filter = None
#     if filter_operands:
#         where_filter = {"operator": "And", "operands": filter_operands}

#     candidates = client.collections.get(collection_name)
#     response = candidates.query.hybrid(
#         query=query,
#         filters=where_filter,  # Pass the constructed filter
#         limit=3
#     )

#     for o in response.objects:
#         print(o.properties)
#         print(o.metadata.score, o.metadata.explain_score)



def filters(*kwargs):

    filter_operands = []

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

    
    where_filter = None
    if filter_operands:
        where_filter = {"operator": "And", "operands": filter_operands}

    return where_filter