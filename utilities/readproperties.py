import configparser


config = configparser.RawConfigParser()
config.read('.\\Configurations\\config.ini')

# for every variable we need to create one method

class ReadConfig():
    
    @staticmethod
    def getApplicationUrl(self):
        url= config.get('common info','baseUrl')
        return url
    

    @staticmethod
    def getUseremail():
       
       useremail= config.get('common info','useremail')
       return useremail

    @staticmethod
    def getPassword():
        password= config.get('common info','password')
        return password
    
# these methods need to be called in Test case