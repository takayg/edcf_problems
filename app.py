from flask import Flask, render_template, request, logging, Response, redirect, flash
from collections import defaultdict
import requests

contest = {1359:88, 1354:87, 1342:86, 1334:85, 1327:84, 1312:83, 1303:82, 1295:81, 1288:80, 1279:79, 1278:78, 1260:77, 1257:76, 1251:75, 1238:74, 1221:73, 1217:72, 1207:71, 1202:70, 1197:69, 1194:68, 1187:67, 1175:66, 1167:65, 1156:64, 1155:63, 1140:62, 1132:61, 1117:60, 1107:59, 1101:58, 1096:57, 1093:56, 1082:55, 1076:54, 1073:53, 1065:52, 1051:51, 1036:50, 1027:49, 1016:48, 1009:47, 1000:46, 990:45, 44:986, 976:43, 962:42, 961:41, 954:40, 946:39, 938:38, 920:37, 915:36, 911:35, 903:34, 893:33, 888:32, 884:31, 873:30, 863:29, 846:28, 845:27, 837:26, 825:25, 818:24, 817:23, 813:22, 808:21, 803:20, 797:19, 792:18, 762:17, 710:16, 702:15, 691:14, 678:13, 665:12, 660:11, 652:10, 632:9, 628:8, 622:7, 620:6, 616:5, 612:4, 609:3, 600:2, 598:1}
contest_id = set(list(contest.keys()))
# Flaskオブジェクトの生成
app = Flask(__name__)

#「/」へアクセスがあった場合に、「index.html」を返す
@app.route("/")
def index():
    return render_template("index.html", name="takayg", ac={})

@app.route("/", methods=["POST"])
def post():
    name = request.form["name"]
    ac = defaultdict(list)
    user_inf = requests.get("https://codeforces.com/api/user.status?handle=" + name + "&from=1&count=10000").json()
    if "result" not in user_inf.keys():
        return
    for i in range(len(user_inf["result"])):
        if int(user_inf["result"][i]["contestId"]) not in contest_id:
            continue
        if user_inf["result"][i]["verdict"] == "OK":
            ac[contest[int(user_inf["result"][i]["contestId"])]].append(user_inf["result"][i]["problem"]["index"])
    return render_template("index.html", name=name, ac=ac)

if __name__ == '__main__':
    app.run()
