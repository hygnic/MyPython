# User: hygnic
# Date: 2018/9/5

# 单例对象

class single:
    __v = None

    @classmethod
    def get_instance(cls):
        if cls.__v:
            return cls.__v
        else:
            cls.__v = single()
            return cls.__v
