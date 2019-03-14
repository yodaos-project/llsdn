# pylint: disable=F0401
import lldb

def get_value_type_field(jval):
    return jval & int('7', 16)


def is_value_error_reference(jval):
    return get_value_type_field(jval) == 7


def get_pointer_from_ecma_value(jval):
    jval = jval >> 3
    jval = jval << 3
    first = lldb.target.FindFirstGlobalVariable('jerry_global_heap').GetValueForExpressionPath('.first').AddressOf().value
    first = int(first, 16)
    ptr = jval + first
    return ptr
