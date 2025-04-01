module fsm_counter(
    input clk,          
    input reset,        
    input in,           
    output reg out      
);

    parameter S0 = 3'b000,  
              S1 = 3'b001,  
              S2 = 3'b010,  
              S3 = 3'b011,  
              S4 = 3'b100,  
              S5 = 3'b101,  
              S6 = 3'b110,  
              S7 = 3'b111;  

    reg [2:0] current_state, next_state;

    always @(posedge clk) begin
        if (reset)
            current_state <= S0;
        else
            current_state <= next_state;
    end

    always @(current_state or in) begin
        case (current_state)
            S0: begin
                if (in)
                    next_state = S1;
                else
                    next_state = S0;
            end
            S1: begin
                if (in)
                    next_state = S2;
                else
                    next_state = S0;
            end
            S2: begin
                if (in)
                    next_state = S3;
                else
                    next_state = S0;
            end
            S3: begin
                if (in)
                    next_state = S4;
                else
                    next_state = S0;
            end
            S4: begin
                if (in)
                    next_state = S5;
                else
                    next_state = S0;
            end
            S5: begin
                if (in)
                    next_state = S6;
                else
                    next_state = S0;
            end
            S6: begin
                if (in)
                    next_state = S7;
                else
                    next_state = S0;
            end
            S7: begin
                if (in)
                    next_state = S7;  
                else
                    next_state = S0;
            end
            default: begin
                next_state = S0;
            end
        endcase
    end

    always @(current_state) begin
        case (current_state)
            S7: out = 1'b1;      
            default: out = 1'b0; 
        endcase
    end

endmodule