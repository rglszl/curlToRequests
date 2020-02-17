import requests
import shlex
import sys

def curlToRequests(curlCommand):
    parsed = shlex.split(curlCommand)
    url=''
    headers={}
    data=''
    for i in range(0, len(parsed)):
        argument = parsed[i]
        if "curl" == argument:
            i=i+1
            url = parsed[i]
        if "-H" == argument:
            i=i+1
            argument = parsed[i]
            headerKey=argument.split(":")[0].strip()
            headerValue=argument.split(":")[1].strip()
            headers[headerKey]=headerValue
        if "--data" == argument:
            i=i+1
            data=parsed[i]
    return url, headers, data

command=sys.argv[1]
url, headers, data = curlToRequests(command)

print "\n"
print 'url="'+url+'"'
print 'headers='+str(headers)
print 'params='+str(data)
