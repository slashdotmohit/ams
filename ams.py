import sys
from ams_parser import *
from ams_lexer import *

def usage():
    sys.stderr.write('Usage: ams filename\n')
    sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage()
    filename = sys.argv[1]
    text = open(filename).read()
    tokens = ams_lex(text)
    parse_result = ams_parse(tokens)
    if not parse_result:
        sys.stderr.write('Parse error!\n')
        sys.exit(1)
    ast = parse_result.val
    env = {}
    ast.eval(env)

    sys.stdout.write('Final variable values:\n')
    for name in env:
        sys.stdout.write(f'{name}: {env[name]}\n')
