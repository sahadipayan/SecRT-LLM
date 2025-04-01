from detection.prompting_flow import v1_hamming_distance, v2_static_deadlock, v4_dead_state, v5_unreachable_state, v7_duplicate_encoding

def handle_prompting_detection(vulnerability, llm, protected_state=None):
    handlers = {
        "V1 (Hamming Distance)": lambda llm: v1_hamming_distance.run(llm, protected_state),
        "V2 (Static Deadlock)": v2_static_deadlock.run,
        "V4 (Dead State)": v4_dead_state.run,
        "V5 (Unreachable State Detection)": v5_unreachable_state.run,
        "V7 (Duplicate Encoding)": v7_duplicate_encoding.run
    }
    if vulnerability in handlers:
        return handlers[vulnerability](llm)
    return "Error: Unsupported vulnerability"