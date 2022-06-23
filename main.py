import sys
from session import createSession, createClient
import keyPair
import config

# global variable for config
config_deployement = {}

# fonction for ec2 instance
def instanceEc2(session):

    global config_deployement

    # create ec2 client 
    ec2 = createClient("ec2", session=session)
    # create key pair for Ec2 instance
    keyPair.createKeyPairEc2(config_deployement['key_pair_name'], ec2)

    print("Create ec2 instance...")
    # create ec2 instance 
    result = ec2.run_instances(
        ImageId=config_deployement['ec2_image_id'],
        InstanceType=config_deployement['ec2_instance_type'],
        MaxCount=1,
        MinCount=1,
        KeyName=config_deployement['key_pair_name'],
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': config_deployement['ec2_name']
                    }
                ]
            }
        ],
    )

    instance = result['Instances'][0]
    print("Instance Id : " + instance['InstanceId'])

# cluster kubernetes
def kubernetes(session) : 
    print("create eks")
    iam = session.client('iam')
    roleArn = iam.get_role(RoleName="eksclustergroup4")
    
    eks = createClient("eks", session)

    result = eks.create_cluster(
        name='Groupe4-Saagie-k',
        roleArn=roleArn,
        resourcesVpcConfig={

        }
    )
    print("\n"+result)
    return result


# main function
def main():

    global config_deployement

    # get deployement config 
    config_deployement = config.load_config()

    # create session  
    session = createSession(config_deployement['access_key_id'], config_deployement['secret_key'], config_deployement['region'])
    print(session)

    # instance EC2
    instanceEc2(session=session)
    return 0 


if __name__ == '__main__':
    sys.exit(main())