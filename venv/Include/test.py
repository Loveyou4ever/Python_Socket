import os, io, sys, re, time, base64, json
import webbrowser, urllib.request

url = "http://is.snssdk.com/api/news/feed/v51/?category=news_hot&refer=1"
stdout = urllib.request.urlopen(url)
weatherInfo = stdout.read().decode('utf-8')

jsonData = json.loads(weatherInfo)
message = jsonData["message"]
print("success: ", message)
total_number = jsonData["total_number"]
print("0: ", total_number)
has_more = jsonData["has_more"]
print("false: ", has_more)
post_content_hint = jsonData["post_content_hint"]
print("分享今日新鲜事: ", post_content_hint)
