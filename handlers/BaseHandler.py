#coding:utf-8
import json
from tornado.web import RequestHandler, StaticFileHandler
from utils.session import Session
class BaseHandler(RequestHandler):

    @property
    def db(self):
        return self.application.db
    @property
    def redis(self):
        return self.application.redis

    def prepare(self):
        if self.request.headers.get("Content-Type", "").startswith("application/json"):
            self.json_args = json.loads(self.request.body)
        else:
            self.json_args = None

    def set_default_headers(self):
        self.set_header("Content-Type", "application/json; charset=UTF-8")

    def write_error(self, status_code, **kwargs):
        pass

    def get_current_user(self):
        self.session = Session(self)
        return self.session.data
class StaticFileBaseHandler(StaticFileHandler):
    def __init__(self, *args, **kwargs):
        super(StaticFileHandler, self).__init__(*args, **kwargs)
        self.xsrf_token