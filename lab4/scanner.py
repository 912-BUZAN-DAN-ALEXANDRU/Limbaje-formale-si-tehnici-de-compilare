from symbol_table import SymbolTable


class Scanner:
    def __init__(self, filename):
        self.__filename = filename
        self.__st = SymbolTable()
        self.__lines = list()
        self.__separators = ['[', ']', '(', ')', '{', '}', ':', ' ']
        self.__operators = ['+', '-', '*', '/', '=', '<', '<=', '==', '>=']
        self.__reserved_words = ['int', 'char', 'array', 'while', 'if', 'else', 'and', 'or', 'not', 'read', 'print']
        self.__types = ['int', 'char']
        self.__digits = ['0','1','2','3','4','5','6','7','8','9']
        self.__letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    def __read_file(self):
        lines = list()
        with open(self.__filename) as f:
            lines = f.readlines()
        for l in lines:
            self.__lines.append(l.split("\n")[0])

    def __is_type(self, type, idx):
        if type in self.__types:
            with open("pif.out", "a+") as f:
                f.write(type + "->(-1,-1)\n")
            return True
        array_toks = type.split("<>")
        if len(array_toks) == 2:
            if array_toks[0] == "array" and array_toks[1] in self.__types:
                with open("pif.out", "a+") as f:
                    f.write("array->(-1,-1)\n")
                    f.write("<->(-1,-1)\n")
                    f.write(array_toks[1] + "->(-1,-1)\n")
                    f.write(">->(-1,-1)\n")
                return True
        raise Exception("Line " + str(idx) + ": Error: Unknown type: " + type)

    def __valid_identifier(self, param, idx):
        if param in self.__reserved_words:
            raise Exception("Line " + str(idx) + ": Error: Identifier not valid: " + param)

        if param[0] in self.__letters:
            if len(param) > 1:
                for s in param[1:]:
                    if s in self.__letters and s in self.__digits:
                        return param
            return param
        raise Exception("Line " + str(idx) + ": Error: Identifier not valid: " + param)

    def __eval(self, val, idx):
        if val[0] == '\'' and val[-1] == '\'':
            return val
        if self.__is_int(val, idx):
            return int(val)

        #TODO implement for expression etc..

    def __is_int(self, val, idx):
        for s in val:
            if s not in self.__digits:
                raise Exception("Line " + str(idx) + ": Error: Integer not valid: " + val)
        return True
    def scan(self):
        self.__read_file()
        for idx in range(len(self.__lines)):
            tokens = self.__lines[idx].split('=')
            if len(tokens) == 2:
                if self.__st.is_in_table(tokens[0].strip()):
                    val = self.__eval(tokens[1].strip(), idx)
                    with open("pif.out", "a+") as f:
                        pos = self.__st.get_position(tokens[0].strip())
                        f.write(tokens[0].strip() + "->(" + str(val) + ',' + str(pos) + ")\n")
                        f.write("=->(-1,-1)\n")

                    self.__st.assign_value(tokens[0].strip(), val)
                    continue
                else:
                    raise Exception(
                        "Line + " + str(idx) + " Error: This identifier '" + tokens[0].strip() + "' does not exist!")

            tokens = self.__lines[idx].split(' ')
            if len(tokens) == 2:
                if self.__is_type(tokens[0].strip(), idx):
                    self.__st.add_element(self.__valid_identifier(tokens[1].strip(), idx), None)
                    with open("pif.out", "a+") as f:
                        f.write(tokens[1].strip() + "->(null," + str(self.__st.get_position(tokens[1].strip())) + ")\n")
                    continue

            for w in self.__operators + self.__separators + self.__reserved_words:
                if w in self.__lines[idx]:
                    with open("pif.out", "a+") as f:
                        f.write(w + "->(-1,-1)\n")


            values = self.__st.get_values()

            with open("st.out", "w") as f:
                for elem in range(len(values)):
                    f.write(str(elem) + ":" + str(values[elem][0]) + "->" + str(values[elem][1]) + "\n")











