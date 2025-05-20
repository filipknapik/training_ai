This is a quick workshop showcasing how to play with AI in Google Cloud Platform.

SESSION 1 - basics

1. Prepare a new GCP project
Pick a project to play in. If you don't have one, get an experimental one. 
An empty and fresh project would be ideal

2. Create a local folder in your laptop
create 'aiworkshop' folder in your Documents


3. gcloud init
Let's also authorize gcloud to access your project. Run:
gcloud init

Reinitialize with the project from #1 project, choose your corporate account, enter a project ID where you would play. 
Skip setting up a zone.


4. Set default project for quota checks and billing
gcloud auth application-default set-quota-project [yourproject]

5. Authenticate to your project for gcloud
Also, authenticate using this command:
gcloud auth application-default login

6. Download and install VS code
On your corporate laptop, install VS Code client.

Follow instructions from https://g3doc.corp.google.com/devtools/editors/vscode/g3doc/install.md?cl=head#macos
(for MacOS you have a direct link; for Windows you need to go to https://code.visualstudio.com/)

7. Add Gemini Code Assist plugin to VS code from the marketplace
You will find it in the marketplace on the left of the window.

8. In VS Code, open 'aiworkshop' folder (using Open Folder option, not individual files)
Leave the VS Code open. 

9. Check python version
Go back to the Terminal and check your python3 version:

python3 --version
or
python --version

Version 3.11 or newer is needed.

10. Create a virtual envrionment
While in the terminal window, in the 'aiworkshop', create a virtual environment:

Mac:
python3 -m venv venv
source venv/bin/activate

Windows:
python -m venv venv
venv\Scripts\activate

11. Enable Gemini API in Cloud Console
Go to the Cloud Console in the right GCP project, search for Gemini API and ensure it's Enabled.

12. Create a Vertex AI credential

Go to Cloud Console and type in Credentials in Cloud Console. Click on Create Credentials, and create API Key. Then, Edit this key and use Restrict Key and narrow it down only to Generative Language API.

Go back to your 

13. Install python dependencies
Back to the terminal. Let's install Python dependencies:

pip install -r requirements.txt

14. Let's run the first exercise!
python exercise1.py



SESSION 2 - Agents


SESSION 3

3. Download Terraform

Go to https://developer.hashicorp.com/terraform/install and download the right version.
In MacOS we can't use Brew, you need to download the right version.

Once downloaded, move the the terraform executable to the infra folder

4. Copy main.tf file to the infra

// TODO

5. Initiate Terraform

Go to infra folder and run:
./terraform init (on mac)
terraform init (on Windows)

You will get an error message like this:
More info:
https://upvote.googleplex.com/blockables/a451c0fbbb7cd5004e9aadf9ba6e2f5083a4530da99da1a460ee176ee9308c47

Copy the link to a browser and open in upvote, and then upvote. You now need to click on G -> sync santa rules to speed up the sync.

Once done, run terraform init again


10. Let's create our resources!

./terraform apply

11.  Establish an SSH tunnel using IAP


gcloud compute ssh jumpbox --project=filipstest6 --zone=europe-west3-a -- -L 5433:10.0.2.3:5432

12. install ADK
google-adk to requirements.txt
#git+https://github.com/google/adk-python.git@main

13. install adk
mkdir appbuilder/
cd appbuilder
touch .env
touch agent.py
touch __init__.py