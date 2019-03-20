#!/usr/bin/python
# pylint: disable=F0401

from __future__ import print_function

import lldb
import commands
import optparse
import shlex

import ecma


def jrs_var(debugger, command, result, internal_dict):
    try:
        val = int(command, 10)
    except ValueError:
        val = lldb.frame.FindVariable(command).value
        val = int(val, 10)
    if val is None:
        return
    val = hex(ecma.get_pointer_from_ecma_value(val))
    print('[DEBUG] val', val, file=result)

def jrs_var_type(debugger, command, result, internal_dict):
    try:
        val = int(command, 10)
    except ValueError:
        val = lldb.frame.FindVariable(command).value
        val = int(val, 10)
    if val is None:
        return
    val_type = ecma.get_value_type_field(val)
    print('[DEBUG] val type', val_type, file=result)


# And the initialization code to add your commands
def __lldb_init_module(debugger, internal_dict):
    lldb.debugger.HandleCommand('command script add -f llsdn.jrs_var jrs_var')
    lldb.debugger.HandleCommand('command script add -f llsdn.jrs_var_type jrs_var_type')
    print('The llsdn has been loaded and ready to use.')
