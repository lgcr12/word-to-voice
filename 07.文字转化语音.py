import jsonpath
import requests
#Cookie需要更换
def get_download_url(text,headers):
    params={
        "content":text,
        "volume":"50",
        "speech_rate":"0",
        "tone_rate":"0",
        "voice": "zhiyan_emo",
        "intensity":"1",
        "mood":""
    }
    res=requests.post(url,data=params,headers=headers)
    res_json=res.json()
    file_path = jsonpath.jsonpath(res_json, '$.data.file_name')[0]
    # print(res_json)
    url_download="https://www.zaixianai.cn/"+file_path
    audio_download(url_download,res)
def audio_download(url_download,res):
    response=requests.get(url_download)
    title=text
    with open("./语音/"+f"{title}.mp3",'wb') as f:
        f.write(response.content)
    if(res.status_code==200):
        print(f"{title}下载完成")
    else:
        print("下载失败")
if __name__=="__main__":
    print("请输入想转换的内容:")
    text=input()
    url="https://www.zaixianai.cn/api/voice/txttovoice"
    headers={
        "Cookie":"PHPSESSID=trj7ca0i4oeuih00ufec4581gl; Hm_lvt_d09fdf7e91f77cddf85908f081d4a3bc=1716715360,1716716203,1716738808,1717566941; Hm_lpvt_d09fdf7e91f77cddf85908f081d4a3bc=1717570846",
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
    }
    get_download_url(text,headers)