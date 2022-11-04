import boto3
#  change the name as per user's bucket name
bucket_name = "test-bucket-gfg"

def upload_data_to_s3(bucket_name:str,file_name_on_bucket:str, file_path:str):
    try:
        s3 = boto3.resource("s3")
        bucket = s3.Bucket(bucket_name)
        
        # Key is the name with which file will be stored in the bucket
        bucket.upload_file(Key= file_name_on_bucket, Filename= file_path)
        print(f"{file_name_on_bucket} uploaded successfully")
    
    except Exception as e:
        return "Error occured while uploading data:: ",e

def download_data_from_s3(bucket_name:str,file_name_on_bucket:str, file_path:str):
    try:
        s3 = boto3.resource("s3")
        bucket = s3.Bucket(bucket_name)
        
        # Key is the name with which file will be stored in the bucket
        # Filename is the path & name for storing the downloaded data downloaded from s3
        bucket.download_file(Key= file_name_on_bucket, Filename= file_path)
        print(f"{file_path} downloaded successfully")
    except Exception as e:
        print(e)
        return "Error occured while downloading data:: ", e




# Run functions 

upload_data_to_s3(bucket_name, "sample_image.jpg", "2110.jpg")
download_data_from_s3(bucket_name, "sample_image.jpg", "s3download.jpg")
