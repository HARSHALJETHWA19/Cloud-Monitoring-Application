# import json
# import boto3

# access_key = "281d55d72b9eedaee8d1a42137a2d9c5210b032d7b08d0109e4788ac18785f70"
# secret_access = "AKIAWRMTLGEUWLXFT7PX"
# repository_name = "my-cloud-repo"

# ecr_client = boto3.client('ecr', region_name="us-east-1",
#                       aws_access_key_id=access_key,
#                       aws_secret_access_key=secret_access)


# response = ecr_client.create_repository(repositoryName=repository_name)

# repository_uri = response['repository']['repositoryUri']

# print(repository_uri)

import boto3

ecr_client = boto3.client('ecr')

repository_name = "cloud_monitoring_app"
response = ecr_client.create_repository(repositoryName=repository_name)

repository_uri = response ['repository']['repositoryUri']
print(repository_uri)