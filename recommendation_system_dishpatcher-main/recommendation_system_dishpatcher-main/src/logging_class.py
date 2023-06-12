import logging
import environ
import os


class logging_information():
    
    """
    Description: This class implements logger function for debugging the errors and keep track
                 of the logs.
    
    Args:
        
        log_file:
                type:<String>
                Description: It takes the log file path as an argument from the .env file.
        
       message:
                type:<String>
                Description: It takes the log message to be logged
                
    Functions:
        
        Description: This classimplements two function which are
        
                        1. Logger_function_info():
                           
                                           Descriptions: It logs the  information in the log file.
                                           
                        2. Logger_function_warning():
                           
                                           Descriptions: It logs the warning information in the log file.  
                                           
                        3.Logger_function_critical():
                                          
                                           Descriptions: It logs the warning information in the log file.
                        
                           
    """
    
    def __init__(self,log_message):
        
        """
        Description: This constructor is used to initialise the message.
        
        Args:

            log_message:
                    type:<String>
                    Description: It takes the log message.
        
        """
        
        self.log_message=log_message
        
        
        #env path
        
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        File_Path = BASE_DIR +"/.env"
        
        env = environ.Env()
        environ.Env.read_env(File_Path)
        
        # #log_file
    
        self.BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        
        self.log_file=File_Path = self.BASE_DIR + env("log_file_path")
        
        
    def Logger_function_warning(self):
        
        """
        This wil log the warning information of this module in the log file
        """
        
        logging.basicConfig(filename=self.log_file, filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',datefmt='%d-%b-%y %H:%M:%S')
        logging.warning(self.log_message)  
        
    def Logger_function_info(self):
        
        """
        This wil log the warning information of this module in the log file
        """
        
        logging.basicConfig(filename=self.log_file, filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',datefmt='%d-%b-%y %H:%M:%S')
        logging.info(self.log_message) 
        
        
    def Logger_function_critical(self):
        
        """
        This wil log the warning information of this module in the log file
        """
        
        logging.basicConfig(filename=self.log_file, filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',datefmt='%d-%b-%y %H:%M:%S')
        logging.critical(self.log_message)          
            
   