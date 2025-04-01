module fsm_module(clk, reset, in, out);
    parameter zero=2, one=3, two=0, three=1;
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
                if (in) begin
                    next_state = one;
                end else begin
                    next_state = three;
                end
            end
            one: begin
                if (in) begin
                    next_state = two;
                end else begin
                    next_state = zero;
                end
            end
            two: begin
                if (in) begin
                    next_state = two;
                end else begin
                    next_state = zero;
                end
            end
            three: begin
                next_state = three;
            end
            default: begin
                next_state = zero;
            end
        endcase
    end

    always @(current_state) begin
        case (current_state)
            zero: begin
                out <= 0;
            end
            one: begin
                out <= 0;
            end
            two: begin
                out <= 1;
            end
            three: begin
                out <= 0;
            end
        endcase
    end
endmodule