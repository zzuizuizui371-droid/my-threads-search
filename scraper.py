import requests
import json

def scrape():
    # 模拟抓取 Threads 热门数据（通过 RSSHub 转换）
    url = "https://rsshub.app/threads/search/Design.json" 
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        res = requests.get(url, headers=headers)
        items = res.json().get('items', [])
        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(items[:15], f, ensure_ascii=False, indent=2)
        print("Success")
    except:
        print("Failed")

if __name__ == "__main__":
    scrape()
