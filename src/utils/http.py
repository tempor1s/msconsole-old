
def retransmission(retries=3, backoff_factor=0.3, status_forcelist=(500, 502, 504), session=None):
    """Performs HTTP/HTTPS GET retransmission request.

    :param retries: URL path for the request. Should begin with a slash.
        :type: int
    :param backoff_factor: HTTP GET parameters.
        :type: float
    :param status_forcelist: The time of the first request (None if no
        retries have occurred).
        :type: tuple(int)
    :param session: The time of the first request (None if no
        retries have occurred).
        :type: Request Session Object
    """
    session = session
    retry = Retry(
        total=retries,  # retry limit
        read=retries,  # retry limit again
        connect=retries,  # retry limit andddd again
        backoff_factor=backoff_factor,  # wait time
        status_forcelist=status_forcelist,  # status code auto retry list
    )
    adapter = HTTPAdapter(max_retries=retry)  # start reconnection
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session
