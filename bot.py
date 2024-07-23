from openai import OpenAI

openai=OpenAI(
    api_key='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
)
def get_gpt_res(user_input):
    message={
        "role":"user",
        "content":user_input
    }
    response=openai.chat.completions.create(
        messages=[message],
        model="gpt-3.5"
    )
    return response.choices[0].message.content

def chat():
    while True:
        user_input=input("You: ")
        if user_input=="exit":
            print("Chatbot :Goodbye!")
            break
        response=get_gpt_res(user_input)
        print(f"Chatbot :{response}")

if __name__=="__main__":
    chat()
        
    
    
    