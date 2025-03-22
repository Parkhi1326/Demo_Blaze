import logging
def test_loggingDemo():
    logger=logging.getLogger(__name__)
    fileHandler=logging.FileHandler('logfile.log')
    formatter=logging.Formatter("%(asctime)s:%(levelname)s:(name)s:%(message)s")
    fileHandler.setFormatter(formatter) # setting the format of log file
    logger.addHandler(fileHandler) #filehandler object

    logger.setLevel(logging.WARNING)
    logger.debug("A debug statement is executed")
    logger.info("Information statement")
    logger.warning("Something is in warning")
    logger.error("A majour error has occured")
    logger.critical("Critical issue")