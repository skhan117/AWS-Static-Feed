# AWS S3 Static Feed Application

This cloud-based application allows a user to read and download files from an AWS S3 bucket.

## Installation

First, ensure that python3, virtualenv, git, and AWSEBCLI are installed on your machine. If necessary install these libraries. 

```pip install virtualenv```

```pip install awsebcli```

To properly setup AWS CLI (command-line interface) on your machine, you will need to follow the instructions for setup on the AWS tutorials page. It is also highly recommended that you cover the basics of AWS S3 and AWS Elastic Beanstalk, since we will be making use of these services. 

Now, let's set up our app. Enter Terminal on Mac or the command line on Windows. Navigate to your home directory, then create a new directory for the project and cd into it.

```mkdir MyStaticFeed```

```cd MyStaticFeed```

Start a virtual environment for this project named "venv". A virtual environment (or virtualenv) allows an application to have its own set of installed packages that are independent of those on your machine. When we deploy this app to AWS Elastic Beanstalk, this virtual environment will tell AWS what packages are needed for the application to run. AWS will automatically take care of these dependencies on our behalf.  

```virtuelenv venv```

Activate the virtual environment.

```source venv/bin/activate```

Clone this git repository into your application directory.

```git clone https://github.com/skhan117/AWS-Static-Feed```

We need to install the proper libraries in the application's virtual environment. The libraries needed (Flask, etc) are listed in requirements.txt, so we just have pip install this text file. 

```pip3 install -r requirements.txt```

You will need to edit line 14 in application.py to point to the S3 bucket in your AWS account that you want to access.

```BUCKET = os.getenv("TARGET_S3_BUCKET")```

Change TARGET_S3_BUCKET to the name of your bucket, and make sure to have permissions setup so that the application can access this bucket.

Get the application up and running on your machine with the following command. The application will be accessible on your machine on port 8004.

```python3 application.py --i 0.0.0.0 --port 8008```

Now open a web browser and enter "http://localhost:8008/staticfeed" into your search bar. You should be able to see a webpage serving files from your S3 bucket. 

To exit the app, hit Control-C. 

We now have a static feed application that can run on our local machine, but we need to be able to deploy this application to AWS Elastic Beanstalk. 

Now we'll initialize the application for AWS EB. 

```eb init myflaskapp -p python-2.7 --region us-west-1```
It is recommended that you the region argument to something closer to you; see the AWS Elastic Beanstalk quickstart tutorial for details.

Create an environment where will we will deploy our source code. Our environment will upload our source code to AWS Elastic Beanstalk and automatically provision EC2 instances and load balancers for us.
```eb create myflaskappenv```

Go to your AWS Elastic Beanstalk console to confirm that the application is up and running. 

Now we'll open our application, which is now running on AWS, in a new web browser window. 
```eb open```

If you want to edit your source code to update your app, do so on your local machine, then re-deploy to AWSEB. 
```eb deploy```

When we no longer need our application to run, we will need to destroy the application on AWS. 
```eb terminate myflaskappenv```
