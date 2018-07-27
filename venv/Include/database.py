import json
import urllib
import pymysql

conn=pymysql.connect(host='127.0.0.1',user='root',passwd='123456',db='weather',port=3306,charset='utf8')
#获取一个游标
cursor = conn.cursor()
sql = "select * from controller"
cursor.execute(sql)
print("cursor.excute:",cursor.rowcount)
#封装json数据格式
#json.dumps({'key':value})
temperatureIn = json.dumps({'temperature': 27.2}, sort_keys=True, indent=4, separators=(',', ': '))
temperatureOut = json.dumps({'temperature': 38.9}, sort_keys=True, indent=4, separators=(',', ': '))
humidityIn = json.dumps({'humidity': 40.1}, sort_keys=True, indent=4, separators=(',', ': '))
humidityOut = json.dumps({'humidity': 35.7}, sort_keys=True, indent=4, separators=(',', ': '))
illumination_intensity_in = json.dumps({'illumination': 200}, sort_keys=True, indent=4, separators=(',', ': '))
illumination_intensity_out = json.dumps({'illumination': 10000}, sort_keys=True, indent=4, separators=(',', ': '))
ultraviolet_ray = json.dumps({'ultraviolet': 10}, sort_keys=True, indent=4, separators=(',', ': '))
air_speed = json.dumps({'airSpeed': 15.0}, sort_keys=True, indent=4, separators=(',', ': '))
wind_direction = json.dumps({'windDirection': "South-East"}, sort_keys=True, indent=4, separators=(',', ': '))
atmospheric_pressure = json.dumps({'atmosphericPressure': 10090}, sort_keys=True, indent=4, separators=(',', ': '))

print (temperatureIn)
print (temperatureOut)
print (humidityIn)
print (humidityOut)
print (illumination_intensity_in)
print (illumination_intensity_out)
print (ultraviolet_ray)
print (air_speed)
print (wind_direction)
print (atmospheric_pressure)








