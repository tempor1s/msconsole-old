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


def check_banner_message(banner_message):
    """Changes the color of the terminal message depending on what the banner message is.

    :param banner_message: 
        :type: str
    """
    message = None
    # check the message so that we can change the color :)
    if 'You code is not related to any class.' == banner_message:
        message = '\033[93m' + banner_message + '\x1b[0m' + '\n'  # yellow
    elif 'You cannot check-in after a class is already over' == banner_message:
        message = '\033[93m' + banner_message + '\x1b[0m' + '\n'  # yellow
    elif 'You are not registered for this class.' == banner_message:
        message = '\x1b[1;31m' + banner_message + '\x1b[0m' + '\n'  # red
    elif 'You need to be connected to Make School Wi-Fi to check-in.' == banner_message:
        message = '\x1b[1;31m' + banner_message + '\x1b[0m' + '\n'  # red
    elif 'You have already checked in as for this class.' == banner_message:
        message = '\x1b[1;32m' + banner_message + '\x1b[0m' + '\n'  # green
    elif 'You have checked in present for this class.' == banner_message:
        message = '\x1b[1;32m' + banner_message + '\x1b[0m' + '\n'  # green
    elif 'You have checked in tardy for this class.' == banner_message:
        message = '\x1b[1;32m' + banner_message + '\x1b[0m' + '\n'  # green
    else:
        message = '\033[93m' + banner_message + '\x1b[0m' + '\n'  # yellow

    return message
