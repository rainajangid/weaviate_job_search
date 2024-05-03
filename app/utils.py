import re
import json

def fix_json_format(data):
    try:
        # Convert to string in case the input data is not
        fields_to_parse = [ "formatted_candidate_history", "formatted_ctc", "formatted_current_company", "formatted_education"]
        
        for field in fields_to_parse:
            # Check if the field exists and is a string
            if field in data and isinstance(data[field], str):
                # Convert the JSON string within the field to a Python dictionary
                data[field] = re.sub(r"'(.*?)'", r'"\1"', data[field])
                data[field] = json.loads(data[field])
        return data
    except json.JSONDecodeError as e:
        print(f"Could not correct data: {data}. Error: {e}")
        return data  # Return original if correction fails
    except Exception as e:
        # Handle other generic errors
        print(f"Unexpected error: {e}")
        return data