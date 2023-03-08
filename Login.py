# import logging
# logging.basicConfig(format='%(levelname)s:%(message)s:%(asctime)s',datefmt='%d/%m/%Y %I:%M:%S %p')
# print('Logging started')
# logging.debug('Debug Information')
# logging.info('info Information')
# logging.warning('warning Information')
# logging.error('error Information')
# logging.critical('critical Information')
# print('Logging end')
"""Using Exceptions in Python """
#Example
import logging
logging.basicConfig(filename='sample_log.txt',level=logging.INFO,format='%(asctime)s:%(levelname)s:%(message)s', datefmt='%d/%m/%Y %I: %M: %S:%p')
logging.info('A new Request Came')
try:
   x=int(input('Enter First Number:'))
   y=int(input('Enter Second Number:'))
   print('The Result:',x/y)
except Exception as msg:
   print('Cannot divide with zero' ,msg)
   logging.error(msg)
# except ValueError as msg:
#    print('Please provide int values only')
#    logging.exception(msg)
logging.info('Request Processing Completed')

    
