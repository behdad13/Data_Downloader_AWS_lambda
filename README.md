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

4. Now, run ```lambda_valodator.py```, and you will see that the files are downloaded and stored in your AWS S3.


