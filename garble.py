from google import Google


class Garble():

    def __init__(self):
        self.curr = ""


    def garble(self,content,time = 10):
        print(content)
        print("--------")
        translator = Google()
        self.curr = content
        while(time > 0):
            print("current time is "+str(time))
            self.curr = translator.translate( 'zh-CN', 'fr',self.curr,)
            self.curr = translator.translate( 'fr', 'ko',self.curr,)
            self.curr = translator.translate( 'ko', 'zh-CN',self.curr,)
            time-=1

        return self.curr

if __name__ == '__main__':
    garble= Garble()
    garble_garble = garble.garble("""MySQL是一个关系型数据库管理系统，由瑞典MySQL AB 公司开发，属于 Oracle 旗下产品。MySQL 是最流行的关系型数据库管理系统之一，在 WEB 应用方面，MySQL是最好的 RDBMS (Relational Database Management System，关系数据库管理系统) 应用软件之一。""")
    print(garble_garble)