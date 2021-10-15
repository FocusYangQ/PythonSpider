class down_email ( ) :

    def __init__ ( self , user , password , email_server ) :

        # 输入邮件地址，口令和POP3服务器地址：
        self.user = user
        # 此处密码是授权码，用于登陆第三方邮件客户端
        self.password = password
        self.pop3_server = email_server

    # 获得msg的编码
    def guess_charset ( self , msg ) :

        charset = msg.get_charset ( )
        if charset is None :
            content_type = msg.get ( 'Content-Type' , '' ).lower ( )
            pos = content_type.find ( 'charset=' )
            if pos >= 0 :
                charset = content_type [ pos + 8 : ].strip ( )
        return charset     

