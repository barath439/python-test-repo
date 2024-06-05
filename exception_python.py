
import logging
import os

#create a logger string
logging_str="[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_folder="logs"
log_file = "logs/running_log.log"
os.makedirs(log_folder, exist_ok=True)



logging.basicConfig(
    level=logging.INFO, 
    format=logging_str,
    
    handlers=[
        logging.FileHandler(log_file)
    ]
)

logger=logging.getLogger("mylog")



def division(a,b):
    try:
        out= a/b
        return out
    except Exception as e:
        logger.info(e)
        adds=a+b
        print(adds)


result=division(12,0)
print(result)