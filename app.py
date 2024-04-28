import replicate
from dotenv import load_dotenv, find_dotenv
from sql_prompt import sql_prompt
import os


# load .env and replicate token
load_dotenv(find_dotenv())
replicate_token = os.getenv('REPLICATE_API_TOKEN')

#configure the replicate with token 
replicate = replicate.Client(api_token=replicate_token)

# Taking user input from user
user_prompt = input("Ask a Question : ")

# input = {
#     "prompt": "Work through this problem step by step:\n\nQ: Sarah has 7 llamas. Her friend gives her 3 more trucks of llamas. Each truck has 5 llamas. How many llamas does Sarah have in total?",
#     "prompt_template": "<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n\nYou are a helpful assistant<|eot_id|><|start_header_id|>user<|end_header_id|>\n\n{prompt}<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n"
# }

input = {
    "prompt": f" {sql_prompt} Work through this problem step by step: \n\nQ: , {user_prompt} ?",
    "prompt_template": "<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n\nYou are a helpful assistant<|eot_id|><|start_header_id|>user<|end_header_id|>\n\n{prompt}<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n"
}



for event in replicate.stream(
    "meta/meta-llama-3-70b-instruct",
    input=input
):
    print(event, end="")
#=> "Let's break this problem down step by step.\n\nStep 1: S...