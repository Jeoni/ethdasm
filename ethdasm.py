import argparse
from ethdasm.contract import Contract
from ethdasm.parse import Parser

parser = argparse.ArgumentParser()
parser.add_argument('input', help='input hex file to parse')
parser.add_argument('--decompile', action='store_true', help='decompiles the contract into a python-like pseudo-code')
parser.add_argument('--disassemble', action='store_true', help='disassemble contract into simplified op-codes')
parser.add_argument('--no-desc', dest='no_desc', action='store_true', help='omit description')
parser.add_argument('--no-opt', dest='no_opt', action='store_true', help='disable optimizations')
parser.add_argument('--out', type=str, help='outputs to a file; outputs to STDOUT if not specified')
args = parser.parse_args()

with open(args.input, 'r') as contract:
    contract_data = contract.read()
    contract_data = contract_data.replace('0x', '')
    contract_data = contract_data.lower()
    if args.decompile:
        contract = Contract(contract_data)
        blocks = contract.parse()
        output = ''
        for lines in blocks:
            output += str(lines) + '\n'
            for line in lines.lines:
                output += "\t" * lines.indentation_level + '{1}'.format(hex(line.address), str(line)) + '\n'
            output += '\n'
    else:
        blocks = Parser.parse(contract_data, args)
        output = ""
        for block in blocks:
            output += '\n'
            output += '; Procedure ' + hex(block.address) + '\n'
            for operation in block.instructions:
                output += '[{: >8}]'.format(hex(operation.address))
                output += ' | {0: <20}'.format(operation.instruction.name)
                output += ' | {0: <75}'.format('{0}'.format(list(map(hex, operation.arguments)) if operation.arguments != None else None))
                if not args.no_desc:
                    output += ' | {0}'.format(operation.instruction.description)
                output += '\n'
    if args.out:
        with open(args.out, 'w') as output_file:
            output_file.write(output)
    else:
        print(output)
    
