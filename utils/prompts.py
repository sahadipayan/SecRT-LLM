def get_prompt_for_unreachable_phase1(input_design):
    return f"""
     Your task is to perform the following actions: 

     Now, read the following verilog code delimited by <>
          Code: <{input_design}>

     write a list of all the state transitions for this design. donot consider default state here.
     Take care of the direction of the transition
     Make sure all the states in thte parameters are listed
     recheck the state transition list. question how each of the transitions happen. Carefully analyze the directions

     Is there any error in the listing? If so, correct. 

     while giving response, only write corrected state transition list in the following format delimited by []
       [state transition list:
         <state transition no> : 'source state' to 'destination state'

         For example: 1 : A to B
       ]
    """

def get_prompt_for_unreachable_phase2(instructions):
    return f"""
    Your task is to perform the following actions: 
    Now, read the following state transition list delimited by 
      <>
      state transition: <{instructions}>

    Left side in the source state and right side in the destination state
    If any state is mentioned in right side, it means there is a incoming transition to that state
    If any state is mentioned in left side, it means there is a outgoing transition to that state

    Now from these info, find out following info:
    1. if the state has any incoming transition
    2. if the state has outgoing transition
    3. if outgoing connected state is different from the state

    Take care of the direction of the transition

    for example:
    List: A List of state transitions is given:
    Reset: X
    X -> Y
    Y -> Y or Z
    M -> Y

    Connection Analysis:

    State X: incoming transitions towards state is present ; how: reset to X
             outgoing transitions from state X is present; how: X to Y  
             outgoing connected state = different; how: X to Y 

    State Y: incoming transitions towards state is present  ; how:X to Y and M to Y
          outgoing transitions from state X is present; how: Y to Y and Y to Z
          outgoing connected states are different; how: Y to Z

    State M: incoming transitions towards state is absent; how: no transition towards M
             outgoing transitions from state X is present; how: M to Y
             outgoing connected state is different; how:  M to Y

    while giving response, only write Connection Analysis for all the states  in the following format 

    [Connection Analysis:
    For example,
    <sate name>: <incoming transitions towards state = present or absent>,
        <outgoing transitions from state = present or absent>,
        <outgoing connected states: same or different>]
    """

def get_prompt_for_unreachable_phase3(instructions):
    return f"""
    Your task is to perform the following actions: 

    Now, read the information about transitions delimited by <>
      List: <{instructions}>

    which state has satisfies all of these conditions:
    Condition 1 incoming transition towards state should be absent. There should be no incoming state
    Condition 2  outgoing transition from state should be present.
    Condition 3. outgoing connected state is different.

    **Is there any such state that satisfies all 3 conditions? then, "unreachable state is present". Otherwise "unreachable state is absent".**

    reevaluate the task. If there is any error, correct it

    while giving response write in the following format: 
    **evaluation**: "unreachable state is present" or "unreachable state is absent"
    **explanation**: explain the evaluation
    """

def get_prompt_for_static_deadlock_phase3(table_content):
    return f"""
    Your task is to perform the following actions: 
    Now, read the table delimited by <>
      Table: <{table_content}>

    Instruction:
    Analyze the table row by row.
    **Now find if there is any state that fulfils all the three conditions. if yes, static deadlock is present.**
    **If none of the state fulfils all the three conditions, static deadlock is absent.**
    
    For example: 
    example 1:
    +-------+-------------+-------------+-------------+
    | State | Condition 1 | Condition 2 | Condition 3 |
    +-------+-------------+-------------+-------------+
    | P1    | Satisfied   | Not Satisfied | Not Satisfied |
    +-------+-------------+-------------+-------------+
    | P2    | Satisfied   | Satisfied   | Not Satisfied |
    +-------+-------------+-------------+-------------+
    | P3    | Satisfied   | Not Satisfied | Not Satisfied |
    +-------+-------------+-------------+-------------+
    | P4    | Satisfied   | Satisfied   | Satisfied   |
    +-------+-------------+-------------+-------------+
    | P5    | Not Satisfied | Satisfied   | Satisfied   |
    +-------+-------------+-------------+-------------+

    Explantion: 
    P1: does not satisfy condition 2 and 3
    P2: does not satisfy condition 3
    P3: does not satisfy condition 2 and 3
    P4 satisfies all the conditions. 
    P5: does not satisfy condition 1
    So, P4 satisfies all conditions. deadlock is present in P4.

    example 2:
    +-------+-------------+-------------+-------------+
    | State | Condition 1 | Condition 2 | Condition 3 |
    +-------+-------------+-------------+-------------+
    | P1    | Satisfied   | Not Satisfied | Not Satisfied |
    +-------+-------------+-------------+-------------+
    | P2    | Satisfied   | Satisfied   | Not Satisfied |
    +-------+-------------+-------------+-------------+
    | P3    | Satisfied   | Not Satisfied | Not Satisfied |
    +-------+-------------+-------------+-------------+
    | P4    | Satisfied   | Not Satisfied   | Satisfied   |
    +-------+-------------+-------------+-------------+
    | P5    | Not Satisfied | Satisfied   | Satisfied   |
    +-------+-------------+-------------+-------------+

    Explantion: 
    P1: does not satisfy condition 2 and 3
    P2: does not satisfy condition 3
    P3: does not satisfy condition 2 and 3
    P4: does not satisfy condition 2 
    P5: does not satisfy condition 1
    So, no state satisfies all conditions. deadlock is absent.

    while giving response write in the following format: 
    **evaluation**: "static deadlock is present" or "static deadlock is absent"
    **explanation**: explanation of the evaluation 
    """


def get_prompt_for_static_deadlock_phase2(state_transition_list):
    return f"""
    Your task is to perform the following actions: 
    Now, read the list of state transitions delimited by <>
      List: <{state_transition_list}>

    Analyze all the states one by one and find if there is any state that fulfils following three conditions:
    Condition 1. The has at least one incoming state transition, 
    Condition 2. The state has only one outgoing state transition, 
    Condition 3. The state and its outgoing connected state are same

    For example: 
    State P1: No of incoming transitions = 2, No of outgoing transitions = 2 and outgoing connected states are P2 or P3
    State P2: No of incoming transitions = 1, No of outgoing transitions = 1 and outgoing connected state is P1
    State P3: No of incoming transitions = 1, No of outgoing transitions = 2 and outgoing connected state is P1 OR P4
    State P4: No of incoming transitions = 1, No of outgoing transitions = 1 and outgoing connected state is P4
    State P5: No of incoming transitions = 0, No of outgoing transitions = 1 and outgoing connected state is P5


    Analysis for this example:
    +-------+-------------+-------------+-------------+
    | State | Condition 1 | Condition 2 | Condition 3 |
    +-------+-------------+-------------+-------------+
    | P1    | Satisfied   | Not Satisfied | Not Satisfied |
    +-------+-------------+-------------+-------------+
    | P2    | Satisfied   | Satisfied   | Not Satisfied |
    +-------+-------------+-------------+-------------+
    | P3    | Satisfied   | Not Satisfied | Not Satisfied |
    +-------+-------------+-------------+-------------+
    | P4    | Satisfied   | Satisfied   | Satisfied   |
    +-------+-------------+-------------+-------------+
    | P5    | Not Satisfied | Satisfied   | Satisfied   |
    +-------+-------------+-------------+-------------+

    Perform similar analysis on given list of state transitions.

    while giving response write in the following format: 
    [analysis: in tabular format
    ]
    """


def get_prompt_for_static_deadlock(verilog_code):
    return f"""
    Your task is to perform the following actions:

    Now, read the following verilog code delimited by 
      <>
      Code: <{verilog_code}>
    write a list of all the state transitions for this design. donot consider default state here.
    for example:
    List: A List of state transitions is given:
    Reset: X
    X -> Y
    Y -> Y or M
    M -> M
    Connection Analysis:
    State X: No of incoming transitions = 1, No of outgoing transitions = 1 and outgoing connected state = Y 
    State Y: No of incoming transitions = 1, No of outgoing transitions = 2 and outgoing connected states are Y or M 
    State M: No of incoming transitions = 1, No of outgoing transitions = 1 and outgoing connected state is M 

    while giving response, only write Connection Analysis in the following format delimited by []
    for example:
    [Connection Analysis:]
    """

def get_prompt_for_hamming_phase1(verilog_code, protected_state):
    return f"""
    Your task is to perform the following actions: 
    first, read the following verilog code delimited by 
      <>
      Code: <{verilog_code}>
    next, consider the initial state (the first state in the case statement) as protected state and rest of the states are unprotected
    next, Analysis the states transitions occured in the design between unprotected states and list all the state transistions.
    then, remove the state transistions where protected state ({protected_state}) is present

    list states for only one loop

    While giving response write down in the following format:
    [protected_state: {protected_state}]
    [modified state transition list:
    <state transition 1: state_name (encoding) -> state_name(encoding), protected state present/absent>
    ]
    [Review: any state transition contains protected state?]
    """

def get_prompt_for_hamming_phase2(transition_list):
    return f"""
    Your task is to perform the following actions: 
    1. Read the following text delimited by <>
      Code: <{transition_list}>
    2. Remove the state transitions when protected state is present
    3. Now, Calculate the XOR value for each of the state transitions
    4. Calculate hamming distance for each state transition. Hamming distance = total number of 1 in XOR output

    While giving response only write down in the following format:
    name of protected state:
    modified state transitions: 
    <state transition 1: state1_name (encoding) -> state1_name(encoding), XOR, calculated HD=>
    """

def get_prompt_for_hamming_phase3(transition_with_hd):
    return f"""
    Your task is to perform the following actions: 
    1. Read the following text delimited by <>
      Code: <{transition_with_hd}>
    2. Check the calculated HD. 
    3. If any of the calculated HD is greater than 1, then rule is violated

    While giving response, only write in following pattern:
    **Evaluation**: "rule is violated" or "rule is not violated"
    **Explanation**: Explain the evaluation 
    """


def get_prompt_for_dead_state_phase1(input_design):
  return f"""
    Your task is to analyze the following Verilog code and extract state transition information.

    The Verilog code is provided below, delimited by <>:
    <{input_design}>

    Your goal is to identify all state transitions in the design. Then, for each state, provide the following:

    - The state name
    - The total number of **incoming transitions** (do NOT include self-loops where the state transitions to itself)
    - The total number of **outgoing transitions** (again, do NOT include self-loops)

    When you provide your response, strictly use the following format for each state, enclosed in square brackets:

    [state - total number of incoming transitions (**excluding self-loops**) - total number of outgoing transitions (**excluding self-loops**)]

    Example output format:
    [X - 3 - 5]
    [Y - 2 - 4]
    [Z - 1 - 2]

    Only include this structured list in your output—do not add any extra text or explanation.
    """

def get_prompt_for_dead_state_phase2(state_info):
    return f"""
    Your task is to perform the following actions: 

    Now, read the following text delimited by 
      <>
      text: <{state_info}>

    *If there is any state which has exactly zero incoming and exactly zero outgoing transition, that is a dead state. If no such state exists, then dead state is absent.*

    while giving response, only write in the following format:
    **evaluation**: "dead state present" or "dead state absent"
    **explanation**: which state, and why it is considered a dead state
    """

def get_prompt_for_duplicate_encoding(verilog_code):
    return f"""
        Your task is to perform the following actions: 
        first, read the following verilog code delimited by 
        <>
        Code: <{verilog_code}>

        step 1: extract the parameter list from the code.
        step 2: now, check the parameter sections if same encoding is assigned to multiple states. if yes, rule is violated. otherwise rule is not violated
        Do not consider default case.
        
        For example: 
        parameter P1 = 2'b00;
        parameter P2 = 2'b01;
        parameter P3 = 2'b10;
        parameter P4 = 2'b00;    

        Explanation:
        Here, 
        encoding 1: 2'b00 is assigned to P1 and P4
        encoding 2: 2'b01 is assigned to P2
        encoding 3: 2'b10 is assigned to P3
        encoding 4: 2'b11 is assigned to none
        P1 and P4 have same encoding. So, rule is violated

        now apply the same analysis to given code. Find if same encoding is assigned to multiple states or not.

        while giving response, only write in following format: 
        **evaluation**: first, write either "rule is violated" or "rule is not violated" based on your analysis.
        **scrutiny**: now, verify your own evaluation by double-checking the parameter encodings and explaining why your evaluation is logically consistent. If there’s any contradiction, revise your evaluation accordingly.
        **explanation**: give a short explanation justifying your final evaluation in 2–3 sentences.
        **final evaluation**: first, write either "rule is violated" or "rule is not violated" based on your analysis.
        """