#!/usr/bin/env python3
# DESCRIPTION: Verilator: Verilog Test driver/expect definition
#
# Copyright 2024 by Wilson Snyder. This program is free software; you
# can redistribute it and/or modify it under the terms of either the GNU
# Lesser General Public License Version 3 or the Perl Artistic License
# Version 2.0.
# SPDX-License-Identifier: LGPL-3.0-only OR Artistic-2.0

import vltest_bootstrap

test.scenarios('vlt')
test.pli_filename = "t/uvm/dpi/uvm_dpi.cc"

if re.search(r'clang', test.cxx_version):
    test.skip("uvm_regex.cc from upstream has clang warnings")

test.compile(
    verilator_flags2=["--binary", "--build-jobs 4", "--vpi", "+incdir+t/uvm", test.pli_filename])

test.execute(expect_filename=test.golden_filename)

test.passes()
