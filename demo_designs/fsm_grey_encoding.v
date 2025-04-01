module fsm_module(clk, reset, in, out);
    parameter zero = 2'b00;
    parameter one  = 2'b01;
    parameter two  = 2'b11;
    parameter three = 2'b10;

    output out;
    input clk, reset, in;
    reg out;
    reg [1:0] current_state, next_state;

    always @(posedge clk or posedge reset) begin
        if (reset) begin
            current_state <= zero;
        end else begin
            current_state <= next_state;
        end
    end

    always @(current_state or in) begin
        case (current_state)
            zero: begin
                if (in)
                    next_state = one;
                else
                    next_state = three;
            end
            one: begin
                if (in)
                    next_state = two;
                else
                    next_state = zero;
            end
            two: begin
                if (in)
                    next_state = two; 
                else
                    next_state = zero;
            end
            three: begin
                if (in)
                    next_state = zero;
                else
                    next_state = three; 
            end
            default: next_state = zero;
        endcase
    end

    always @(current_state) begin
        case (current_state)
            zero: out <= 0;
            one:  out <= 0;
            two:  out <= 1;
            three:out <= 0;
        endcase
    end
endmodule
