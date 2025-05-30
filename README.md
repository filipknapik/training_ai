This is a quick workshop showcasing how to play with AI in Google Cloud Platform.

## SESSION 1: Setup and First Exercise

### Installation Steps

1.  **Upgrade Gcloud** 
    If you don't have gcloud on your laptop today, install it from https://cloud.google.com/sdk/docs/install

    If you have it, upgrade it to the latest version, running the following command from your terminal (command) window:
    ```sh
    gcloud components update
    ```
    (approve all changes)

2.  **Download and install VS Code**  
    On your corporate laptop, install VS Code client.  
    Follow instructions from https://g3doc.corp.google.com/devtools/editors/vscode/g3doc/install.md?cl=head#macos
    (For MacOS you have a direct link; for Windows you need to go to https://code.visualstudio.com/)

3.  **Add Gemini Code Assist plugin to VS Code**  
    You will find it in the VS Code Marketplace (usually on the left sidebar).  

4.  **Check Python version**  
    Go to your Terminal and check your `python3` version. Version 3.11 or newer is needed.  
    You can use either of the following commands:  
    ```sh
    python3 --version
    ```
    ```sh
    python --version
    ```

5.  **Prepare a new GCP project**  
    Pick a Google Cloud Platform project to use for this workshop. If you don't have one, get an experimental one. An empty, fresh project is ideal. Note down your Project ID.

6.  **Create a local folder**  
    Create an `aiworkshop` folder in your `Documents` directory (or any preferred location).  

7. **Install Git**
    
    Check if you have a git client installed by running the following command in a terminal window:
    ```sh
    git --version
    ```

    If you have it installed, move on to the next point. If it throws an error, install it using the instruction below.

    **Mac/Linux:**
    Refresh libraries:
    ```sh
    xcode-select --install
    cd /
    mkdir temp
    cd temp
    curl -LO https://mirrors.edge.kernel.org/pub/software/scm/git/git-2.49.0.tar.gz
    tar -xzf git-2.49.0.tar.gz
    cd git-2.49.0
    make configure
    ./configure --prefix=/usr/local --with-openssl=/usr/bin/openssl 
    make all NO_TCLTK=1
    sudo make install NO_TCLTK=1
    git -v
    ```

8. **Clone this repo**
    
    While in the `aiworkshop` folder, clone this repo to it. 
    ```sh
    git clone https://github.com/filipknapik/training_ai.git
    ```  

9.  **Create a virtual environment**  
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
    All further python commands will need to be done in this session (window).

10.  **Install Python dependencies**  
    With your virtual environment activated, install the required Python packages from `requirements.txt`
    Check the contents of the `requirements.txt` file to see what you are installing. 

    **Mac/Linux or Windows:**  
    ```sh
    pip install -r requirements.txt
    ```

11.  **Open 'aiworkshop' folder in VS Code**  
    In VS Code, use the "Open Folder" option to open the `aiworkshop` directory. Do not open individual files. Leave VS Code open.
  
12.  **Enable Gemini API and Vertex AI API in Cloud Console**  
    Go to the Google Cloud Console, select the correct GCP project, search for "Gemini API" in the search bar, and ensure it's **Enabled**. Do the same for "Vertex AI API".

13. **Create a Vertex AI API Key**  
    In the Cloud Console, search for "Credentials". Click on "Create Credentials" and select "API Key".  
    Once the key is created, **edit the API key** to restrict its usage. Under "API restrictions", select "Restrict key" and choose "Generative Language API" from the dropdown. Save the changes.  

14. **Create an env variable with the key**  
    Go back to your VS Code window and create an `envvars.sh` file in the same folder where you have exercise files. Place the following line into this file:  
    ```sh
    export GCP_KEY="YOUR_API_KEY_HERE"`
    ```  
    (replacing YOUR_API_KEY_HERE with your actual code from the previous step) and save it.
    **Remember to never share this file or your API key with anyone!**

---
*Installation complete*

### Running Exercises

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

3.  **Authenticate `gcloud` for application default credentials**  
    Authenticate using this command:  
    ```sh
    gcloud auth application-default login
    ```

4.  **Set default project for quota and billing**  
    Set your project for application default credentials, which is used for quota checks and billing by some client libraries:  
    ```sh
    gcloud auth application-default set-quota-project YOUR_PROJECT_ID
    ```
    Replace `YOUR_PROJECT_ID` with your actual GCP Project ID.  

5.  **Activate the virtual environment**  
    If you are NOT seeing (venv) in front of your command prompt, activate it manually:
    ```sh
    venv\Scripts\activate
    ```

6.  **Exercise 1 - hardcoded question**  
    The first exercise will run a simple program that answers a question of "the capital of France".
    Execute the first Python script:  
    ```sh
    python exercise1.py
    ```

    Now, open exercise1.py file and read it carefully. Ensure you understand every part of it, in case of question - ask!

7.  **Exercise 2 - our first chat**  
    The second exercise improves the program a bit and allows it to answer any questions provided by a user. ".

    ```sh
    python exercise2.py
    ```

    Now, open exercise2.py file and again ensure you understand it.
    Try asking follow up questions (i.e. related to the model's previous answer or your prompt). You will see that the model remembers no context of the conversation.

8.  **Exercise 3 - our first chat, now with a Pro model**  
    The third exercise is identical to the third one - but uses a Pro model instead of Flash. Do you notice any differences? Go to the pricing model and notice price differences.  ".

    ```sh
    python exercise3.py
    ```

9.  **Exercise 4 - model configurations**  
    Let's play with model's settings. This exercise shows an example of a model with adjusted temperature. Change the settings to other options and see how the model's behavior changes. Look up configurations and feel free to play with other settings.  

    ```sh
    python exercise4.py
    ```

10.  **Exercise 5 - output schema definition**  
    What if you wanted to use LLM as a function in a program? You'd often need to enforce specific output conventions or formatting to make it useful for more deterministic parts of your application. This exercise shows how to define an output schema and enforce it on the model's response. 
    NOTE: Ask the model only in a way that it can answer with a location (it has no checks / protections against unrelated questions - for code clarity). E.g. ask 'where's the statue of liberty?' or 'where is the capital of Poland?'.
    This exercise will return a JSON with latitude and longitude of a location.  

    ```sh
    python exercise5.py
    ```

11.  **Exercise 6 - context injection into a prompt**  
    How do we include additional information into a call to LLM, beyond what a user provided in their input?
    This exercise shows how, at an application layer, to add additional information to LLM and connect user provided information with this additional input in a prompt.  

    The model includes the contents of 'taxmenothing.txt' - a user guide for totally fake accounting application. Ask the model about features of this application etc. 

    ```sh
    python exercise6.py
    ```

12.  **Exercise 7 - context injection into a prompt**  
    How to enforce a particular behaviour or a style to the model?
    Some applications and models have system prompts that you can influence outside of the current prompt provided to it. If it's not there, you can always provide it as an instruction to the actual input. 

    This is a very rude model, that will always answer in a very offensive way. Run at your own risk :P

    ```sh
    python exercise7.py
    ```

13.  **Exercise 8 - context injection into a prompt**  
    Similar exercise to the previous one, just that now we will be talking to a model that speaks in a youth language. 

    ```sh
    python exercise8.py
    ```

14.  **Exercise 9 - Let's build a backend service for a translation app**  
    Let's build an application that translates text from English to Polish and output the contents in a way that can be fed into another application component (e.g. UI).
    Write any English sentences to this model. 

    ```sh
    python exercise9.py
    ```

15.  **Exercise 10 - Image generation**  
    Let's generate an image from a text prompt. We will use both Positive and Negative prompts (Positive - what you want in the picture, Negative - what you DON'T want in the picture).

    ```sh
    python exercise10.py
    ```

## SESSION 2: Advanced Development Kit (ADK)  

1.  **Clone the repo again (potentially)**  
    If you cloned the repo just now, you can skip this step. Otherwise, ensure you have the latest copy of this code including the ADK examples (added lately).  
    Since you can't re-clone a repo to the same location, we'll need to do it again and do one file modification. 

    Ensure you run the code from the aiworkshop folder!  
    ```sh
    cd aiworkshop
    mkdir session2
    cd session2
    git clone https://github.com/filipknapik/training_ai.git
    cd training_ai
    mv adk1/model/.env_example adk1/model/.env
    ```

2.  **Open the session2 folde in VS Code**  
    Since we are in a different folder now, we need to open a new folder in VS Code - open the session2 folder.

3.  **Start ADK web server**  
    First, ensure that in a terminal session you still see `(venv)` in front of your command prompt. If not, activate the virtual environment manually (see step 5 in the `Running Exercises` section).
    
    When confirmed, go to the `adk1` folder start an ADK web server:  
    ```sh
    adk web
    ```

4.  **Play with it**  
    Open http://localhost:8000 in your browser.
    
    Ask the model the following questions (one by one):
    - What's the temperature in New York?
    - What's the time in New York?
    - How much is 28*(15 - 3.1531) + 12.11?
    - Who was the first president of the United States?


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
