
import urllib
import json
import globalData
globalData.init()

def rotoLinkForOffset(offset):
    return 'http://www.rotoworld.com/services/mobile.asmx/GetNews?articleid=' + str(offset) + '&sport=NBA&token=m1rw-xor-434s-bbjt-1'

def generateTestData(fileName, num, articleid):
    arr = []
    lastOffset = articleid
    for i in range(num / 50):
        url = rotoLinkForOffset(lastOffset)
        response = urllib.urlopen(url)
        data = json.loads(response.read())
        arr.extend(map(lambda d: d['HEADLINE'] + ': ' + d['ANALYSIS'], data))
        lastOffset = data[-1]['NEWSID'] - 1
    with open(fileName, 'w') as f:
        for a in arr:
            f.write((',' + '"' + a.replace('&quot;', '\'') + '"').encode("ascii", "ignore").decode('UTF-8') + '\n')
