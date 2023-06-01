import boto3
from botocore.errorfactory import ClientError


def get_client():
    return boto3.client('s3')


def get_prev_file_name(bucket, file_prefix, bookmark_file, baseline_file):
    s3_client = get_client()
    try:
        bookmark_file = s3_client.get_object(
            Bucket=bucket,
            Key=f'{file_prefix}/{bookmark_file}'
        )
        prev_file = bookmark_file['Body'].read().decode('utf-8')
    except ClientError as e:
        if e.response['Error']['Code'] == 'NoSuchKey':
            prev_file = baseline_file
        else:
            raise
    return prev_file


def upload_bookmark(bucket, file_prefix, bookmark_file, bookmark_contents):
    s3_client = get_client()
    s3_client.put_object(
        Bucket=bucket,
        Key=f'{file_prefix}/{bookmark_file}',
        Body=bookmark_contents.encode('utf-8')
    )

from datetime import datetime, timedelta

from datetime import datetime, timedelta

def get_next_file_name(prev_file):
    date_part = prev_file.split('_')[2].split('.')[0]
    year = int(date_part[:4])
    month = int(date_part[4:6])
    day = int(date_part[6:8])
    hour = int(date_part[8:10])

    # If the hour is 24, we consider it as the beginning of the next day, and the hour should be 1 (for the next file)
    if hour == 24:
        current_datetime = datetime(year, month, day) + timedelta(days=1) # increment the day
        formatted_hour = '01' # start from 1 for the next day
    else:
        # Otherwise, increment the hour and maintain the day
        current_datetime = datetime(year, month, day) + timedelta(hours=hour)
        formatted_hour = f"{current_datetime.hour + 1:02d}" # increment the hour, ensure it's two digits

    next_file = f"PUB_RealtimeMktTotals_{current_datetime.strftime('%Y%m%d')}{formatted_hour}.csv"
    return next_file

