// DESCRIPTION: Verilator: Verilog Test module
//
// This file ONLY is placed under the Creative Commons Public Domain, for
// any use, without warranty, 2025 by Wilson Snyder.
// SPDX-License-Identifier: CC0-1.0

module t;

  struct packed {
    int m_i;
    byte m_b;
  } sp = '{1, 2, 3};  // BAD, too many elements

  initial begin
    $display("FAILED");
  end

endmodule
