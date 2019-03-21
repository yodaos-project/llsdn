#!/usr/bin/python
# pylint: disable=F0401

from __future__ import print_function

import lldb
import commands
import optparse
import shlex

import ecma
import llhelper


def jrs_var(debugger, command, result, internal_dict):
    try:
        val = int(command, 10)
    except ValueError:
        frame = llhelper.get_selected_frame(debugger)
        val = frame.FindVariable(command).value
        val = int(val, 10)
    if val is None:
        return
    ecma_debugger = ecma.EcmaDebugger(debugger)
    val = ecma_debugger.get_pointer_from_ecma_value(val)
    val = hex(val)
    print('[DEBUG] val', val, file=result)


def jrs_var_type(debugger, command, result, internal_dict):
    try:
        val = int(command, 10)
    except ValueError:
        frame = llhelper.get_selected_frame(debugger)
        val = frame.FindVariable(command).value
        val = int(val, 10)
    if val is None:
        return
    ecma_debugger = ecma.EcmaDebugger(debugger)
    val_type = ecma_debugger.get_value_type_field(val)
    print('[DEBUG] val type', val_type, file=result)


# And the initialization code to add your commands
def __lldb_init_module(debugger, internal_dict):
    lldb.debugger.HandleCommand('command script add -f llsdn.jrs_var jrs_var')
    lldb.debugger.HandleCommand('command script add -f llsdn.jrs_var_type jrs_var_type')
    print('The llsdn has been loaded and ready to use.')
