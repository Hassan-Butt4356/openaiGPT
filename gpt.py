import openai
from decouple import config
openai.api_key=config('API_KEY')

# user_input=input('Enter your prompt :  ')

# response = openai.ChatCompletion.create(
#   model="gpt-3.5-turbo",
#   messages=[
#         {"role": "user", "content": user_input},
#     ]
# )

# print(response)

chat_log=[]
while True:
    user_input=input('User Prompt : ')
    if user_input.lower()=='quit':
        break
    else:
        chat_log.append({'role':'user','content':user_input})
        response=openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            # We have to pass chat_log so that it remember previous context
            messages=chat_log
        )

        assistant_Response=response['choices'][0]['message']['content'].strip('\n').strip()
        print('Assisttant Response : ',assistant_Response)
        chat_log.append({'role':'assistant','content':assistant_Response})

print(chat_log)