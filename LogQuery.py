#encoding=utf-8
 
from fabric.api import run,env,local,cd
from fabric.tasks import execute,abort
from fabric.contrib.console import confirm
import logging
 
logging.basicConfig(format='[%(levelname)s]: %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)
logging.getLogger('paramiko.transport').setLevel(logging.ERROR)
logger.setLevel(logging.DEBUG)
 
EXECUTE_RESULT = {}
 
def hosts(hostarr):
    '''
    set hosts
    hostarr:[(hostname,password),(hostname,password)...]
    '''
    env.hosts =  [x[0] for x in hostarr]
    env.passwords = dict(x for x in hostarr)
 
def query(expression,hostname,logfile,unique=True,sort=None,output=None,pattern=None,path=None):
    '''
    expression: regex rule
    hostname: hostname as specified hosts()
    logfile: log file name, wildcard supported, eg:*.log
    unique: whether result is unique
    sort: 1(ASC) or -1(DESC) ,default None
    output:None or file name, default None imply print stream
    pattern: group pattern , default None imply '1'
    path: cd to path before execution
    '''
 
    if not path:
        path = r'.'
    cmd_str = generate_cmd(expression,logfile,unique,sort,output,pattern)
    execute(executor,hostname,cmd_str,path,host=hostname)
    result = EXECUTE_RESULT[hostname]
    return result
 
def aggregate(expression,hostname,logfile,output=None,pattern=None,path=None):
    '''
    expression: regex rule
    hostname: hostname as specified hosts()
    logfile: log file name, wildcard supported, eg:*.log
    output:None or file name, default None imply print stream
    pattern: group pattern , default None imply '1'
    path: cd to path before execution
    '''
    if not path:
        path = r'.'
    cmd_str = generate_cmd(expression,logfile,False,None,output,pattern,True,True)
    execute(executor,hostname,cmd_str,path,host=hostname)
    result = EXECUTE_RESULT[hostname]
    return result
 
def count(expression,hostname,logfile,unique=True,sort=None,output=None,pattern=None,path=None):
    '''
    expression: regex rule
    hostname: hostname as specified hosts()
    logfile: log file name, wildcard supported, eg:*.log
    unique: whether result is unique
    sort: 1(ASC) or -1(DESC) ,default None
    output:None or file name, default None imply print stream
    pattern: group pattern , default None imply '1'
    path: cd to path before execution
    '''
 
    if not path:
        path = r'.'
    cmd_str = generate_cmd(expression,logfile,unique,sort,output,pattern,True)
    execute(executor,hostname,cmd_str,path,host=hostname)
    result = EXECUTE_RESULT[hostname]
    if result:
        result = int(result[0])
    return result
 
 
def executor(hostname,cmd_str,path=None):
    '''
    executor , called by execute
    '''
    if not path:
        path = r'.'
    with cd(path):
        res = run(cmd_str,quiet=True)
        logger.debug('Command: %s:%s > %s'%(hostname,path,cmd_str))
        logger.debug('Command Execute Successful:%s, Failure:%s'%(res.succeeded,res.failed))
        EXECUTE_RESULT[hostname] = res.splitlines()
 
def generate_cmd(expression,logfile,unique=True,sort=None,output=None,pattern=None,count=False,aggregate=False):
    '''
    generate command
    '''
    if not pattern:
        pattern = r'\1'
 
    if aggregate:
        aggregate = '''| awk  '{a[$1]++}END{for (j in a) print j","a[j]}' '''
        unique = False
        sort = False
        count = False
    else:
        aggregate = ''
 
    if not unique:
        unique = ''
    else:
        unique = '| uniq'
 
    if sort:
        if sort==1:
            sort = '| sort'
        elif sort==-1:
            sort = '| sort -r'
        else:
            sort = ''
    else:
        sort = ''
 
    if count:
        count = '| wc -l'
    else:
        count = ''
 
    if output:
        output = '>%s'%output
    else:
        output = ''
 
    cmd_str = '''cat %s | grep "%s" | sed 's/%s/%s/gp' %s %s %s %s %s'''%(logfile,expression,expression,pattern,unique,sort,count,output,aggregate)
    return cmd_str