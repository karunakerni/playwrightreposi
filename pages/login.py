
class ApiLoginPage:
        LOGIN_ENDPOINT = "/api/auth/login"
        
        def __init__(self,context):
         self.context=context

        def url_API_login(self,email,password):
            response = self.context.request.post(self.LOGIN_ENDPOINT,
                       headers={"content-type": "application/json"},
                       data={"email": email, "password": password})   
                               
            if "token" in response.json():
                token = response.json()["token"]
                return token
            else:
             print("There is no token-Login failed")
             #print("hi")
             return None
            
        

        
                                                        
                                                
                                    
                                    

                              
                        
                                              
                        
