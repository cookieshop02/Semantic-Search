from groq import Groq



client = Groq(api_key="YOUR_API_KEY")

def generate_response(context, question):

    prompt = f"""
    You are an assistant that answers questions based on the provided context. If you don't know the answer, say you don't know.
    Context: {context}
    Question: {question}
    """

    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    return completion.choices[0].message.content