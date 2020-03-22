# coding:utf-8
# python2
import sys
import urllib
import xml.etree.ElementTree as ET

def getapi(query, orgname):
    url = 'http://www.kkj.go.jp/api/?'
    params = urllib.urlencode(
            {'Query' : query,
             'Organization_Name' : orgname})
    response = urllib.urlopen(url + params)
    return response.read()

def getHits(xmlData):
    root = ET.fromstring(xmlData)
    return root[1].findtext("SearchHits")

def getEachOrg():
    result = ""
    gov_list = ["内閣府","宮内庁","警察庁","金融庁","消費者庁","復興庁","総務省","消防庁","法務省","検察庁","公安調査庁","外務省","財務省","国税庁","文部科学省","文化庁","スポーツ庁","厚生労働省","農林水産省","林野庁","水産庁","経済産業省","資源エネルギー庁","特許庁","中小企業庁","国土交通省","観光庁","気象庁","海上保安庁","環境省","防衛省","防衛装備庁"]
    print ("結果書き込み中")
    for gov in gov_list:
        print (".", end="")
        xml = getapi('', gov)
        result += (gov + "," + getHits(xml) + "\n")
    return result

if __name__ == '__main__':
    res = getEachOrg()
    f = open('out.csv', 'w')
    f.write(res)
    f.close()

