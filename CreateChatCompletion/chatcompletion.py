import os
python_path = os.path.dirname(os.path.realpath(__file__))
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "Hello!"}
  ]
)
python_path = os.path.dirname(os.path.realpath(__file__)) + "\\chatcompletion.py"
print(python_path) # This is just to show the path of the file.
print(completion) # This is just to show the completion object.
""" The output of the above code is:  """
print(completion.choices[0].message)
