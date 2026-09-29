# 🇮🇳 BIS AI Assistant

### AI-Powered Intelligent Assistant for Indian Standards & BIS Services

> A multilingual Retrieval-Augmented Generation (RAG) prototype that helps industries and consumers find relevant information about Bureau of Indian Standards (BIS) standards using natural-language queries.

---

## 🌟 Overview

The **BIS AI Assistant** is an AI-powered prototype designed to make information related to Indian Standards easier to discover and understand.

Instead of manually searching through standards, product manuals, and BIS resources, users can ask questions in natural language.

For example:

**User:**
> Which BIS standard applies to domestic pressure cookers?

**AI:**
> The BIS standard that applies to domestic pressure cookers is IS 2347:2023.

The system uses **Retrieval-Augmented Generation (RAG)** to retrieve relevant information from a BIS knowledge base and then uses a local Large Language Model (LLM) to generate a concise answer.

### Current Language Support

- 🇬🇧 English
- 🇮🇳 Hindi
- 🇮🇳 Marathi

---

# ✨ Key Features

### 🔎 Natural Language BIS Search

Users can ask BIS-related questions naturally without knowing the exact standard number or keywords.

Example:

```text
I manufacture electric food mixers. Which BIS standard applies to my product?

# 🇮🇳 BIS AI Assistant

### AI-Powered Intelligent Assistant for Indian Standards & BIS Services

> A multilingual Retrieval-Augmented Generation (RAG) prototype that helps industries and consumers find relevant information about Bureau of Indian Standards (BIS) standards using natural-language queries.

---

## 🌟 Overview

The **BIS AI Assistant** is an AI-powered prototype designed to make information related to Indian Standards easier to discover and understand.

Instead of manually searching through standards, product manuals, and BIS resources, users can ask questions in natural language.

For example:

**User:**
> Which BIS standard applies to domestic pressure cookers?

**AI:**
> The BIS standard that applies to domestic pressure cookers is IS 2347:2023.

The system uses **Retrieval-Augmented Generation (RAG)** to retrieve relevant information from a BIS knowledge base and then uses a local Large Language Model (LLM) to generate a concise answer.

### Current Language Support

- 🇬🇧 English
- 🇮🇳 Hindi
- 🇮🇳 Marathi

---

# ✨ Key Features

### 🔎 Natural Language BIS Search

Users can ask BIS-related questions naturally without knowing the exact standard number or keywords.

Example:

```text
I manufacture electric food mixers. Which BIS standard applies to my product?

# 🇮🇳 BIS AI Assistant

### AI-Powered Intelligent Assistant for Indian Standards & BIS Services

> A multilingual Retrieval-Augmented Generation (RAG) prototype that helps industries and consumers find relevant information about Bureau of Indian Standards (BIS) standards using natural-language queries.

---

## 🌟 Overview

The **BIS AI Assistant** is an AI-powered prototype designed to make information related to Indian Standards easier to discover and understand.

Instead of manually searching through standards, product manuals, and BIS resources, users can ask questions in natural language.

For example:

**User:**
> Which BIS standard applies to domestic pressure cookers?

**AI:**
> The BIS standard that applies to domestic pressure cookers is IS 2347:2023.

The system uses **Retrieval-Augmented Generation (RAG)** to retrieve relevant information from a BIS knowledge base and then uses a local Large Language Model (LLM) to generate a concise answer.

### Current Language Support

- 🇬🇧 English
- 🇮🇳 Hindi
- 🇮🇳 Marathi

---

# ✨ Key Features

### 🔎 Natural Language BIS Search

Users can ask BIS-related questions naturally without knowing the exact standard number or keywords.

Example:

```text
I manufacture electric food mixers. Which BIS standard applies to my product?
The system can retrieve the relevant standard:
IS 4250:2025


🧠 Retrieval-Augmented Generation (RAG)

The project uses a RAG architecture to generate answers using relevant information retrieved from the BIS knowledge base.

User Question
      ↓
Language Detection
      ↓
Multilingual Embedding
      ↓
Semantic Similarity Search
      ↓
Relevant BIS Information
      ↓
Local LLM
      ↓
Final Answer

🌍 Multilingual Support

The system uses a multilingual embedding model to support queries in English, Hindi and Marathi.

English

Which BIS standard applies to domestic pressure cookers?

Hindi

घरेलू प्रेशर कुकर के लिए कौन सा BIS मानक लागू है?

Marathi

घरगुती प्रेशर कुकरसाठी कोणता BIS मानक लागू आहे?

🏭 Product-Specific BIS Standards

The current knowledge base contains information related to multiple products, including:

Electric Food Mixers
Domestic Pressure Cookers
Industrial Safety Helmets
Safety Footwear
Packaged Drinking Water
Structural Steel
Self-Ballasted LED Lamps

Example:

I manufacture electric food mixers. Which BIS standard applies to my product?

Relevant standard:

IS 4250:2025

🛡️ Hallucination Protection

The system uses a similarity threshold to determine whether sufficiently relevant BIS information is available.

If a question is outside the current knowledge base, the system avoids generating an unsupported answer.

Example:

What are the BIS requirements for aircraft engines?

If relevant information is unavailable, the system returns a safe fallback such as:

I don't have enough information in my BIS knowledge base to answer that.

This helps reduce unsupported AI-generated information.

🔗 BIS Source Information

The knowledge base stores source information along with BIS records, including:

Product / Topic
Indian Standard
Description
Source
Official BIS URL

🏗️ System Architecture

                         ┌───────────────────┐
                         │    User Query     │
                         └─────────┬─────────┘
                                   ↓
                         ┌───────────────────┐
                         │ Language Detection│
                         └─────────┬─────────┘
                                   ↓
                         ┌───────────────────┐
                         │ Multilingual      │
                         │ Embedding Model   │
                         └─────────┬─────────┘
                                   ↓
                         ┌───────────────────┐
                         │ Semantic Similarity│
                         │ Search            │
                         └─────────┬─────────┘
                                   ↓
                         ┌───────────────────┐
                         │ Relevant BIS      │
                         │ Knowledge         │
                         └─────────┬─────────┘
                                   ↓
                         ┌───────────────────┐
                         │ Ollama            │
                         │ Llama 3.2 3B      │
                         └─────────┬─────────┘
                                   ↓
                         ┌───────────────────┐
                         │ Grounded Answer   │
                         └───────────────────┘

🔄 How the RAG Pipeline Works

The project has two main stages.

Stage 1 — Create Embeddings

The raw BIS knowledge base is stored in:

data/bis_sources.json

The create_embeddings.py script converts the BIS information into numerical vectors using the multilingual embedding model.

bis_sources.json
       ↓
create_embeddings.py
       ↓
Multilingual Embedding Model
       ↓
bis_embeddings.json

The generated embeddings are stored in:

data/bis_embeddings.json
Stage 2 — Run the RAG Assistant

Once embeddings are available, the RAG system can process user questions.

User Question
      ↓
Question Embedding
      ↓
Similarity Search
      ↓
Relevant BIS Records
      ↓
Context sent to LLM
      ↓
AI Generated Answer

🧰 Technology Stack
Technology	Purpose
Python -> Main programming language
Sentence Transformers -> Generates multilingual embeddings
paraphrase-multilingual-MiniLM-L12-v2 ->	Multilingual embedding model
Ollama ->	Runs the local LLM
Llama 3.2 3B ->	Local language model
NumPy	Vector and similarity calculations
JSON	Knowledge base and embedding storage
RAG	Retrieval-Augmented Generation architecture
Git & GitHub	Version control and project hosting

🤖 AI Models Used
Multilingual Embedding Model
sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2

This model converts BIS documents and user questions into embeddings.

The embeddings allow the system to compare the meaning of a user's question with information stored in the BIS knowledge base.

Large Language Model
Llama 3.2 3B

The model runs locally using:

Ollama

This allows the prototype to generate answers without requiring a paid cloud LLM API.

📁 Project Structure
bis-ai-assistant/
│
├── data/
│   ├── bis_sources.json
│   └── bis_embeddings.json
│
├── src/
│   ├── load_data.py
│   ├── create_embeddings.py
│   ├── embedding_test.py
│   ├── search_test.py
│   ├── rag_test.py
│   └── ollama_test.py
│
├── .gitignore
├── README.md
└── .env
data/bis_sources.json

Contains the BIS knowledge used by the RAG system.

Each record contains information such as:

Title
Content
Source
URL
data/bis_embeddings.json

Contains the numerical embeddings generated from the BIS knowledge base.

This file is generated using:

src/create_embeddings.py
📂 Source Files
load_data.py

Loads and checks the BIS source data.

create_embeddings.py

Generates multilingual embeddings from the BIS knowledge base.

embedding_test.py

Tests the multilingual embedding model.

search_test.py

Tests semantic similarity search.

rag_test.py

The main RAG prototype.

It:

Detects the user's language.
Loads the BIS embeddings.
Converts the user question into an embedding.
Performs semantic similarity search.
Retrieves relevant BIS information.
Applies a similarity threshold.
Sends relevant context to the local LLM.
Generates a concise answer.
ollama_test.py

Tests communication with the local Ollama model.

⚙️ Installation & Setup
1. Clone the Repository
git clone https://github.com/ashmitha-1130/bis-ai-assistant.git

Move into the project:

cd bis-ai-assistant
2. Create a Python Virtual Environment
python -m venv venv

Activate it:

.\venv\Scripts\Activate.ps1

After activation, the terminal should show something similar to:

(venv) PS D:\BIS_AI>
3. Install Python Dependencies

Install the required packages:

pip install numpy sentence-transformers ollama
Required Python packages
numpy
sentence-transformers
ollama
4. Install and Configure Ollama

Install Ollama and download the required model:

ollama pull llama3.2:3b

Check that the model is installed:

ollama list

You should see:

llama3.2:3b
🚀 Running the Project

There are two important stages:

1. Create Embeddings
2. Run RAG Assistant
Step 1 — Prepare the BIS Knowledge Base

The raw BIS information is stored in:

data/bis_sources.json

This file acts as the knowledge base for the current prototype.

Step 2 — Generate Embeddings

Run:

python src\create_embeddings.py

This script:

Loads BIS data
      ↓
Loads multilingual embedding model
      ↓
Generates embeddings
      ↓
Saves embeddings

The generated file is:

data/bis_embeddings.json
Step 3 — Run the RAG Assistant

After embeddings have been generated, run:

python src\rag_test.py

The assistant will then be ready to process BIS questions.

Example:

Which BIS standard applies to domestic pressure cookers?

🔁 Complete First-Time Setup

For a completely fresh setup, follow this order:

Clone Repository
       ↓
Create Virtual Environment
       ↓
Activate Virtual Environment
       ↓
Install Python Dependencies
       ↓
Install Ollama
       ↓
Download Llama 3.2 3B
       ↓
Run create_embeddings.py
       ↓
Run rag_test.py
       ↓
Ask BIS Questions
Commands
git clone https://github.com/ashmitha-1130/bis-ai-assistant.git

cd bis-ai-assistant

python -m venv venv

.\venv\Scripts\Activate.ps1

pip install numpy sentence-transformers ollama

ollama pull llama3.2:3b

python src\create_embeddings.py

python src\rag_test.py
⚡ Running the Project After Initial Setup

Once the project has been set up and bis_embeddings.json already exists, you normally only need to run:

.\venv\Scripts\Activate.ps1

python src\rag_test.py

You do not need to recreate the embeddings every time.

🔄 When Should Embeddings Be Recreated?

Run:

python src\create_embeddings.py

again when you:

Add new BIS records
Modify existing BIS information
Add new products
Update the knowledge base

Then run:

python src\rag_test.py

The workflow is:

Update BIS Data
      ↓
bis_sources.json
      ↓
create_embeddings.py
      ↓
bis_embeddings.json
      ↓
rag_test.py

If the BIS data has not changed:

Existing Embeddings
      ↓
rag_test.py
🧪 Example Queries
English
Which BIS standard applies to domestic pressure cookers?

Example answer:

The BIS standard that applies to domestic pressure cookers is IS 2347:2023.
Manufacturer Query
I manufacture electric food mixers. Which BIS standard applies to my product?

Relevant standard:

IS 4250:2025
Hindi
मैं इलेक्ट्रिक फूड मिक्सर बनाता हूँ। मेरे उत्पाद के लिए कौन सा BIS मानक लागू है?
Marathi
मी इलेक्ट्रिक फूड मिक्सर बनवतो. माझ्या उत्पादनासाठी कोणता BIS मानक लागू आहे?
Unsupported Query
What are the BIS requirements for aircraft engines?

If relevant information is not available in the knowledge base, the system uses a safe fallback instead of attempting to invent an answer.

Example:

I don't have enough information in my BIS knowledge base to answer that.
🛡️ Grounded Answer Strategy

The system uses a similarity threshold to reduce unsupported answers.

                 User Question
                       ↓
                Semantic Search
                       ↓
                Similarity Score
                       ↓
             ┌─────────┴─────────┐
             ↓                   ↓
       Relevant Enough      Not Relevant
             ↓                   ↓
      Retrieve Context       Safe Fallback
             ↓
            LLM
             ↓
          Answer

Current prototype:

Similarity Threshold = 0.60

A stronger match can also be given higher priority so that unrelated BIS records are not unnecessarily passed to the LLM.

📚 Current BIS Knowledge Base

The current prototype contains information related to:

Product / Resource	Indian Standard
Electric Food Mixers	IS 4250:2025
Domestic Pressure Cookers	IS 2347:2023
Industrial Safety Helmets	IS 2925:1984
Safety Footwear	IS 15298 Part 2:2024
Packaged Drinking Water	IS 14543:2024
Structural Steel	IS 2062 Part 1:2025
Self-Ballasted LED Lamps	IS 16102 Part 1:2012

The knowledge base also contains general BIS resources related to standards, certification and consumer information.

🔐 Security

Sensitive configuration files should not be committed to GitHub.

The .gitignore file protects files such as:

.env
venv/
__pycache__/
*.pyc

Never commit API keys, passwords, access tokens or other secrets.

💻 Why Use a Local LLM?

The prototype uses:

Ollama + Llama 3.2 3B

instead of depending on a paid cloud LLM API.

Benefits include:

No paid API credits required
Local inference
Easy experimentation
Greater control over the model
Suitable for a local development and hackathon environment
🎯 Project Goals

The long-term goal is to build an intelligent assistant that can help both industries and consumers interact with BIS information more easily.

🏭 For Industries

Potential use cases include:

Finding applicable Indian Standards
Searching product-specific standards
Understanding BIS certification information
Finding relevant BIS resources
Asking standards-related questions using natural language
👨‍👩‍👧 For Consumers

Potential use cases include:

Understanding BIS-related information
Finding relevant standards
Searching BIS resources
Asking questions without knowing technical terminology
Accessing standards-related information more easily
🔮 Future Enhancements
1. 📄 Larger BIS Knowledge Base

Expand the knowledge base with more:

Indian Standards
Product manuals
Certification information
Guidelines
FAQs
Consumer resources
2. 🔍 BIS Licence Verification

Add a separate licence verification module where users can enter a BIS licence number and retrieve current information from an appropriate BIS verification source.

Possible information:

Licence Number
Manufacturer
Product
Applicable Indian Standard
Licence Scope
Current Status

This information should be retrieved from a current BIS verification source rather than generated from the LLM.

3. 🌐 Web Interface

Connect the AI backend to a web interface.

Possible workflow:

User enters question
        ↓
AI processes question
        ↓
BIS information retrieved
        ↓
Answer generated
        ↓
Source displayed
4. 🗣️ More Indian Languages

The current prototype focuses on:

English
Hindi
Marathi

Future versions can expand support to additional Indian languages.

5. 📑 PDF-Based Retrieval

Future versions can process BIS documents and product manuals directly.

Possible pipeline:

BIS PDF
   ↓
Text Extraction
   ↓
Document Chunking
   ↓
Embeddings
   ↓
Vector Database
   ↓
Semantic Search
   ↓
LLM
6. 🗄️ Vector Database

As the knowledge base grows, the current JSON-based embedding storage can be replaced with a dedicated vector database.

Possible technologies include:

FAISS
Chroma
Qdrant
Milvus

This would make large-scale semantic search more efficient.

🧩 Current Prototype vs Future System
Current Prototype
BIS JSON Knowledge Base
          ↓
Multilingual Embeddings
          ↓
Similarity Search
          ↓
Relevant BIS Context
          ↓
Ollama / Llama 3.2 3B
          ↓
Grounded Answer

Future System

BIS Documents
      ↓
Document Processing
      ↓
Vector Database
      ↓
RAG Retrieval
      ↓
     LLM
      ↓
BIS Intelligent Assistant
      ↓
Web / Mobile Interface
🏆 Hackathon Value

The prototype demonstrates the core AI capability required for an intelligent BIS assistant:

Natural Language Question
          ↓
Semantic Understanding
          ↓
Relevant BIS Retrieval
          ↓
Grounded Context
          ↓
AI Generated Answer

The architecture is modular, allowing future features such as licence verification, PDF processing, larger knowledge bases, additional languages and web interfaces to be integrated later.
