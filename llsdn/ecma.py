# pylint: disable=F0401
import lldb
from enum32 import Enum

class EcmaType(Enum):
    ECMA_TYPE_DIRECT = 0
    ECMA_TYPE_STRING = 1
    ECMA_TYPE_FLOAT = 2
    ECMA_TYPE_OBJECT = 3
    ECMA_TYPE_DIRECT_STRING = 5
    ECMA_TYPE_ERROR = 7
    ECMA_TYPE_COLLECTION_CHUNK = ECMA_TYPE_ERROR
    ECMA_TYPE_SNAPSHOT_OFFSET = ECMA_TYPE_ERROR


def get_value_type_field(jval):
    return EcmaType(jval & int('7', 16))


def is_value_error_reference(jval):
    return get_value_type_field(jval) == EcmaType.ECMA_TYPE_ERROR


def get_pointer_from_ecma_value(jval):
    jval = jval >> 3
    jval = jval << 3
    first = lldb.target.FindFirstGlobalVariable('jerry_global_heap').GetValueForExpressionPath('.first').AddressOf().value
    first = int(first, 16)
    ptr = jval + first
    return ptr
