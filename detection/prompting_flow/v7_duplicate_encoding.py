import openai
from utils.file_utils import read_file
from utils.get_response import get_response
from utils.prompts import get_prompt_for_duplicate_encoding

def run(llm):


    file_name = open(r"work\temp\temp_info.txt", "r").read()
    verilog_code = read_file(file_name)

    prompt= get_prompt_for_duplicate_encoding(verilog_code)

    reply_content = get_response(prompt = prompt, 
                            model = llm, 
                            temperature = 0.1)
    with open(r"work\intermediate_reports\evaluation.txt", "w") as f:
        f.write(reply_content)

    return f"""--- V7: Duplicate Encoding Detection using {llm} ---\n
        {reply_content}"""
