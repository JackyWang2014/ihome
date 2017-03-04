#coding:utf-8
import logging
import constants
from handlers.BaseHandler import BaseHandler
from utils.response_code import RET
from utils.commons import required_login
from utils.qiniu_storage import storage
class ProfileHandler(BaseHandler):
    @required_login
    def get(self):
        user_id = self.session.data['user_id']
        try:
            ret = self.db.get("select up_name, up_mobile, up_avatar from ih_user_profile where up_user_id = %s", user_id)
        except Exception as e:
            logging.error(e)
            return self.write({"errcode":RET.DBERR, "errmsg":"get data error"})

        if ret["up_avatar"]:
            img_url = constants.QINIU_URL_PREFIX + ret["up_avatar"]
        else:
            img_url = None

        self.write({"errcode":RET.OK, "errmsg":"OK", "data":{"user_id":user_id, "name":ret["up_name"], "mobile":ret["up_mobile"], "avatar":img_url}})

class AvatarHandler(BaseHandler):
    @required_login
    def post(self):
        files = self.request.files.get("avatar")
        if not files:
            return self.write(dict(errcode=RET.PARAMERR, essmsg="图片未上传"))
        avatar = files[0]["body"]

        try:
            file_name = storage(avatar)
            logging.info(file_name)
        except Exception as e:
            logging.error(e)
            return self.write(dict(errcode=RET.THIRDERR, errmsg="上传失败"))

        user_id = self.session.data["user_id"]

        sql = "update ih_user_profile set up_avatar=%(avatar)s where up_user_id=%(user_id)s"

        try:
            row_count = self.db.execute_rowcount(sql, avatar=file_name, user_id=user_id)
        except Exception as e:
            logging.error(e)
            return self.write(dict(errcode=RET.DBERR, errmsg="保存错误"))
        self.write(dict(errcode=RET.OK, errmsg="保存成功", data="%s%s" % (constants.QINIU_URL_PREFIX, file_name)))

class NameHandler(BaseHandler):
    @required_login
    def post(self):
        user_id = self.session.data["user_id"]
        name = self.json_args.get("name")

        if name in (None, ""):
            return self.write({"errcode":RET.PARAMERR, "errmsg":"params error"})

        try:
            self.db.execute_rowcount("update ih_user_profile set up_name = %s where up_user_id = %s", name, user_id)
        except Exception as e:
            logging.error(e)
            return self.write({"errcode": RET.DBERR, "errmsg": "name has exist"})

        self.session.data["name"] = name

        try:
            self.session.save()
        except Exception as e:
            logging.error(e)
        self.write({"errcode":RET.OK, "errmsg":"OK"})

class AuthHandler(BaseHandler):
    @required_login
    def get(self):
        user_id = self.session.data["user_id"]
        try:
            ret = self.db.get("select up_real_name, up_id_card from ih_user_profile WHERE up_user_id = %s", user_id)
        except Exception as e:
            logging.error(e)
            return self.write({"errcode": RET.DBERR, "errmsg":"get data failed"})
        logging.debug(ret)
        if not ret:
            return self.write({"errcode": RET.NODATA, "errmsg":"no data"})
        self.write({"errcode":RET.OK, "errmsg":"OK", "data":{"real_name":ret.get("up_real_name", ""), "id_card":ret.get("up_id_card", "")}})
    @required_login
    def post(self):
       user_id = self.session.data["user_id"]
       real_name = self.json_args.get("real_name")
       id_card = self.json_args.get("id_card")
       if real_name in (None, "") or id_card in (None, ""):
           return self.write({"errcode":RET.PARAMERR, "errmsg":"params error"})

       try:
           self.db.execute_rowcount("update ih_user_profile set up_real_name=%s, up_id_card=%s where up_user_id = %s ",real_name, id_card, user_id)
       except Exception as e:
           logging.error(e)
           return self.write({"errcode": RET.DBERR, "errmsg": "update failed"})
       self.write({"errcode": RET.OK, "errmsg": "OK"})