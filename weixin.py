#coding:utf-8
from PIL import Image
import qrcode
import matplotlib.pyplot as plt
file=open('aaaa.txt',encoding='utf-8')
name=[]
phone=[]
for line in file:
    name1=line[0:4]
    phone1= line[6:20].strip()
    name.append(name1)
    phone.append(phone1)
    #print name
    #print phone
# vCard内容
# vstr = """
# BEGIN:VCARD
# FN:name[2]
# TEL:010-80008000
# # EMAIL:dtong@gmail.com
# # URL:dtong.gmail.com
# END:VCARD
# """
a=0
while a<len(name):
    vstr ="BEGIN:VCARD"+"\n\tFN:"+name[a]+"\n\tTEL:"+phone[a]+"\n\t EMAIL:"+"liruiping@coagent.com"+"END:VCARD"


    qr = qrcode.QRCode(
 # version值为1~40的整数,控制二维码的大小,(最小值是1,是个12*12的矩阵)
# 如果想让程序自动确定,将值设置为 None 并使用 fit 参数即可
    version=1,
# error_correction: 控制二维码的错误纠正功能,可取值下列4个常量
#   ERROR_CORRECT_L: 大约7%或更少的错误能被纠正
#   ERROR_CORRECT_M(默认): 大约15%或更少的错误能被纠正
#   ERROR_CORRECT_Q: 大约25%或更少的错误能被纠正
#   ERROR_CORRECT_H: 大约30%或更少的错误能被纠正
    error_correction=qrcode.constants.ERROR_CORRECT_L,
# 控制二维码中每个小格子包含的像素数
    box_size=2,
# 控制边框(二维码与图片边界的距离)包含的格子数(默认为4,是相关标准规定的最小值)
    border=20,
    )
# 将vCard数据填入qr
    qr.add_data(vstr)
    qr.make(fit=True)
# 生成图片
    img = qr.make_image()
#    plt.figure("dog")
#    plt.imshow(img)
#    plt.show()
# 将图片存入指定路径文件
    img.save(str(a)+".jpg")
    a=a+1


