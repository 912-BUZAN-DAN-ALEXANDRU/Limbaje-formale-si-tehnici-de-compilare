class SymbolTable:
    def __init__(self):
        self.__dict = list()


    def get_element(self, key):
        for idx in range(len(self.__dict)):
            if self.__compare(key, self.__dict[idx][0]) == 0:
                return self.__dict[idx][1]
        raise Exception("This value does not exists!")

    def add_element(self, key, val):
        if len(self.__dict) == 0:
            self.__dict.append((key, val))
            return

        if len(self.__dict) == 1:
            if self.__compare(key, self.__dict[0][0]) == -1:
                self.__dict.append((key, val))
            if self.__compare(key, self.__dict[0][0]) == 1:
                self.__dict.insert(0, (key, val))
            if self.__compare(key, self.__dict[0][0]) == 0:
                raise Exception("This value already exists!")
            return

        if self.__compare(key, self.__dict[-1][0]) == 0:
            raise Exception("This value already exists!")

        if self.__compare(self.__dict[-1][0], key) == 1:
            self.__dict.append((key, val))
            return

        for idx in range(len(self.__dict) - 1):
            if self.__compare(key, self.__dict[idx][0]) == 0:
                raise Exception("This value already exists!")
            if self.__compare(self.__dict[idx][0], key) == 1 and self.__compare(self.__dict[idx + 1][0], key) == -1:
                self.__dict.insert(idx + 1, (key, val))


    def __compare(self, s1, s2):
        lmin = min(len(s1), len(s2))

        for idx in range(lmin):
            if s1[idx] < s2[idx]:
                return 1
            if s2[idx] < s1[idx]:
                return -1

        if lmin == len(s1) and lmin == len(s2):
            return 0

        if lmin == len(s1):
            return 1

        if lmin == len(s2):
            return -1

        return 0

