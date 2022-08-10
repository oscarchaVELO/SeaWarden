import resource
import boto3
import botocore  #Libraries

#boto3 documentation
resource = boto3.resource('s3')
my_bucket = resource.Bucket('sea-warden-platform-dev')


#getting into the path for files
for object_summary in my_bucket.objects.filter(Prefix="sw_eos/0_sw_eos/site_"): #iterate through s3
    splitObj = object_summary.key #Used for splitting
    Suffix = 'KDEs.json'  #Case for file needed
    edgeCase = '6_outputs' #Edge case for garbage file
    split = splitObj.split('/') #Getting file name from path
    if Suffix in object_summary.key and edgeCase not in object_summary.key: #Checking if its the right file
        #Download code
        resource.Bucket('sea-warden-platform-dev').download_file(object_summary.key,  
        '/Users/chacha/Downloads/'+ split[3])  #Change the path for your machine i.e /Users/chacha is mine
        print(split[3])
       





