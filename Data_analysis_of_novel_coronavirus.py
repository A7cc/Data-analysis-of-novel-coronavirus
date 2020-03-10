import re   #正则
import requests     #爬虫
import fake_useragent   #http包
import chardet  #识别编码
import json #字典编码
#网站
url = "https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_pc_3"
#获取http包
params = {
    "User-Agent":fake_useragent.UserAgent().random
}

#获取网站
html = requests.get(url, params)
#设置编码
html.encoding = chardet.detect(html.content)['encoding']
#获取有用数据
list_1 = re.findall(r"{\"city\".*?}", html.text)
#将开头写进文件
with open("H:\\疫情.txt","a") as f:
    f.write("{}\t\t{}\t{}\t{}\t{}\t{}\n".format("城市","确诊","死亡","治愈","新增","现有"))

for i in range(len(list_1)):
    #使用eval函数特性，将str转换成字典
    data = eval(list_1[i])
    #取消待定区域
    if data["city"] == "待确认" or data["city"] == "检疫、隔离及搬运等相关人员":
        continue
    #{"city":"拉萨","confirmed":"1","died":"","crued":"1","confirmedRelative":"0","curConfirm":"0","cityCode":"100"}
    #检测异常
    try:
        #打开文件并写入
        with open("H:\\疫情.txt","a") as f:
            f.write("{}\t\t{}\t{}\t{}\t{}\t{}\n".format(data["city"],data["confirmed"],eval("data['died'] if data['died'] == ' ' else 0"),data["crued"],data["confirmedRelative"],data["curConfirm"]))
        print("{}导入成功！".format(data["city"]))
    #key异常异常
    except KeyError:
        try:
            with open("H:\\疫情.txt","a") as f:
                f.write("{}\t\t{}\t{}\t{}\n".format(data["city"],eval("data['confirmed'] if data['confirmed'] == ' ' else 0"),eval("data['died'] if data['died'] == ' ' else 0"), eval("data['crued'] if data['crued'] == ' ' else 0")))
            print("{}导入成功！".format(data["city"]))
        except:
            print("{}导入失败！".format(data["city"]))
    #所有异常处理
    except Exception:
        print("{}导入失败！".format(data["city"]))
print("成功！")





"""
for i in list_1:
    j = i.encode('ascii').decode('unicode_escape')
    with open("H:\\list.txt", "a") as f:
        f.write(j + "\n")

    print("成功")
#print(re.findall(r"", html.text))
"""