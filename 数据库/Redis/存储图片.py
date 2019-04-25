import redis
import base64

# 图片转文字

with open("E:\wcc\图片\dlam.png", "rb") as f:  # 打开01.png图片
    # b64encode是编码，b64decode是解码
    base64_data = base64.b64encode(f.read())  # 读取图片转换的二进制文件，并给赋值
    # base64.b64decode(base64data)
    print(base64_data)
    r = redis.Redis(host='127.0.0.1', port=6379, password=682240)
    r.set("save_pic_test_2", base64_data)

    # var = r.get("save_pic_test_2")
    # print(var)
    # data = base64.b64decode(var)  # 把二进制文件解码，并复制给data
    # with open("E:\wcc\图片\jd.jpeg", "wb") as f:  # 写入生成一个jd.png
    #     f.write(data)
