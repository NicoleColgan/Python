#assign param a default val to make an optional arg
# if you wanna accept other arguments you can use the args
# kwargs is more useful cause you can pass keyword and value
def greeting(name=None, shout=False, *args, **kwargs):

    #nested function
    def nested():
        print("nested")
    nested()

    print(args)
    print(args[1])
    print(kwargs)
    #see if this argument exists
    print(kwargs.get('a'))

    if name:
        greet = f"Hello {name}"
    else: 
        greet = "Hello"
    if shout:
        print(greet.upper())
    else:
        print(greet)

# if you dont pass a key value, it asssigns from first to last so below would assign nicole to name
#greeting("nicole")
#greeting("num2", True)
#greeting()
# If you wanted to pass in shout but not name, you say so
#greeting(shout=True)
#pass in other arguments
greeting("nic", True, 1,2,3, a=True, b=43)