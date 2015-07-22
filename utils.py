"""
Helper functions for isitrainingnow.com
"""

def format_result(is_raining, location_tuple, conditions, meta_string):
    """
    Format the given data to match the `result.html` template.
    """
    return {
        "raining": is_raining,
        "location": location_tuple,
        "weather": {
            "summary": conditions["summary"],
            "temperature": conditions["temperature"],
        },
        "location_meta": meta_string
    }
