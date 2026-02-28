import os
import json

PATH = "data.json"
data = []
current_stack = []

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
                        with open(path,'r+') as file:
                            dataContent = json.load(file)
                            return dataContent
                        

                    elif(res["operation"] == "append"):
                          with open(path,'a+') as file:
                            with open(path,'r+') as fl:
                                dataContent = json.load(fl)
                            current_stack.append(res['content'])
                            return dataContent
            else:
                return {}
        except BaseException as e :
            print("Error 1",e)
        finally:
             with open(path,'w+') as file:
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
    if(isLoad):
      content = fm.load_json()
      fm.append_json(item)
    else:
      print("Else case")
      fm.append_json(item)  
        

class IOFile:
    def add_content(self,content):
       fm = FileManagement()
       if(os.path.exists(PATH)):
        if(os.path.getsize(PATH) != 0):
            cnt = file_management(fm,content,isLoad=True)
        else:
            cnt = file_management(fm,content,isLoad = False)



    


    



