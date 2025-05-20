This is a quick workshop showcasing how to play with AI in Google Cloud Platform.

## SESSION 1: Setup and First Exercise

### Installation Steps

1.  **Download and install VS Code**  
    On your corporate laptop, install VS Code client.  
    Follow instructions from https://g3doc.corp.google.com/devtools/editors/vscode/g3doc/install.md?cl=head#macos
    (For MacOS you have a direct link; for Windows you need to go to https://code.visualstudio.com/)

2.  **Add Gemini Code Assist plugin to VS Code**  
    You will find it in the VS Code Marketplace (usually on the left sidebar).  

3.  **Create a local folder**  
    Create an `aiworkshop` folder in your `Documents` directory (or any preferred location).  

4.  **Check Python version**  
    Go to your Terminal and check your `python3` version. Version 3.11 or newer is needed.  
    You can use either of the following commands:  
    ```sh
    python3 --version
    ```
    ```sh
    python --version
    ```

5.  **Create a virtual environment**  
    While in the terminal window, navigate into the `aiworkshop` folder, then create and activate a virtual environment:  

    **Mac/Linux:**  
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

    **Windows:**  
    ```sh
    python -m venv venv
    venv\Scripts\activate
    ```

6.  **Install Python dependencies**  
    With your virtual environment activated, install the required Python packages from `requirements.txt`:  
    ```sh
    pip install -r requirements.txt
    ```

7.  **Open 'aiworkshop' folder in VS Code**  
    In VS Code, use the "Open Folder" option to open the `aiworkshop` directory. Do not open individual files. Leave VS Code open.

8.  **Prepare a new GCP project**  
    Pick a Google Cloud Platform project to use for this workshop. If you don't have one, get an experimental one. An empty, fresh project is ideal. Note down your Project ID.

9.  **Enable Gemini API in Cloud Console**
    Go to the Google Cloud Console, select the correct GCP project, search for "Gemini API" in the search bar, and ensure it's **Enabled**.

10. **Create a Vertex AI API Key**  
    In the Cloud Console, search for "Credentials". Click on "Create Credentials" and select "API Key".  
    Once the key is created, **edit the API key** to restrict its usage. Under "API restrictions", select "Restrict key" and choose "Generative Language API" from the dropdown. Save the changes.  
    Go back to your VS Code window and edit the `envvars.sh` file in your `aiworkshop` folder. Place the API key you just created into this file (e.g., `export API_KEY="YOUR_API_KEY_HERE"`) and save it.
    **Remember to never share this file or your API key with anyone!**

---
*Installation complete*

### Running Your First Exercise

1.  **Load the API key into your terminal session**  
    In your terminal, within the `aiworkshop` folder (and with the virtual environment activated), run:  
    ```sh
    source envvars.sh
    ```

2.  **Initialize `gcloud`**  
    Authorize `gcloud` to access your project. Run:  
    ```sh
    gcloud init
    ```
    Reinitialize with the GCP project ID you selected in Installation Step 8. Choose your corporate account when prompted. You can skip setting up a default Compute Engine zone if asked.

3.  **Set default project for quota and billing**  
    Set your project for application default credentials, which is used for quota checks and billing by some client libraries:  
    ```sh
    gcloud auth application-default set-quota-project YOUR_PROJECT_ID
    ```
    Replace `YOUR_PROJECT_ID` with your actual GCP Project ID.  

4.  **Authenticate `gcloud` for application default credentials**  
    Authenticate using this command:  
    ```sh
    gcloud auth application-default login
    ```

5.  **Run the first exercise - hardcoded question**  
    The first exercise will run a simple program that answers a question of "the capital of France".
    Execute the first Python script:  
    ```sh
    python exercise1.py
    ```

    Now, open exercise1.py file and read it carefully. Ensure you understand every part of it, in case of question - ask!

6.  **Run the second exercise - our first chat**  
    The second exercise improves the program a bit and allows it to answer any question provided by a user. ".
    Execute the first Python script:  
    ```sh
    python exercise1.py
    ```

    Now, open exercise2.py file and again ensure you understand it.

## SESSION 2: Advanced Development Kit (ADK)  

1.  **Install the Advanced Development Kit (ADK)**  
    To use the ADK, you'll need to add it to your Python dependencies.  

    a.  **Update `requirements.txt`:**  
        Open your `requirements.txt` file in the `aiworkshop` folder and add the following line:  
        ```text
        google-adk
        ```
        *(Note: The original workshop material also mentioned an alternative for using a direct Git source, which was commented out. If instructed, you might use this instead:*
        ```text
        #git+https://github.com/google/adk-python.git@main
        ```
        *Ensure this line is commented out unless you specifically need to use it.)*

    b.  **Install dependencies:**  
        After saving `requirements.txt`, go to your terminal (with the virtual environment activated) and run:
        ```sh
        pip install -r requirements.txt
        ```

## SESSION 3: Infrastructure with Terraform

1.  **Download Terraform**
    Go to https://developer.hashicorp.com/terraform/install and download the appropriate Terraform binary for your operating system.
    For macOS, if you cannot use Brew, download the Darwin AMD64 or ARM64 version directly.
    Once downloaded, unzip it and move the `terraform` executable file into an `infra` subfolder within your `aiworkshop` directory.

2.  **Copy `main.tf` file to the `infra` folder**
    // TODO: (This step needs the `main.tf` file to be provided or created)

3.  **Initiate Terraform**
    Navigate to the `infra` folder in your terminal.
    Run the init command:
    -   For **Mac/Linux**:
        ```sh
        ./terraform init
        ```
    -   For **Windows**:
        ```sh
        terraform init
        ```
    You might encounter an error message related to executable policies (e.g., Santa on macOS). If so, follow the provided link for resolution steps:
    `https://upvote.googleplex.com/blockables/a451c0fbbb7cd5004e9aadf9ba6e2f5083a4530da99da1a460ee176ee9308c47`
    Copy the link to a browser, open it in Upvote, and upvote the policy. You may need to click on "G -> sync santa rules" to expedite the synchronization.
    Once done, try running `terraform init` (or `./terraform init`) again.

4.  **Create Terraform resources**
    After successful initialization, apply the Terraform configuration to create your resources:
    -   For **Mac/Linux**:
        ```sh
        ./terraform apply
        ```
    -   For **Windows**:
        ```sh
        terraform apply
        ```

5.  **Establish an SSH tunnel using IAP (if applicable)**
    If your setup involves a jumpbox and requires an SSH tunnel via Identity-Aware Proxy (IAP), use a command similar to this:
    ```sh
    gcloud compute ssh jumpbox --project=YOUR_PROJECT_ID --zone=europe-west3-a -- -L 5433:10.0.2.3:5432
    ```
    Replace `YOUR_PROJECT_ID`, `jumpbox`, `europe-west3-a`, and the port/IP details with your specific configuration.
