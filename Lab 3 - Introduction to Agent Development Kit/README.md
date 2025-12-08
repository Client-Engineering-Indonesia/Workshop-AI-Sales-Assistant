# Introduction to Agent Development Kit

This lab is to introduce how the watsonx could configure Agentic AI in the UI that will define them in **code**, attach tools and run them programmatically.<br>

---

By the end of this lab you will be able to:<br>
- Set up and configure the **Agent Development Kit (ADK)** in a Python environment.
- Define an agent (profile, behavior, tools) **in code**.
- Call external tools (APIs / backends) from an ADK agent, reusing the same customer
  and product data as previous labs.
- Run and test the Sales Assistant end-to-end from the command line or notebook.

---

### Step 1: Installing the IBM Watsonx Orchestrate ADK

Before installing the ADK, ensure the following software is installed on your system:<br>

1. Python
- The ADK is written in Python and requires **Python 3.11 or later**
- The **latest compatible version** is Python **3.13**
- For more information and download, visit the [Python website](https://www.python.org/downloads/)

2. Pip
- Pip is Python's package manager and is often included with Python
- If pip is not compliant with your Python installation, please see the [Pip documentation](https://pip.pypa.io/en/stable/installation/)

3.  (Optional) Create a Virtual Environment<br>
&nbsp;Use Python's built-in `venv` module to isolate your environment:

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
source venv/bin/activate  # On Linux/macOS
venv\Scripts\activate     # On Windows
```

---

### Step 2: Installation Steps

1. Install the ADK with pip

```bash
pip install ibm-watsonx-orchestrate
```

2. Test the Installation

```bash
orchestrate --version
```

Configure the following environments based on your needs:

#### Environment 1: New Agentic Incubation
```bash
orchestrate env add -n agentic-inc-3-v2 -u https://api.dl.watson-orchestrate.ibm.com/instances/20250606-1001-3583-008e-cbf8fc63ad50
```

---

### Step 3: Configure watsonx orchestrate

1. Input API key and verify

🔑 **Input WatsonX.orchestrate API key**

> **Note:** The terminal will not display anything when you paste the API key. Simply copy, paste once, and press Enter.

Verify Environment Setup

```bash
orchestrate env list
```

2. Activate Your Environment

```bash
orchestrate env activate agentic-inc-3-v2
```

---

### Step 4: Build Workflow

In this session you will try to deploy collaborator agent from this <a href="https://github.com/IBM/ibm-watsonx-orchestrate-adk/tree/main/examples/flow_builder/get_pet_facts">link</a>

1. Download all the folder inside the Lab 3, i.e., `agents`, `knowledge`, and `tools`

2. Inside the CLI, do command `sh import.sh`

```bash
orchestrate env activate agentic-inc-3-v2

# create tools
orchestrate tools import -k python -f tools/StatsCalculator.py -r tools/requirements.txt

# create knowledge
orchestrate knowledge-bases import -f knowledge/report_extracted.yaml

# create agents
orchestrate agents import -f agents/StatsAgentADK.yaml
orchestrate agents import -f agents/SalesAgentADK.yaml
```

---

### Step 5: Play around to query your ChatBot

<img width="1305" height="860" alt="image" src="https://github.com/user-attachments/assets/5d02c561-6021-40a0-80e5-7b122f92922a" /><br>

Example QNA:
- who is the chairman of the HDB?
- What is the total income and capital expenditure for 2019/2020?
- How many BTO flats were launched, completed, and under construction in FY 2019/2020?
- What is the overall deficit and capital expenditure for FY 2019/2020, and how do they compare with FY 2018/2019?

---

### References:
https://developer.watson-orchestrate.ibm.com/
