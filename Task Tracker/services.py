import os
import json
from variable import current_stack,flagDataExist

PATH = "data.json"
data = []
# class FileNotFoundError:
#     pass

def fileIOoperation(func):
    def wrapper(self,*args,**kwargs):

        res = func(self,*args,**kwargs)
        try:
            if(os.path.exists(PATH)):
                    path = str(PATH)
                    if((res["operation"] == 'append') & (os.path.getsize(PATH) == 0)):
                        current_stack.append(res['content'])
# 
                    elif(res["operation"] == "load"):
                        with open(path,'a+') as file:
                            dataContent = json.load(file)
                            if(dataContent not in current_stack):
                                current_stack.append(dataContent)
                            # return dataContent
                            # return dataContent
                        

                    elif(res["operation"] == "append"):
                            current_stack.append(res['content'])
                            
            else:
                return {}
        except json.JSONDecodeError as e:
            print("Error",repr(e))
        except BaseException as e :
            print("Error 1",e)
        finally:
            if(flagDataExist):
                with open(path,'a+') as file:
                    json.dump(current_stack,file,indent=4) 
            else:
                with open(path,'w+') as file:
                        # result = json.load(file)
                        # current_stack+=result
                        json.dump(current_stack,file,indent=4) 

    return wrapper        # with open(PATH,method) as file:

                # with open(`PATH,res["method"]) as file:
                #     dataContent = json.load(file)
                #     print(json.dumps(dataContent, indent=4))
            # except FileNotFoundError as e:
            #     return(e)

            




class FileManagement:
    
    def add_data_to_json(content):
        return 0
    
    @fileIOoperation
    def load_json(self):
        return {
            "operation" : "load"
        }


    @fileIOoperation
    def append_json(self,content):
        return {
            "operation" : "append",
            "content" : content
        }


        

def file_management(fm,item,isLoad = True):
    print("TITLE in filemanagement",item)
    if(isLoad):
      content = fm.load_json()
      fm.append_json(item)
    else:
      print("Else case")
      fm.append_json(item)  
        

class IOFile:
    def __init__(self):
        try:
            with open(PATH,'r+') as file:
                if(os.path.getsize(PATH) !=0 & os.path.exists(PATH)):
                    result = json.load(file)
                    flagDataExist = True
                    # print("Ressssss",result)
                    # current_stack = result
                    with open(PATH,'a+') as file:
                        json.dump(result,file,indent=4)

        except JSONDecodeError as e:
            print("Error",repr(e))
        except BaseException as e:
            print("error",repr(e))
        # finally:
            #  with open(PATH,'w+') as file:
        #             json.dump(current_stack,file,indent=4) 

    def add_content(self,content):
       print("TITLE in add_task in TaskManager class",type(content),"Self",self)
       fm = FileManagement()
       if(os.path.exists(PATH)):
        if(os.path.getsize(PATH) != 0):
            flagDataExist = True
            cnt = file_management(fm,content,isLoad=True)
        else:
            cnt = file_management(fm,content,isLoad = False)



    


    



