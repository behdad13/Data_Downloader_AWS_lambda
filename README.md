# Data_Downloader_AWS_lambda
An automated file downloader, designed for AWS Lambda function 

First, set the environment variables in AWS Lambda:
1. BASELINE_FILE : PUB_RealtimeMktTotals_2023042708.csv (your initial file name)
2. BOOKMARK_FILE : bookmark
3. BUCKET_NAME : ieso-downloader (your bucket name)
4. FILE_PREFIX : landing/ieso-weekly-activity (landing path)
