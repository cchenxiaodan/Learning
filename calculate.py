class Calculate:
    def add(self, a, b):
        return a + b

    def divide(self, a, b):
        if b == 0:
            return "error"
        else:
            return a / b
