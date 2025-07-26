# 🤖 Basic_Chatbot – Data Engineering Assistant (LLaMA 3 via Groq)

A terminal-based chatbot that answers **data engineering-related questions** using the **LLaMA 3** model served through the **Groq API**, using an OpenAI-compatible interface.

---

## 🚀 Features

- Interactive command-line chat loop
- Specialized in **data engineering topics**:
  - ETL/ELT
  - Data Pipelines
  - Apache Spark, Kafka, Airflow
  - SQL, NoSQL, Warehousing (Redshift, Snowflake, BigQuery, etc.)
- Uses `llama3-70b-8192` via Groq’s API

---

## 🛠 Requirements

- Python 3.7 or higher
- [`openai`](https://pypi.org/project/openai/) Python SDK
- A valid [Groq API Key](https://console.groq.com/keys)

---

## 🧑‍💻 Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/AdonisJeswin/Basic_Chatbot.git
   cd Basic_Chatbot

2. **Install Dependencies**:
   ```bash
   pip install openai

3. **Edit the Script**:
   Open `chatbot.py` and replace:

   ```python
   api_key = "your_groq_api_key"
   ```

   with your actual Groq API key.

---

## 💬 Usage

Run the chatbot in your terminal:

```bash
python chatbot.py
```

You’ll see:

```text
You:
```

Start typing your data engineering questions. For example:

```text
You: What is Apache Airflow?
Bot: Apache Airflow is an open-source platform to programmatically author, schedule, and monitor workflows...
```

To exit the chat:

```text
You: exit
Bot: Goodbye!
```

---

## 📁 Project Structure

```
Basic_Chatbot/
├── chatbot.py       # Main chatbot script
├── README.md        # This file
├── LICENSE          # MIT License
└── .gitignore       # Git ignore file
```

---

## 🧪 Example Interaction

```text
You: What is ETL in data engineering?
Bot: ETL stands for Extract, Transform, Load. It's a process used in data pipelines to move data from source systems into a data warehouse...
```

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
You are free to use, modify, and distribute this software with proper attribution.

---
