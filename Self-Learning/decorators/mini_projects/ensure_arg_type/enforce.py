def enforce(*types):
    def decorator(f):
        def new_func(*args, **kwargs): #comes in as a tuple
            #convert args into something mutable   
            newargs = []
            test = list(((a, b) for (a, b) in zip(args, types)))
            print(test)
            for (a, t) in zip(args, types):
               newargs.append( t(a)) #feel free to have more elaborated convertion
            return f(*newargs, **kwargs)
        return new_func
    return decorator

@enforce(str, int)#below in message --> will be int and string 
def repeat_msg(msg, times):
	for time in range(times):
		print(msg)

@enforce(float, float)
def divide(a,b):
	print(a/b)
repeat_msg("a", '5')
divide('1', '4')
