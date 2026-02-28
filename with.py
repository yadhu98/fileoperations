# temp =EXPR
# value = temp.__enter__()
# try:
#     name = value
# finally:
#     temp.__exit__(None,None,None)


# class Manager:
#     def __enter__(self):
#         print("Entering to value")
#         return "SOME VALUE"

#     def __exit__(self,exc_type,exc_value,traceback):
#         print("Exiting the block")
#         print("Exception info:", exc_type, exc_value)
#         return False



# with Manager as m:
#     print("Inside with value",m)

# from contextlib import contextmanager

# @contextmanager
# def my_ctx():
#     try:
#         print("Start")
#         yield 
#     finally:
#         print("Exited")

# with my_ctx():
#     print("HELLO")



setting = {"debug": False}
class ContextManager:
   
        
    def __enter__(self):
        self.oldValue = setting['debug']
        setting["debug"] = True
        return self
    def __exit__(self,exc_type,exc_value,traceback):
        setting["debug"] = self.oldValue
       
        print(self,exc_type,exc_value)
        return False

with ContextManager() as cm:
    print("CM",cm.__dict__,setting)


