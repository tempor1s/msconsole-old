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

def retransmission(self, retries=3, backoff_factor=0.3, status_forcelist=(500, 502, 504), session=None):
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


# TODO: For later use in encryption
# helper functions
def _gen_key(self):
    # start by generating a encryption key
    key = Fernet.generate_key()
    # write encryption key to current working directory
    file = open(os.curdir, 'wb')  # wb = write bytes
    # input bytes into file
    file.write(key)
    # close file input stream
    file.close()

def _retrieve_key(self, path):
    # open file in read bytes mode
    file = open(path, 'rb')
    # set the key
    key = file.read()
    # close the output stream
    file.close()
    # print the key
    print(key)
    # return the key
    return key

def _encrypt(self, path):
    """Encrptys the credentials files"""
    # Get the key from the file
    file = open(path, 'rb')
    # set key variable
    key = file.read()
    # close the output stream
    file.close()
    #  Open the credentials file we need to encrypt
    with open(self.creds_path, 'rb') as f:
        # output file contents
        data = f.read()
    # fernet encryption key
    fernet = Fernet(key)
    # encrypt file output stream with generated key
    encrypted = fernet.encrypt(data)
    # Write the encrypted file
    with open(self.creds_path, 'wb') as f:
        f.write(encrypted)
        f.close()

def _decrypt(self, path):
    # Get the key from the file
    file = open(path, 'rb')
    # set key to output stream
    key = file.read()
    # close output stream
    file.close()
    #  open the credentials file
    with open(self.creds_path, 'rb') as f:
        # the stream is the data we need to decrypt with our key
        data = f.read()
    # set the fernet key
    fernet = Fernet(key)
    # decrypt the output stream
    encrypted = fernet.decrypt(data)
    # Open the decrypted file
    with open(self.creds_path, 'wb') as f:
        # input decrypted data
        f.write(encrypted)
        # close input stream
        f.close()