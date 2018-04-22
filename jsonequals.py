class jsonequals():
    def __init__(self,testjson):
        self.testjson=testjson

    def jsonequals(self):
        a = self.testjson['value1']
        b = self.testjson['value2']
        if a and b:
            if a!=b:
                return False
            for i in range(len(a)):
                if a[i] != b[i]:
                    return False
            return True
        return False










