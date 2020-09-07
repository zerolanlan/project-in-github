import requests
import json

url = 'http://www.toutiao.com/api/pc/feed/?category=news_society&utm_source=toutiao&widen=1&max_behot_time=0&max_behot_time_tmp=0&tadrequire=true&as=A1B5093B4F12B65&cp=59BF52DB0655DE1'
resp = requests.get(url)
print  resp.status_code    

Jdata = json.loads(resp.text)
#print Jdata
news = Jdata['data']

for n in news:
    title = n['title']
    source = n['source']
    groupID = n['group_id']
    print title,'|',source,'|',groupID
    function(t) {
    var e = {};
    e.getHoney = function() {
        var t = Math.floor((new Date).getTime() / 1e3),
            e = t.toString(16).toUpperCase(),
            i = md5(t).toString().toUpperCase();
        if (8 != e.length) return {
            as: "479BB4B7254C150",
            cp: "7E0AC8874BB0985"
        };
        for (var n = i.slice(0, 5), a = i.slice(-5), s = "", o = 0; 5 > o; o++) s += n[o] + e[o];
        for (var r = "", c = 0; 5 > c; c++) r += e[c + 3] + a[c];
        return {
            as: "A1" + s + e.slice(-3),
            cp: e.slice(0, 3) + r + "E1"
        }
    }
