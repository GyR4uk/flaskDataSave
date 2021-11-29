from urllib.parse import parse_qs


def parse_query_params(query_string):
    # Parse the query param string
    query_params = dict(parse_qs(query_string))
    # Get the value from the list
    query_params = {k: v[0] for k, v in query_params.items()}
    print(query_params)
    return query_params
