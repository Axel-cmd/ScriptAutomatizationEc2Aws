import os

# path to save the key 
key_path = "./key/ec2_key.pem"

# function to create keyPair 
def createKeyPairEc2(name, ec2):
    print("creating keypair for ec2 ...")
    keyPair = ec2.create_key_pair(KeyName=name)
    # get key in response
    privateKey = keyPair['KeyMaterial']
    # save the key in a file
    with os.fdopen(os.open(key_path, os.O_WRONLY | os.O_CREAT, 0o400), "w+") as handle:
        handle.write(privateKey)
    return 0