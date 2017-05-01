import time

def name_args(f):
    def log(*arg):
        print 'Function Name: ' + f.func_name
        print 'Arguments: ' + str(arg)
        return f(*arg)
    return log

def exec_time(f):
    def log(*arg):
        start = time.time()
        ret = f(*arg)
        end = time.time()
        t = end - start
        print 'Execution Time: ' + str(t)
        return ret
    return log

@name_args
def mult(x, y, z):
    return x * y * z

@exec_time
def squares():
    ret = [0] * 20
    for i in range(1, 21):
        ret[i-1] = i ** 2
    return ret

print mult(3, 4, 5)
print squares()
