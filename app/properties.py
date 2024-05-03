import weaviate.classes.config as wvc

properties = [
    wvc.Property(
        name="accessible_ids",
        data_type=wvc.DataType.INT_ARRAY,
        description="candidate accessible recruiter",
        vectorize_property_name=True
    ),
    wvc.Property(
        name="age",
        data_type=wvc.DataType.INT,
        description="candidate age",
        vectorize_property_name=True
    ),
    wvc.Property(
        name="candidate_id",
        data_type=wvc.DataType.INT,
        description="Unique identifier for the candidate",
        vectorize_property_name=True
    ),
    wvc.Property(
        name="created_at",
        data_type=wvc.DataType.DATE,
        description="date and time at candidate creation",
        vectorize_property_name=True
    ),
    wvc.Property(
        name="creator_name",
        data_type=wvc.DataType.TEXT,
        description="Candidate created by user",
        vectorize_property_name=True
    ),
    wvc.Property(
        name="present_ctc",
        data_type=wvc.DataType.NUMBER,
        description="Current CTC of the candidate",
        vectorize_property_name=True
    ),
    wvc.Property(
        name="current_company",
        data_type=wvc.DataType.TEXT,
        description="Current Company Name of a candidate",
        vectorize_property_name=True,
        tokenization=wvc.Tokenization.LOWERCASE 
    ),
    wvc.Property(
        name="current_location",
        data_type=wvc.DataType.TEXT,
        description="Current location of candidate",
        vectorize_property_name=True,
        tokenization=wvc.Tokenization.LOWERCASE 
    ),
    wvc.Property(
        name="education",
        data_type=wvc.DataType.TEXT_ARRAY,
        description="candidate educations",
        vectorize_property_name=True,
        tokenization=wvc.Tokenization.LOWERCASE 
    ),
    wvc.Property(
        name="expected_ctc",
        data_type=wvc.DataType.NUMBER,
        description="Expected CTC of the candidate",
        vectorize_property_name=True
    ),
    wvc.Property(
        name="experience",
        data_type=wvc.DataType.NUMBER,
        description="total experience of candidate",
        vectorize_property_name=True
    ),
    wvc.Property(
        name="formatted_candidate_history",
        data_type=wvc.DataType.OBJECT_ARRAY,
        description="formatted candidate history",
        vectorize_property_name=True,
        nested_properties=[
            wvc.Property(
                name="job_title",
                data_type=wvc.DataType.TEXT,
                vectorize_property_name=True,
                tokenization=wvc.Tokenization.LOWERCASE 
            ),
            wvc.Property(
                name="lead_status",
                data_type=wvc.DataType.TEXT,
                vectorize_property_name=True,
                tokenization=wvc.Tokenization.LOWERCASE 
            ),
            wvc.Property(
                name="last_updated_at",
                data_type=wvc.DataType.DATE,
                vectorize_property_name=True 
            ),
            wvc.Property(
                name="created_by",
                data_type=wvc.DataType.INT,
                vectorize_property_name=True,
            )
        ]
    ),
    wvc.Property(
        name="formatted_ctc",
        data_type=wvc.DataType.OBJECT_ARRAY,
        description="formatted candidate present and expected ctc",
        nested_properties=[
            wvc.Property(
                name="formatted_present_ctc",
                data_type=wvc.DataType.TEXT,
                vectorize_property_name=True,
                tokenization=wvc.Tokenization.LOWERCASE 
            ),
            wvc.Property(
                name="formatted_expected_ctc",
                data_type=wvc.DataType.TEXT,
                vectorize_property_name=True,
                tokenization=wvc.Tokenization.LOWERCASE 
            )
        ]
    ),
    wvc.Property(
        name="formatted_current_company",
        data_type=wvc.DataType.OBJECT_ARRAY,
        description="formatted candidate present or last company",
        nested_properties=[
            wvc.Property(
                name="from",
                data_type=wvc.DataType.DATE,
                vectorize_property_name=True 
            ),
            wvc.Property(
                name="profile",
                data_type=wvc.DataType.TEXT,
                vectorize_property_name=True,
                tokenization=wvc.Tokenization.LOWERCASE 
            ),
            wvc.Property(
                name="company",
                data_type=wvc.DataType.TEXT,
                vectorize_property_name=True,
                tokenization=wvc.Tokenization.LOWERCASE 
            )
        ]
    ),
    wvc.Property(
        name="formatted_education",
        data_type=wvc.DataType.OBJECT_ARRAY,
        description="candidate education formatted",
        nested_properties=[
            wvc.Property(
                name="passing_year",
                data_type=wvc.DataType.NUMBER,
                vectorize_property_name=True
            ),
            wvc.Property(
                name="college",
                data_type=wvc.DataType.TEXT,
                vectorize_property_name=True,
                tokenization=wvc.Tokenization.LOWERCASE 
            ),
            wvc.Property(
                name="education",
                data_type=wvc.DataType.TEXT,
                vectorize_property_name=True,
                tokenization=wvc.Tokenization.LOWERCASE 
            )
        ]
    ),
    wvc.Property(
        name="formatted_previous_company",
        data_type=wvc.DataType.OBJECT_ARRAY,
        description="formatted candidate present or last company",
        vectorize_property_name=True,
        nested_properties=[
            wvc.Property(
                name="from",
                data_type=wvc.DataType.DATE,
                vectorize_property_name=True
            ),
            wvc.Property(
                name="to",
                data_type=wvc.DataType.DATE,
                vectorize_property_name=True
            ),
            wvc.Property(
                name="profile",
                data_type=wvc.DataType.TEXT,
                vectorize_property_name=True,
                tokenization=wvc.Tokenization.LOWERCASE 
            ),
            wvc.Property(
                name="company",
                data_type=wvc.DataType.TEXT,
                vectorize_property_name=True,
                tokenization=wvc.Tokenization.LOWERCASE 
            )
        ]
    ),
    wvc.Property(
        name="gender",
        data_type=wvc.DataType.TEXT,
        description="Gender of candidate",
        vectorize_property_name=True,
        tokenization=wvc.Tokenization.LOWERCASE 
    ),
    wvc.Property(
        name="headline",
        data_type=wvc.DataType.TEXT,
        description="headline of candidate",
        vectorize_property_name=True,
        tokenization=wvc.Tokenization.LOWERCASE
    ),
    wvc.Property(
        name="job_ids",
        data_type=wvc.DataType.INT_ARRAY,
        description="Candidate applied job ids",
        vectorize_property_name=True
    ),
    wvc.Property(
        name="key_skills",
        data_type=wvc.DataType.TEXT_ARRAY,
        description="Candidate Key Skills",
        vectorize_property_name=True,
        tokenization=wvc.Tokenization.LOWERCASE 
    ),
    wvc.Property(
        name="notice_period",
        data_type=wvc.DataType.NUMBER,
        description="Candidate Notice Period",
        vectorize_property_name=True
    ),
    wvc.Property(
        name="organization_id",
        data_type=wvc.DataType.INT,
        description="Candidate organization id",
        vectorize_property_name=True
    ),
    wvc.Property(
        name="name",
        data_type=wvc.DataType.TEXT,
        description="Name for the candidate",
        vectorize_property_name=True,
        tokenization=wvc.Tokenization.LOWERCASE 
    ),
    wvc.Property(
        name="other_skills",
        data_type=wvc.DataType.TEXT_ARRAY,
        description="Candidate Key Skills",
        vectorize_property_name=True,
        tokenization=wvc.Tokenization.LOWERCASE 
    ),
    wvc.Property(
        name="preferred_location",
        data_type=wvc.DataType.TEXT_ARRAY,
        description="Candidate Preferred location",
        vectorize_property_name=True,
        tokenization=wvc.Tokenization.LOWERCASE 
    ),
    wvc.Property(
        name="previous_company",
        data_type=wvc.DataType.TEXT_ARRAY,
        description="Candidate previous company",
        vectorize_property_name=True,
        tokenization=wvc.Tokenization.LOWERCASE 
    ),
    wvc.Property(
        name="profile",
        data_type=wvc.DataType.TEXT_ARRAY,
        description="Candidate profile",
        vectorize_property_name=True,
        tokenization=wvc.Tokenization.LOWERCASE 
    ),
    wvc.Property(
        name="profile_hash",
        data_type=wvc.DataType.TEXT,
        description="Candidate profile hash",
        vectorize_property_name=True,
        tokenization=wvc.Tokenization.LOWERCASE 
    ),
    wvc.Property(
        name="resume",
        data_type=wvc.DataType.TEXT,
        description="The textual content of the candidate's resume",
        vectorize_property_name=True,
        tokenization=wvc.Tokenization.LOWERCASE 
    ),
    wvc.Property(
        name="supplier_ids",
        data_type=wvc.DataType.INT_ARRAY,
        description="Candidate Supplier id",
        vectorize_property_name=True,
    ),
    wvc.Property(
        name="updated_at",
        data_type=wvc.DataType.DATE,
        description="date and time at candidate updated",
        vectorize_property_name=True
    )
]