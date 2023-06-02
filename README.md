# Data_Downloader_AWS_lambda
An automated file downloader, designed for AWS Lambda function 
-----------------

1. First step: create an environment to run and test the code with an IDE (e.g., Pycharm). In order to do it, run the following commands in Terminal.

* Create a directory for the project:
```
mkdir IESO-downloader
cd IESO-downloader
```

* Set up a virtual environment and activate it:
```
IESO-downloader % python3 -m venv ieso-venv
IESO-downloader % source ieso-venv/bin/activate
```

* Install the required libraries into the environment:
```
pip install boto3
pip install requests
mkdir iesolib
pip install requests -t iesolib
```

* List all installed libraries in the target directory:
```
ls -ltr iesolib
```

2. Open the created folder in your IDE and download all the code files. Copy them to your main directory (```IESO-downloader```).


3. Before running the code, set the environment variables in your IDE:

* BASELINE_FILE : PUB_RealtimeMktTotals_2023042708.csv (your initial file name)
* BOOKMARK_FILE : bookmark
* BUCKET_NAME : ieso-downloader (your bucket name)
* FILE_PREFIX : landing/ieso-weekly-activity (landing path)

4. Now, run ```lambda_valodator.py``` on your IDE, and you will see that the files are downloaded and stored in your AWS S3.

5. The final step using the IDE involves creating a .zip file for your AWS Lambda function. Follow these commands:

```
cd ghalib
zip -r ../ieso-downloader.zip .
cd ..
zip -g ieso-downloader.zip lambda_function.py download.py upload.py util.py
```

----------
6. Lambda Function configuration: Once you have created the .zip file, uploading it to AWS Lambda is a straightforward process. Remember to set the necessary environment variables, adjust the memory size and timeout values to prevent any potential errors. Additionally, ensure proper access management by assigning the AmazonS3FullAccess IAM role to the Lambda function. Finally, execute the function and retrieve your data in your designated S3 Bucket.

7. Schedule Lambda Function using AWS EventBridge: To automate the data download process, you can schedule your AWS Lambda function according to your desired schedule type. Depending on the frequency of your data updates (whether hourly, daily, monthly, or otherwise), AWS EventBridge allows you to conveniently schedule the Lambda function to fetch the data automatically.

8. If you wish to customize the code for your specific data downloader, you can easily modify the "download.py" and "utils.py" files according to your requirements. These files are responsible for the downloading and utility functions, respectively. By making changes to these files, you can tailor the functionality to suit your specific data retrieval needs.

-------

Data Source:

<img width="814" alt="image" src="https://github.com/behdad13/Data_Downloader_AWS_lambda/assets/58978680/b40bdd21-fa80-495f-8117-f7e51e8ec028">


Data Destination on S3:

<img width="1068" alt="image" src="https://github.com/behdad13/Data_Downloader_AWS_lambda/assets/58978680/7f0cb2fd-3f8f-4a6f-ba37-656e05e0aa5d">



