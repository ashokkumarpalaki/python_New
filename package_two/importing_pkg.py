from core_python import oops_concept


class ChildClass(oops_concept.Employee):
    def __init__(self):
        print("package2-> ChildClass -> init")


if __name__ == '__main__':
    cc = ChildClass()
