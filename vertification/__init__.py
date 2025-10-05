"""鉴权机制，由Fayeyu或其他拥有权限的用户提供一次性的临时管理员能力（只能进行一次操作）"""
import random,time

codes={}

s="1 2 3 4 5 6 7 8 9 0 a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split()
def generateVerifyCode(userId:str,seed:float=time.time())->str:
    """生成12位鉴权码"""
    random.seed(seed)
    random.shuffle(s)
    out="".join([random.choice(s) for _ in range(12)])
    codes.update({userId:out})
    return out #构思算法
    ...
def validation(userId:str,code:str)->bool:
    "鉴权"
    return (userId in codes.keys())and(codes[userId]==code)
    ...

if __name__=="__main__":
    print(generateVerifyCode("6892513"))
    print(codes)
    print(validation("6892513",codes["6892513"]))