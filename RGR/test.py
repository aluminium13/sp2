# @format params {varname}
create_int = """\tint {0} = {1};\n"""
create_double = """\tdouble {} = 0.0;\n"""
create_ptr = """\tvoid *{}"""

#@format params {varname}
call_std_out = """
printf("{0}=%d\\n",{0});
"""

# @format params {operation}

op_to_stack = """
\t\tpop ebx
\t\tpop eax
\t\t{} eax, ebx
\t\tpush eax
"""

single_op_tp_stack = """
\t\tpop ebx
\t\tpop eax
\t\t{} ebx
\t\tpush eax
"""
# @format params {varname}

push_val = """
\t\tmov edx, {}
\t\tpush edx
"""

# @format params {varname}
from_stack = """
\t\tpop edx
\t\tmov {}, edx
"""

push_arr = """
\t\tmov eax, [{0} + 4 * {1}] ; get element by index from array
\t\tpush eax
"""

assign_to_arr_index = """
\t\tpop edx
\t\tmov [{0} + 4 * {1}], edx ; write element by index to array
"""

# "(a+b)-c+4" -> a b + c - 4 +

operations = {"+": "add", "-": "sub", "*": "mul", "/": "div"}
new_vals = []

asm_code = ""


def verify_int(i):
    try:
        int(i)
    except:
        return False
    return True


def verify_double(i):
    try:
        float(i)
    except:
        return False
    return True


def compile(root_node):
    # print(root_node.name)
    if root_node.name in ["int", "double"]:
        asm_code = ""
        for i in root_node._children:
            if root_node.name == "int":
                if '[' in i.name:
                    asm_code += create_int.format(i.name, '{'+','.join(
                        '0' for _ in range(int(i.name.split('[')[1][:-1])))+'}')
                else:
                    asm_code += create_int.format(i.name, 0)
            else:
                asm_code += create_double.format(i.name)
        return "", asm_code, ""
    elif root_node.name == "print":
        return "", "", call_std_out.format(root_node._children[0].name)
    else:
        assign_to = root_node._children[0].name
        assign_from = root_node._children[1]
        asm_code = compile_ar(assign_from.cont)
        if '[' in assign_to:
            ident, index = assign_to.split('[')
            asm_code += assign_to_arr_index.format(ident, eval(index[:-1]))
        else:
            asm_code += from_stack.format(assign_to)
        return asm_code, "", ""


def compile_ar(stack):
    asm_code = ""
    for i in stack:
        if i in ["+", "-"]:
            asm_code += op_to_stack.format(operations[i])
        elif i in ['*', '/']:
            if i == '/':
                asm_code += 'sub edx, edx'
            asm_code += single_op_tp_stack.format(operations[i])
        elif "]" in i:
            print("@at arr:", )
            val, num = i.split("[")
            num = num[:-1]
            print("@compile_arr", val, num)
            asm_code += push_arr.format(val, num)
        else:
            asm_code += push_val.format(i)
    return asm_code
