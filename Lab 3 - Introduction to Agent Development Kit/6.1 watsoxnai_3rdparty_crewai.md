# Building an AI Agent with **watsonx.ai** & **Crew AI**

In this lab, we will create a **Sales Analyzer Agent** by leveraging *watsonx.AI Agent Lab* and the **Crew AI** framework. This agent will analyze product sales data to support the procurement process.

> **Note** Required files can be downloaded from the "📂 *to-be-provided*" folder.

---

## Agent Creation Steps

### Step 1: Create a *Project*
1. If this is your first time using this account, create a new **Project** before opening Agent Lab.
2. If you already have one, you can use an existing project.

![Project](https://github.com/user-attachments/assets/1282049d-f55e-47f6-9ff9-e176dd3e4af8)

---

### Step 2: Associate watsonx.ai Runtime
1. Open **Manage → Services & Integrations → Associate Service**.
2. Select **watsonx.ai** and link it to your project.

![Associate Service](https://github.com/user-attachments/assets/3e22c81c-288c-445c-a5c8-6cffb5976012)

---

### Step 3: Add a New *Asset*
1. Go to the **Assets** tab and click **New Asset**.

![New Asset](https://github.com/user-attachments/assets/dda99a0c-7240-40e7-a747-428d6bc2d06b)

---

### Step 4: Create a Notebook
1. Select **Work with data and models in Python or R notebooks**.
2. Click **Create a notebook**.

![Create Notebook](https://github.com/user-attachments/assets/2c45d6e5-167b-4189-afd0-f69e6a2ca284)

---

### Step 5: Upload the Notebook
1. Click **Local File**.
2. Upload the file:  
   • `salesFund_crewai.ipynb`  
3. Click **Create** to complete.

![Upload Notebook](https://github.com/user-attachments/assets/6c517d66-8bb0-441b-9b5e-94c44c601aed)

![Upload Notebook](https://github.com/user-attachments/assets/55564b87-dc55-4b54-a255-31ae39892c2e)

---

### Step 6: Configure API Key
1. Enter the required keys in the configuration cell.
2. Create a new **IBM Cloud API Key** *or* use your team's existing key, then populate the `api_key` parameter.
3. Ensure `api_base` matches your watsonx instance.
4. `DB_Password` is available in *DB Connection Details.boxnote*.

![API Key](https://github.com/user-attachments/assets/44e0ec77-0eb2-4822-8d5e-38e67706f9ae)

> You can also create an API key through the IBM Cloud homepage and save it to your local machine.

![Create Key](https://github.com/user-attachments/assets/9d1f90ef-4da0-493b-bcca-07887e609c56)

---

### Step 7: Run the Notebook
1. Execute the notebook cells sequentially.
2. Several test queries are provided as comments—remove the `#` and run them to test the results.

![Run Notebook](https://github.com/user-attachments/assets/7a5fedd0-7f73-40db-a5eb-4cfdcb92bdce)