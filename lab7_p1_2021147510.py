import re


def find_functions(code):

    # find the patterns of function and function calls
    function_form = re.compile(r'\bdef\s+(\w+)\s*\(')
    call_form = re.compile(r'\b(\w+)\s*\(')

    # dictionaris for functions
    functions = {}
    # count every functions
    for match in function_form.finditer(code):
        funct = match.group(1)
        functions[funct] = {'defines': code.count(
            '\n', 0, match.start()) + 1, 'calls': set()}
    # counts the number of function calls for each function
    for match in call_form.finditer(code):
        call = match.group(1)
        if call in functions:
            call_line = code.count('\n', 0, match.start()) + 1
            if call_line != functions[call]['defines']:
                functions[call]['calls'].add(call_line)

    # sort the lines for each function calls
    for funct, data in sorted(functions.items()):
        data['calls'] = sorted(data['calls'])

    return functions


def main():
    input_file = "input_7_1.txt"

    with open(input_file, 'r') as file:
        code = file.read()

    result = find_functions(code)

    for funct, data in sorted(result.items()):
        defines = data['defines']
        calls = data['calls']
        calls_str = ', '.join(map(str, calls))
        print(f"{funct}: def in {defines}, calls in [{calls_str}]")


if __name__ == "__main__":
    main()
