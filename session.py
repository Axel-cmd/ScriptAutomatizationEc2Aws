from boto3.session import Session

# create session with accesskey and secret key ( and region )
def createSession(accessKeyId, secretKey, region):
    print("create session ...")
    return Session(
        accessKeyId,
        secretKey,
        region_name=region
    )

# create client (name : "eks", "ec2" etc )
def createClient(name, session):
    print("\ncreate client "+name+"...")
    return session.client(
        name,
        region_name= session.region_name # region's name get in session
    )