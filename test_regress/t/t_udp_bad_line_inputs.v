// DESCRIPTION: Verilator: Verilog Test module
//
// This file ONLY is placed under the Creative Commons Public Domain, for
// any use, without warranty, 2025 by Wilson Snyder.
// SPDX-License-Identifier: CC0-1.0

primitive udp_0(output o, input i);
  table
    ? 1 ? 0 0 : 0;  // <--- BAD too many inputs
  endtable
endprimitive
