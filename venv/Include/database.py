import json
import pymysql
import urllib
from urllib import parse,request

header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',"Content-Type": "application/json"}
url_temperatureIn= 'http://localhost:9091/InsertTempIn'
url_temperatureOut= 'http://localhost:9091/InsertTempOut'
url_humidityIn= 'http://localhost:9091/InsertHumiIn'
url_humidityOut= 'http://localhost:9091/InsertHumiOut'
url_illumination_intensity_in= 'http://localhost:9091/IlluminationInInesrt'
url_illumination_intensity_out= 'http://localhost:9091/IlluminationOutInesrt'
url_ultraviolet_ray= 'http://localhost:9091/UltravioletInsert'
url_air_speed= 'http://localhost:9091/AirSpeedInsert'
url_wind_direction= 'http://localhost:9091/WindDirectionInsert'
url_atmospheric_pressure= 'http://localhost:9091/AtmoPreInsert'

#Database Operation
#conn=pymysql.connect(host='127.0.0.1',user='root',passwd='123456',db='weather',port=3306,charset='utf8')
# cursor = conn.cursor()
# sql = "select * from temperature_indoor"
# cursor.execute(sql)

example_str = "atmos=10111"

key_str = example_str[0:5]
value_str = example_str[6:]
print("key:", key_str)
print("value:", value_str)
#封装json数据格式
#json.dumps({'key':value})
if(key_str == "temp1"):
    temperatureIn = json.dumps({'temperature': value_str}, sort_keys=True, indent=4, separators=(',', ': ')).encode(encoding='utf-8')
    req1 = request.Request(url=url_temperatureIn, data=temperatureIn, headers=header_dict)
    res1 = request.urlopen(req1)
    res1 = res1.read()
    print(res1)
if(key_str == "temp2"):
    temperatureOut = json.dumps({'temperature': value_str}, sort_keys=True, indent=4, separators=(',', ': ')).encode(encoding='utf-8')
    req2 = request.Request(url=url_temperatureOut, data=temperatureOut, headers=header_dict)
    res2 = request.urlopen(req2)
    res2 = res2.read()
    print(res2)
if(key_str == "humi1"):
    humidityIn = json.dumps({'humidity': value_str}, sort_keys=True, indent=4, separators=(',', ': ')).encode(encoding='utf-8')
    req3 = request.Request(url=url_humidityIn, data=humidityIn, headers=header_dict)
    res3 = request.urlopen(req3)
    res3 = res3.read()
    print(res3)
if(key_str == "humi2"):
    humidityOut = json.dumps({'humidity': value_str}, sort_keys=True, indent=4, separators=(',', ': ')).encode(encoding='utf-8')
    req4 = request.Request(url=url_humidityOut, data=humidityOut, headers=header_dict)
    res4 = request.urlopen(req4)
    res4 = res4.read()
    print(res4)
if (key_str == "ligh1"):
    illumination_intensity_in = json.dumps({'illumination': value_str}, sort_keys=True, indent=4,separators=(',', ': ')).encode(encoding='utf-8')
    req5 = request.Request(url=url_illumination_intensity_in, data=illumination_intensity_in, headers=header_dict)
    res5 = request.urlopen(req5)
    res5 = res5.read()
    print(res5)
if (key_str == "ligh2"):
    illumination_intensity_out = json.dumps({'illumination': value_str}, sort_keys=True, indent=4,separators=(',', ': ')).encode(encoding='utf-8')
    req6 = request.Request(url=url_illumination_intensity_out, data=illumination_intensity_out, headers=header_dict)
    res6 = request.urlopen(req6)
    res6 = res6.read()
    print(res6)
if (key_str == "ultra"):
    ultraviolet_ray = json.dumps({'ultraviolet': value_str}, sort_keys=True, indent=4, separators=(',', ': ')).encode(encoding='utf-8')
    req7 = request.Request(url=url_ultraviolet_ray, data=ultraviolet_ray, headers=header_dict)
    res7 = request.urlopen(req7)
    res7 = res7.read()
    print(res7)
if (key_str == "speed"):
    air_speed = json.dumps({'airSpeed': value_str}, sort_keys=True, indent=4, separators=(',', ': ')).encode(encoding='utf-8')
    req8 = request.Request(url=url_air_speed, data=air_speed, headers=header_dict)
    res8 = request.urlopen(req8)
    res8 = res8.read()
    print(res8)
if (key_str == "direc"):
    wind_direction = json.dumps({'windDirection': value_str}, sort_keys=True, indent=4,separators=(',', ': ')).encode(encoding='utf-8')
    req9 = request.Request(url=url_wind_direction, data=wind_direction, headers=header_dict)
    res9 = request.urlopen(req9)
    res9 = res9.read()
    print(res9)
if(key_str == "atmos"):
    atmospheric_pressure = json.dumps({'atmosphericPressure': value_str}, sort_keys=True, indent=4,separators=(',', ': ')).encode(encoding='utf-8')
    req10 = request.Request(url=url_atmospheric_pressure, data=atmospheric_pressure, headers=header_dict)
    res10 = request.urlopen(req10)
    res10 = res10.read()
    print(res10)
























