"""
Stores all information about different _OPCODES.
"""
import typing

class OpCode(typing.NamedTuple):
	name: str
	removed: int
	added: int
	args: int
	equivalent_function: typing.Optional[typing.Callable]
	infix_operator: typing.Optional[str]
	tags: typing.List[str]
	description: str

_OPCODES = {
        # Stop and Arithmetic Operations
	'00': OpCode(name = 'STOP', removed = 0, added = 0, args = 0, equivalent_function = None, infix_operator = None, tags=['moves'], description="Halts execution."),
	'01': OpCode(name = 'ADD', removed = 2, added = 1, args = 0, equivalent_function = lambda a, b: a + b, infix_operator='+', tags=[], description="Addition operation."),
	'02': OpCode(name = 'MUL', removed = 2, added = 1, args = 0, equivalent_function = lambda a, b: a * b, infix_operator='*', tags=[], description="Multiplication operation."),
	'03': OpCode(name = 'SUB', removed = 2, added = 1, args = 0, equivalent_function = lambda a, b: a - b, infix_operator='-', tags=[], description="Subtraction operation."),
	'04': OpCode(name = 'DIV', removed = 2, added = 1, args = 0, equivalent_function = lambda a, b: a // b, infix_operator='//', tags=[], description="Integer division operation."),
	'05': OpCode(name = 'SDIV', removed = 2, added = 1, args = 0, equivalent_function = lambda a, b: a // b, infix_operator='//', tags=[], description="Signed integer division"),
	'06': OpCode(name = 'MOD', removed = 2, added = 1, args = 0, equivalent_function = lambda a, b: a % b, infix_operator='%', tags=[], description="Modulo"),
	'07': OpCode(name = 'SMOD', removed = 2, added = 1, args = 0, equivalent_function = lambda a, b: a % b, infix_operator='%', tags=[], description="Signed modulo"),
	'08': OpCode(name = 'ADDMOD', removed = 3, added = 1, args = 0, equivalent_function = lambda a, b, c: (a + b) % c, infix_operator=None, tags=[], description="Modulo"),
	'09': OpCode(name = 'MULMOD', removed = 3, added = 1, args = 0, equivalent_function = lambda a, b, c: (a * b) % c, infix_operator=None, tags=[], description="Modulo"),
	'0a': OpCode(name = 'EXP', removed = 2, added = 1, args = 0, equivalent_function = lambda a, b: a ** b, infix_operator='**', tags=[], description="Exponential operation."),
	'0b': OpCode(name = 'SIGNEXTEND', removed = 2, added = 1, args = 0, equivalent_function = None, infix_operator=None, tags=[], description="Extend length of two’s complement signed integer."),
        # Comparison & Bitwise Logic Operations
	'10': OpCode(name = 'LT', removed = 2, added = 1, args = 0, equivalent_function = None, infix_operator='<', tags=[], description="Less-than comparison"),
	'11': OpCode(name = 'GT', removed = 2, added = 1, args = 0, equivalent_function = None, infix_operator='>', tags=[], description="Greater-than comparison"),
	'12': OpCode(name = 'SLT', removed = 2, added = 1, args = 0, equivalent_function = None, infix_operator='<', tags=[], description="Signed less-than comparison"),
	'13': OpCode(name = 'SGT', removed = 2, added = 1, args = 0, equivalent_function = None, infix_operator='>', tags=[], description="Signed greater-than comparison"),
	'14': OpCode(name = 'EQ', removed = 2, added = 1, args = 0, equivalent_function = None, infix_operator='==', tags=[], description="Equality  comparison"),
	'15': OpCode(name = 'ISZERO', removed = 1, added = 1, args = 0, equivalent_function = None, infix_operator=None, tags=[], description="Simple not operator"),
	'16': OpCode(name = 'AND', removed = 2, added = 1, args = 0, equivalent_function = lambda a, b: a & b, infix_operator='&', tags=[], description="Bitwise AND operation."),
	'17': OpCode(name = 'OR', removed = 2, added = 1, args = 0, equivalent_function = lambda a, b: a | b, infix_operator='|', tags=[], description="Bitwise OR operation."),
	'18': OpCode(name = 'XOR', removed = 2, added = 1, args = 0, equivalent_function = lambda a, b: a ^ b, infix_operator='^', tags=[], description="Bitwise XOR operation."),
	'19': OpCode(name = 'NOT', removed = 1, added = 1, args = 0, equivalent_function = lambda a: ~a, infix_operator=None, tags=[], description="Bitwise NOT operation."),
	'1a': OpCode(name = 'BYTE', removed = 2, added = 1, args = 0, equivalent_function = None, infix_operator=None, tags=[], description="Retrieve single byte from word"),
        # SHA3
	'20': OpCode(name = 'SHA3', removed = 2, added = 1, args = 0, equivalent_function = None, infix_operator=None, tags=[], description="Compute Keccak-256 hash."),
        # Environmental Information
	'30': OpCode(name = 'ADDRESS', removed = 0, added = 1, args = 0, equivalent_function = None, infix_operator=None, tags=[], description="Get address of currently executing account."),
	'31': OpCode(name = 'BALANCE', removed = 1, added = 1, args = 0, equivalent_function = None, infix_operator=None, tags=[], description="Get balance of the given account."),
	'32': OpCode(name = 'ORIGIN', removed = 0, added = 1, args = 0, equivalent_function = None, infix_operator=None, tags=[], description="Get execution origination address."),
	'33': OpCode(name = 'CALLER', removed = 0, added = 1, args = 0, equivalent_function = None, infix_operator=None, tags=[], description="Get caller address. This is the address of the account that is directly responsible for this execution."),
	'34': OpCode(name = 'CALLVALUE', removed = 0, added = 1, args = 0, equivalent_function = None, infix_operator=None, tags=[], description="Get deposited value by the instruction/transaction responsible for this execution."),
	'35': OpCode(name = 'CALLDATALOAD', removed = 1, added = 1, args = 0, equivalent_function = None, infix_operator=None, tags=[], description="Get input data of current environment."),
	'36': OpCode(name = 'CALLDATASIZE', removed = 0, added = 1, args = 0, equivalent_function = None, infix_operator=None, tags=[], description="Get size of input data in current environment."),
	'37': OpCode(name = 'CALLDATACOPY', removed = 3, added = 0, args = 0, equivalent_function = None, infix_operator=None, tags=[], description="Copy input data in current environment to memory. This pertains to the input data passed with the message call instruction or transaction."),
	'38': OpCode(name = 'CODESIZE', removed = 0, added = 1, args = 0, equivalent_function = None, infix_operator=None, tags=[], description="Get size of code running in current environment."),
	'39': OpCode(name = 'CODECOPY', removed = 3, added = 0, args = 0, equivalent_function = None, infix_operator=None, tags=[], description="Copy code running in current environment to memory."),
	'3a': OpCode(name = 'GASPRICE', removed = 0, added = 1, args = 0, equivalent_function = None, infix_operator=None, tags=[], description="Get price of gas in current environment."),
	'3b': OpCode(name = 'EXTCODESIZE', removed = 1, added = 1, args = 0, equivalent_function = None, infix_operator=None, tags=[], description="Get size of an account's code."),
	'3c': OpCode(name = 'EXTCODECOPY', removed = 4, added = 0, args = 0, equivalent_function = None, infix_operator=None, tags=[], description="Copy an account's code to memory."),
	'3d': OpCode(name = 'RETURNDATASIZE', removed=0, added=1, args=0, equivalent_function=None, infix_operator=None, tags=[], description=""),
	'3e': OpCode(name = 'RETURNDATACOPY', removed=3, added=0, args=0, equivalent_function=None, infix_operator=None, tags=[], description=""),
        # Block Information
	'40': OpCode(name = 'BLOCKHASH', removed = 1, added = 1, args = 0, equivalent_function = None, infix_operator=None, tags=[], description="Get the hash of one of the 256 most recent complete blocks."),
	'41': OpCode(name = 'COINBASE', removed = 0, added = 1, args = 0, equivalent_function = None, infix_operator=None, tags=[], description="Get the block's beneficiary address."),
	'42': OpCode(name = 'TIMESTAMP', removed = 0, added = 1, args = 0, equivalent_function = None, infix_operator=None, tags=[], description="Get the block's timestamp."),
	'43': OpCode(name = 'NUMBER', removed = 0, added = 1, args = 0, equivalent_function = None, infix_operator=None, tags=[], description="Get the block's number."),
	'44': OpCode(name = 'DIFFICULTY', removed = 0, added = 1, args = 0, equivalent_function = None, infix_operator=None, tags=[], description="Get the block's difficulty."),
	'45': OpCode(name = 'GASLIMIT', removed = 0, added = 1, args = 0, equivalent_function = None, infix_operator=None, tags=[], description="Get the block's gas limit."),
        # Stack, Memory, Storage and Flow Operations
	'50': OpCode(name = 'POP', removed = 1, added = 0, args = 0, equivalent_function = None, infix_operator=None, tags=[], description="Remove item from stack."),
	'51': OpCode(name = 'MLOAD', removed = 1, added = 1, args = 0, equivalent_function = None, infix_operator=None, tags=[], description="Load word from memory."),
	'52': OpCode(name = 'MSTORE', removed = 2, added = 0, args = 0, equivalent_function = None, infix_operator=None, tags=[], description="Save word to memory."),
	'53': OpCode(name = 'MSTORE8', removed = 2, added = 0, args = 0, equivalent_function = None, infix_operator=None, tags=[], description="Save byte to memory."),
	'54': OpCode(name = 'SLOAD', removed = 1, added = 1, args = 0, equivalent_function = None, infix_operator=None, tags=[], description="Load word from storage."),
	'55': OpCode(name = 'SSTORE', removed = 2, added = 0, args = 0, equivalent_function = None, infix_operator=None, tags=[], description="Save word to storage."),
	'56': OpCode(name = 'JUMP', removed = 1, added = 0, args = 0, equivalent_function = None, infix_operator=None, tags=['moves'], description="Alter the program counter."),
	'57': OpCode(name = 'JUMPI', removed = 2, added = 0, args = 0, equivalent_function = None, infix_operator=None, tags=[], description="Alter the program counter if condition was met."),
	'58': OpCode(name = 'PC', removed = 0, added = 1, args = 0, equivalent_function = None, infix_operator=None, tags=[], description="Get the value of the program counter prior to the increment."),
	'59': OpCode(name = 'MSIZE', removed = 0, added = 1, args = 0, equivalent_function = None, infix_operator=None, tags=[], description="Get the size of active memory in bytes."),
	'5a': OpCode(name = 'GAS', removed = 0, added = 1, args = 0, equivalent_function = None, infix_operator=None, tags=[], description="Get the amount of available gas, including the corresponding reduction."),
	'5b': OpCode(name = 'JUMPDEST', removed = 0, added = 0, args = 0, equivalent_function = None, infix_operator=None, tags=[], description="Mark a valid destination for jumps."),
        # 0x60 - 0x7f Stack Push Operations
        # 0x80 - 0x8f Duplication Operations
        # 0x90 - 0x9f Exchange Operations
        # 0xa0 - 0xa4 Logging Operations
        # System Operations
	'f0': OpCode(name = 'CREATE', removed = 3, added = 1, args = 0, equivalent_function = None, infix_operator=None, tags=[], description="Create a new contract account with associated code."),
	'f1': OpCode(name = 'CALL', removed = 7, added = 1, args = 0, equivalent_function = None, infix_operator=None, tags=[], description="Message-call into an account."),
	'f2': OpCode(name = 'CALLCODE', removed = 7, added = 1, args = 0, equivalent_function = None, infix_operator=None, tags=[], description="Message-call into this account with alternative account's code."),
	'f3': OpCode(name = 'RETURN', removed = 2, added = 0, args = 0, equivalent_function = None, infix_operator=None, tags=['moves'], description="Halt execution returning output data."),
	'f4': OpCode(name = 'DELEGATECALL', removed = 6, added = 1, args = 0, equivalent_function = None, infix_operator=None, tags=[], description=""),
	'fa': OpCode(name='STATICCALL', removed=6, added=1, args=0, equivalent_function=None, infix_operator=None, tags=[], description=""),
	'fd': OpCode(name='REVERT', removed=2, added=0, args=0, equivalent_function=None, infix_operator=None, tags=['moves'], description=""),
	'ff': OpCode(name = 'SUICIDE', removed = 1, added = 0, args = 0, equivalent_function = None, infix_operator=None, tags=['moves'], description="Halt execution and register account for deletion.")
}

for i in range(96, 128):
	_OPCODES[hex(i)[2:]] = OpCode(name='PUSH' + str(i - 95), removed=0, added=1, args=i-95, equivalent_function=None, infix_operator=None, tags=[], description="Place " + str(i - 95) + "-byte item on stack.")

for i in range(128, 144):
	_OPCODES[hex(i)[2:]] = OpCode(name='DUP' + str(i - 127), removed=i-127, added=i-126, args=0, equivalent_function=None, infix_operator=None, tags=[], description="Duplicate " + str(i - 127) + ". stack item.")

for i in range(144, 160):
	_OPCODES[hex(i)[2:]] = OpCode(name='SWAP' + str(i - 143), removed=i-142, added=i-142, args=0, equivalent_function=None, infix_operator=None, tags=[], description="Exchange 1. and " + str(i - 142) + ". stack items.")

for i in range(160, 165):
	_OPCODES[hex(i)[2:]] = OpCode(name='LOG' + str(i - 160), removed=i-158, added=0, args=0, equivalent_function=None, infix_operator=None, tags=[], description="Append log record with " + str(i - 160) + " topics.")

for i in range(0, 256):
	if not _OPCODES.get(hex(i)[2:].zfill(2)):
			_OPCODES[hex(i)[2:].zfill(2)] = OpCode(name = 'UNK_' + hex(i)[2:].zfill(2), removed = 0, added = 0, args = 0, equivalent_function = None, infix_operator=None, tags=['moves'], description="Unknown opcode.")

def get_opcode_by_code(sym: str) -> OpCode:
	return _OPCODES[sym]

def get_opcode_by_mnemonic(mne: str) -> OpCode:
	i = 0
	while _OPCODES[hex(i)[2:].zfill(2)].name != mne:
		i += 1
	return _OPCODES[hex(i)[2:].zfill(2)]
