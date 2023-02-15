import json

from ckanext.eaw_core.utils.general import format_to_list_of_strings


def add_zulu_to_timestamp(ts):
    """Z means “zero hour offset” also known as “Zulu time” (UTC)"""
    if (ts.count(":") == 2) and not ts.endswith("Z"):
        ts += "Z"
    return ts


def load_datetime_strings(datetime_string) -> list:
    try:
        return json.loads(datetime_string)
    except ValueError:
        return [datetime_string]


def output_daterange(values):
    """
    For display:
      + remove brackets from timerange.
      + remove trailing "Z"  from time-points.
    """
    # We try to output everything, even "illegal" values.
    values = format_to_list_of_strings(values)
    return [value.strip().strip("[]").replace("Z", "") for value in values]
