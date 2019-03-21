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


class EcmaDebugger:
    def __init__(self, debugger):
        self.debugger = debugger


    def get_value_type_field(self, jval):
        return EcmaType(jval & int('7', 16))


    def is_value_error_reference(self, jval):
        return self.get_value_type_field(jval) == EcmaType.ECMA_TYPE_ERROR


    def get_pointer_from_ecma_value(self, jval):
        jval = jval >> 3
        jval = jval << 3
        first = self.debugger.GetTargetAtIndex(0)
        first = first.FindFirstGlobalVariable('jerry_global_heap').GetValueForExpressionPath('.first').AddressOf().value
        first = int(first, 16)
        ptr = jval + first
        return ptr
