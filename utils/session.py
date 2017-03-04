#coding:utf-8

import uuid
import json
import logging

from constants import SESSION_EXPIRES_SECONDS

class Session(object):
    def __init__(self , request_handler_obj):
        self._request_handler = request_handler_obj
        self.session_id = request_handler_obj.get_secure_cookie("session_id")
        print ("aaa %s" % self.session_id)
        if not self.session_id:
            self.session_id = uuid.uuid4().hex
            print("ssss %s" % self.session_id)
            self.data = {}

            request_handler_obj.set_secure_cookie("session_id", self.session_id)

        else:
            try:
                json_data = request_handler_obj.redis.get("sess_%s" % self.session_id)
            except Exception as e:
                logging.error(e)
                raise e
            if not json_data:
                self.data = {}
            else:
                self.data = json.loads(json_data)
    def save(self):
        print "session save"
        json_data = json.dumps(self.data)
        print  self.session_id
        try:
            self._request_handler.redis.setex("sess_%s" %self.session_id, SESSION_EXPIRES_SECONDS, json_data)

        except Exception as e:
            logging.error(e)
            raise e

    def clear(self):
        try:
            self._request_handler.redis.delete("sess_%s" % self.session_id)
        except Exception as e:
            logging.error(e)
        self._request_handler.clear_cookie("session_id")
