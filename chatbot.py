from openai import OpenAI

client= OpenAI(
    api_key="your_groq_api_key",  
    base_url="https://api.groq.com/openai/v1"
)

while True:
    user_input = input("You: ")
    
    if user_input.lower() in ["quit", "exit", "bye"]:
        print("Bot: Goodbye!")
        break

    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an expert data engineering assistant. Respond with accurate, concise, and relevant "
                    "information related to data engineering topics such as data pipelines, ETL/ELT, databases, "
                    "data warehousing, distributed systems, and data processing tools like Apache Spark, Airflow, "
                    "Kafka, and SQL. Avoid answering questions outside of data engineering."
                )
            },
            {"role": "user", "content": user_input}
        ]
    )

    print("Bot:", response.choices[0].message.content)