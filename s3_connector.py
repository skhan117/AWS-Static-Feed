import boto3

s3 = boto3.client('s3')    # Use Boto3 to open a connection to the S3 bucket.

def list_files(bucket):
    # Return a list of files present in a given bucket.
    contents = []
    try:
        for item in s3.list_objects(Bucket=bucket)['Contents']:
            print(item)
            contents.append(item)
    except Exception as e1:
        pass
    return contents

def download_file(file_name, bucket):
    # Download a specific file in the bucket.
    s3 = boto3.client('s3')
    s3 = boto3.resource('s3')
    output = f"downloads/{file_name}"
    s3.Bucket(bucket).download_file(file_name, output)
    return output