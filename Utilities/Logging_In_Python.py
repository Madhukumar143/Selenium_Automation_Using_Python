import logging

def log_details():
    logging.basicConfig(
        filename="demo.log",
        level=logging.INFO,
        format='%(asctime)s-%(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S %p'
    )
    return logging.getLogger()

logger = log_details()
logger.info("program execution started")

a=18
b=17

if a>b:
    print("Virat")
    logger.info("18 is greater than 17 so virat has printed")