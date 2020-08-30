# This is a static feed application that allows a user to download files from
# an Amazon S3 bucket. Login and logout is handled by an Auth0-based accessory application,
# which will handle logins and logouts, and is located at http://github.com/skhan117.

from flask import Flask, render_template, request, redirect, send_file
from s3_connector import list_files, download_file
import os

# Load environmental variables from a .env file in the root directory.
from dotenv import load_dotenv
load_dotenv()

application = Flask(__name__)
BUCKET = os.getenv("TARGET_S3_BUCKET")    # This is the S3 bucket we will be accessing.

# Root endpoint just returns a simple message.
@application.route('/')
def entry_point():
    return 'Roooot, you got the root route up.'

# The user is redirected to this endpoint after Auth0 has logged out the user.
@application.route('/logout')
def logout():
    return 'User has been logged out.'

@application.route("/staticfeed")
def staticfeed():
    # Staticfeed function uses a template to generate a basic HTML page 
    # with a list of files in the S3 bucket.
    contents = list_files(BUCKET)
    return render_template('staticfeed.html', contents=contents)

@application.route("/download/<filename>", methods=['GET'])
def download(filename):
    # This endpoint will call the proper Get method to download a specific 
    # file from the S3 bucket.
    if request.method == 'GET':
        output = download_file(filename, BUCKET)
    return send_file(output, as_attachment=True)

if __name__ == '__main__':
    application.run(debug=True)