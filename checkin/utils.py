def graph_query(session, query):
    """Query MakeSchool GraphQL for data.

    :param session: Requests session.
        :type: Request Session Object
    :param query: GraphQL Query
        :type: str
        example:
        "
            {
                currentUser {
                    name
                }
            }
        "

    :returns GraphQL response
        :type: dict
    """
    headers = {
        "Content-Type": 'application/json'}  # set headers to declare json type

    # post to makeschool graphql endpoint with query and headers
    r = session.post(f'https://www.makeschool.com/graphql',
                     json={'query': query}, headers=headers)

    # check if request was successful
    if r.status_code == 200:
        # return graphQL json
        return r.json()
    else:
        # return None object if not 200 - #TODO Change to raise Exception
        return None
