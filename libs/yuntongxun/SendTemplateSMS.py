#coding=gbk
import logging

#coding=utf-8

#-*- coding: UTF-8 -*-  

from CCPRestSDK import REST
import ConfigParser

#���ʺ�
accountSid= '8a216da85a60ae8d015a635a9b640075';

#���ʺ�Token
accountToken= 'bdb94da9255c4c5ea67f46e1d1d30e92';

#Ӧ��Id
appId='8a216da85a60ae8d015a635a9bc3007a';

#�����ַ����ʽ���£�����Ҫдhttp://
serverIP='app.cloopen.com';

#����˿� 
serverPort='8883';

#REST�汾��
softVersion='2013-12-26';

  # ����ģ�����
  # @param to �ֻ�����
  # @param datas �������� ��ʽΪ���� ���磺{'12','34'}���粻���滻���� ''
  # @param $tempId ģ��Id

# def sendTemplateSMS(to,datas,tempId):
#
#
#     #��ʼ��REST SDK
#     rest = REST(serverIP,serverPort,softVersion)
#     rest.setAccount(accountSid,accountToken)
#     rest.setAppId(appId)
#
#     result = rest.sendTemplateSMS(to,datas,tempId)
#     for k,v in result.iteritems():
#
#         if k=='templateSMS' :
#                 for k,s in v.iteritems():
#                     print '%s:%s' % (k, s)
#         else:
#             print '%s:%s' % (k, v)
    
   
#sendTemplateSMS(�ֻ�����,��������,ģ��Id)
class CCP(object):
    def __init__(self):
        self.rest = REST(serverIP, serverPort, softVersion)
        self.rest.setAccount(accountSid, accountToken)
        self.rest.setAppId(appId)

    @staticmethod
    def instance():
        if not hasattr(CCP, "_instance"):
            CCP._instance = CCP()
        return CCP._instance

    def sendTemplateSMS(self, to, datas, tempId):
        try:
            result = self.rest.sendTemplateSMS(to, datas, tempId)
        except Exception as e:
            logging.error(e)
            raise e
        print result
        if result.get("statusCode") == "000000":
            return True
        else:
            return False

ccp = CCP.instance()

if __name__ == "__main__":
    ccp = CCP.instance()
    ccp.sendTemplateSMS("15375366009", ["1234", 5], 1)


