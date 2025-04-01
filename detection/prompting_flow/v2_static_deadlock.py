import openai
from utils.file_utils import read_file
from utils.get_response import get_response
from utils.prompts import (
    get_prompt_for_static_deadlock,
    get_prompt_for_static_deadlock_phase2,
    get_prompt_for_static_deadlock_phase3
)

def run(llm):
    # Phase 1
    file_name = open(r"work\temp\temp_info.txt", "r").read()
    verilog_code = open(file_name, "r").read()
    prompt1 = get_prompt_for_static_deadlock(verilog_code)
    phase1_output = get_response(prompt = prompt1, 
                            model = llm, 
                            temperature = 0.1)
    with open(r"work\intermediate_reports\evaluation1.txt", "w") as f:
        f.write(phase1_output)

    # Phase 2
    transition_data = read_file(r"work\intermediate_reports\evaluation1.txt")
    prompt2 = get_prompt_for_static_deadlock_phase2(transition_data)
    phase2_output = get_response(prompt = prompt2, 
                               model = llm, 
                               temperature = 0.1)
    with open(r"work\intermediate_reports\evaluation2.txt", "w") as f:
        f.write(phase2_output)

    # Phase 3
    table_data = read_file(r"work\intermediate_reports\evaluation2.txt")
    prompt3 = get_prompt_for_static_deadlock_phase3(table_data)
    phase3_output = get_response(prompt = prompt3, 
                            model = llm, 
                            temperature = 0.1)
    with open(r"work\intermediate_reports\evaluation3.txt", "w") as f:
        f.write(phase3_output)

    return f"""--- V1: Static Deadlock Detection using {llm} ---

--- Phase 1 Output ---
{phase1_output}

--- Phase 2 Output ---
{phase2_output}

--- Phase 3 Output ---
{phase3_output}
"""