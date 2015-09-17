import urllib
import re
def WL2Py(val="Print[\"Welcome to Wolfram programming Cloud\"]"):
    head = "https://www.wolframcloud.com/objects/e946fe************************?x="
    params = urllib.urlencode({'x':val})
    req = urllib.request.urlopen(head,params).read()
    return req
