To create a README file for your project, you should include details about the project's purpose, its structure, how to set it up, and how to use it. Below is a suggested template for your README, focusing on the `core.py` file that contains the code for the compliance checker using a language model.

---

# Compliance Checker API

## Overview
This project provides an API for checking website content against a compliance policy. It uses a language model to analyze the content of a given website and compares it with the provided compliance policy document.

## Core Functionality
The core functionality is handled by `core.py`, which uses the LangChain library to leverage OpenAI's GPT model for compliance checking. The script first index  compliance policy into a vector db and then splits the target website content into manageable segments and compares them to against compliance.

## Prerequisites
- Python 3.9+
- FastAPI
- Uvicorn
- Requests
- BeautifulSoup4
- LangChain
- OpenAI

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/dheerajiiitv/market-checker.git
   ```
2. Navigate to the project directory and install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Application
To start the application, use the following command:
```
uvicorn app:app --reload
```
The API will be accessible at `http://127.0.0.1:8000`.

## Usage
Send a POST request to `/check-compliance/` with the policy URL and the target URL in the request body. The API will return a list of findings regarding the compliance of the target website's content.

