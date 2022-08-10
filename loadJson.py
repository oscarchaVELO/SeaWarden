import resource
import boto3
import botocore
import json
from decimal import Decimal #Libraries


resource = boto3.resource('s3')
s3 = boto3.client('s3')   #Boto 3 tools
my_bucket = resource.Bucket('sea-warden-platform-dev')

dynamodbclient=boto3.resource('dynamodb')  #Dynamo Tools
sample_table = dynamodbclient.Table('demoLoad') # desried table to upload to

    
for object_summary in my_bucket.objects.filter(Prefix="sw_eos/0_sw_eos/site_"): #iterate through s3
    Suffix = 'KDEs.json'  #Case for file needed
    edgeCase = '6_outputs' #Edge case for garbage file
    if Suffix in object_summary.key and edgeCase not in object_summary.key: #Checking if its the right file
        result = s3.get_object(Bucket='sea-warden-platform-dev', Key=object_summary.key) #Getting object from AWS
        jsonDict = result["Body"].read().decode('utf-8') #Decoding into JSOn readablity
        jsonFileReader = json.loads(jsonDict, parse_float=Decimal) #loading and changing floats to decimals
        sample_table.put_item(Item = jsonFileReader) #filling the table
print('loaded into Dynamo')#see this when finsihed
        
        
        
    
              

        







