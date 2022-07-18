'''
Test path search - open python interpreter in module_1 path
Try import path_test - fail
manipulate sys.path to add folder 'not_searched' then import - pass

Conclusion: import of modules can be manipulated during runtime 
by modify sys.path, but it's not solid
'''
def found(): 
    print("Python found me!")