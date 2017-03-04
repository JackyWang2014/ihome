import os
from handlers.BaseHandler import StaticFileBaseHandler as StaticFileHandler
from handlers import Passport, VerifyCode, Profile
from handlers import House
urls = [
    (r"/api/check_login", Passport.CheckLoginHandler),
    (r"/api/register", Passport.RegisterHandler),
    (r"/api/login", Passport.LoginHandler),
    (r"/api/logout", Passport.LogoutHandler),
    (r"/api/smscode", VerifyCode.SMSCodeHandler),
    (r"/api/piccode", VerifyCode.PicCodeHandler),
    (r"/api/house/area", House.AreaInfoHandler),
    (r"/api/profile/avatar", Profile.AvatarHandler),
    (r"/api/profile/name", Profile.NameHandler),
    (r"/api/profile",Profile.ProfileHandler),
    (r"/api/profile/auth", Profile.AuthHandler),
    (r"^/api/house/info$", House.HouseInfoHandler),
    (r"^/api/house/image$", House.HouseImageHandler),
    (r"^/api/house/my$", House.MyHouseHandler),
    (r"^/api/house/index$", House.IndexHandler),
    (r"^/api/house/list$", House.HouseListHandler),
    (r"^/api/house/list2", House.HouseListRedisHandler),
    (r"/(.*)",StaticFileHandler, dict(path=os.path.join(os.path.dirname(__file__), "html"), default_filename = "index.html"))]