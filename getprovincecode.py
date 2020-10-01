# import datetime
# import os
#
# from logger import logger
#
# last_week_start = datetime.date.today() - datetime.timedelta(days=datetime.date.today().weekday() + 7)
#
# class MyConfig:
# 	config = {
# 		'LOG_FILE_PATH':None,
# 		'LOG_FORMAT':None,
# 		"LOG_FILE_FILENAME":None
# 	}
#
# if __name__ == '__main__':
# 	Log = logger("oderaway").init_app(MyConfig)
# 	# os.environ["OD_CELERY_TYPE"] = "True"
# 	Log.e(os.environ.get('OD_CELERY_TYPE'))
# 	Log.e(os.getenv('OD_CELERY_TYPE'))
# 	# Log.e(os.getenv('path'))

import json

with open(r"C:\Users\surface\Desktop\code.txt","r",encoding='utf-8') as f_code:
    city_code = {}
    b = f_code.read()
    pi = b.split("\n\n\n\n\n")
    for pi_ in pi:
        ci = pi_.split("\n")
        for index,ci_ in enumerate(ci):
            area_code_, area_name = ci_.split("=")
            if index == 0:
                pi_name = area_name
                city_code[pi_name] = {
                
                }
            else:
                if city_code[pi_name].get(area_name,None):
                    # raise Exception("发现重名{}".format(area_name))
                    print("发现重名{}".format(area_name))
                city_code[pi_name][area_name] = area_code_
                # city_code[pi_name][area_name+"区"] = area_code_
                # city_code[pi_name][area_name+"市"] = area_code_
                # city_code[pi_name][area_name+"县"] = area_code_
                # city_code[pi_name][area_name + "镇"] = area_code_
                # city_code[pi_name][area_name + "村"] = area_code_
    print(city_code)
    

with open(r"C:\Users\surface\Desktop\province.json","r",encoding='utf-8') as f:
    json_data = [

    ]
    a = json.load(f)
    for _ in a.keys():
        shi_ = a[_]["child"]
        sheng = {
            "name":a[_]["name"],
            "code":_
        }
        print("省：{}".format(sheng))
        json_sheng = {
            "name": a[_]["name"],
            "city":[]
        }
        if shi_:
            for __ in shi_.keys():
                shi = {
                    "name": shi_[__]["name"] if shi_[__]["name"] != "市辖区" else sheng["name"],
                    # "code": __
                }
                area_ = shi_[__]["child"]
                print("  市：{}".format(shi))
                json_shi = {
                    "name":shi_[__]["name"] if shi_[__]["name"] != "市辖区" else sheng["name"],
                    "area":[

                    ]
                }
                if area_:
                    for ___ in area_.keys():
                        area = {
                            "name":area_[___] if area_[___] != "市辖区" else shi["name"],
                        }
                        print("    区：{}".format(area))
                        print(32 * "*")
                        print(a[_]["name"])
                        print(area["name"])
                        print(area["name"][:-1])
                        code = city_code[a[_]["name"]].get(area["name"],None)
                        if code == None:
                            code = city_code[a[_]["name"]].get(area["name"][:-1], None)
                            if code == None:
                                if "彝族" in area["name"]:
                                    code = city_code[a[_]["name"]].get(area["name"].split("彝族")[0], None)
                                if "特区" in area["name"] and code == None:
                                    code = city_code[a[_]["name"]].get(area["name"].split("特区")[0], None)
                                if "仡佬" in area["name"] and code == None:
                                    code = city_code[a[_]["name"]].get(area["name"].split("仡佬")[0], None)
                                if "苗族" in area["name"] and code == None:
                                    code = city_code[a[_]["name"]].get(area["name"].split("苗族")[0], None)
                                if "布依族" in area["name"] and code == None:
                                    code = city_code[a[_]["name"]].get(area["name"].split("布依族")[0], None)
                                if "水族" in area["name"] and code == None:
                                    code = city_code[a[_]["name"]].get(area["name"].split("布依族")[0], None)
                                if "土家族" in area["name"] and code == None:
                                    code = city_code[a[_]["name"]].get(area["name"].split("土家族")[0], None)
                                if "侗族" in area["name"] and code == None:
                                    code = city_code[a[_]["name"]].get(area["name"].split("侗族")[0], None)
                                if "壮族" in area["name"] and code == None:
                                    code = city_code[a[_]["name"]].get(area["name"].split("壮族")[0], None)
                                if "藏族" in area["name"] and code == None:
                                    code = city_code[a[_]["name"]].get(area["name"].split("藏族")[0], None)
                                if "回族" in area["name"] and code == None:
                                    code = city_code[a[_]["name"]].get(area["name"].split("回族")[0], None)
                                if "满族" in area["name"] and code == None:
                                    code = city_code[a[_]["name"]].get(area["name"].split("满族")[0], None)
                                elif code == None:
                                    pass
                        print(code)
                        print(32 * "*")
                        
                        json_qu = {
                            "name":area["name"],
                            "code":code
                            # "code":city_code[a[_]["name"]][___]
                        }
                        json_shi["area"].append(json_qu)
                json_sheng["city"].append(json_shi)
        json_data.append(json_sheng)
    data = json.dumps(json_data,ensure_ascii=False)
    print(data)

with open(r"C:\Users\surface\Desktop\province2.json", "w",encoding="utf-8") as f2:
    f2.write(data)