import streamlit as st
import random

st.set_page_config(page_title="資料復原期原神模擬器陽春版", page_icon="🌌")
st.title("🌌 資料復原期原神模擬器.陽春ver")
st.markdown("PhotoRec 招魂法事絕讚進行中，提瓦特立入禁止。")

# 角色池設定
characters = [
    {"name": "艾爾海森", "rarity": 5, "message": "你抽到了艾爾海森。他正在把你USB裡的靈魂拆成sector觀察。"},
    {"name": "卡維", "rarity": 5, "message": "你抽到了卡維。他正在被室友氣成風史萊姆。"},
    {"name": "納西妲", "rarity": 5, "message": "納西妲問你：你為什麼不備份？"},
    {"name": "多莉", "rarity": 4, "message": "多莉說：要不要買我這顆1TB SSD？只要八百萬摩拉。"},
    {"name": "芭芭拉", "rarity": 4, "message": "芭芭拉正在為你毀損的 .fits 檔唱歌療傷。"},
    {"name": "溫迪", "rarity": 3, "message": "溫迪：欸你那資料夾怎麼叫 trash 啊？我來唱一首trash song"},
    {"name": "凱亞", "rarity": 4, "message": "凱亞：聽說你硬碟快壞了，來點冰元素冷靜一下？"},
    {"name": "鐘離", "rarity": 5, "message": "鐘離：記得，資料長存，靠的是備份與穩固。"},
    {"name": "空氣", "rarity": 1, "message": "你抽到了空氣，也就是你那 114 小時掃描前 60 小時的成果。"}
]

# 顏文字與對話框樣式設定
message_styles = {
    "艾爾海森": {"emoji": "(・_・)", "top": "╔═━━━═╗", "bottom": "╚═━━━═╝"},
    "卡維": {"emoji": "｡ﾟ(ﾟ´Д｀ﾟ)ﾟ｡", "top": "╭――――╮", "bottom": "╰――――╯"},
    "納西妲": {"emoji": "(◕‿◕✿)", "top": "❀❀❀❀❀", "bottom": "❀❀❀❀❀"},
    "多莉": {"emoji": "(๑•̀ㅂ•́)و✧💰", "top": "💎💎💎💎💎", "bottom": "💰💰💰💰💰"},
    "芭芭拉": {"emoji": "(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧", "top": "♪♫♪♫♪", "bottom": "♫♪♫♪♫"},
    "溫迪": {"emoji": "(～￣▽￣)～♪", "top": "🌬️🌬️🌬️", "bottom": "🌬️🌬️🌬️"},
    "凱亞": {"emoji": "(╯✧▽✧)╯", "top": "❄️❄️❄️", "bottom": "❄️❄️❄️"},
    "鐘離": {"emoji": "(￣︶￣)↗", "top": "🪨🪨🪨", "bottom": "🪨🪨🪨"},
    "空氣": {"emoji": "(。_。)", "top": "░░░░░", "bottom": "░░░░░"},
}

# 抽卡互動
if st.button("🔮 抽角色"):
    result = random.choices(characters, weights=[2 if c["rarity"] == 5 else 5 if c["rarity"] == 4 else 8 for c in characters])[0]
    style = message_styles.get(result["name"], {"emoji": "☆彡", "top": "╭──────╮", "bottom": "╰──────╯"})
    st.markdown(
    f"""
```
★ {result["rarity"]}星角色獲得！

{style["emoji"]} {result["name"]} 登場！

{style["top"]}
{result["message"]}
{style["bottom"]}
```
""")

# 模擬 trash 狀態
with st.expander("📁 查看 trash 資料夾狀況"):
    st.write("目前有：")

    jpeg_count = random.randint(1, 100)
    fits_size = random.randint(1, 100)
    py_count = random.randint(1, 100)
    doc_count = random.randint(1, 100)

    markdown_text = f"""
- `recup_dir.1/`: {jpeg_count} 個無法辨識的 JPEG，例如 `{random_filename('jpg')}`  
- `recup_dir.2/`: 1 個 {fits_size}GB 的 `.fits` 無法打開，例如 `{random_filename('fits')}`  
- `recup_dir.3/`: {py_count} 個你自己都忘記寫過的 `.py` 腳本，例如 `{random_filename('py')}`  
- `recup_dir.4/`: `~$報告1.docx` 殘骸，共 {doc_count} 段碎片，例如 `{random_filename('docx')}`  
- `recup_dir.5/`: 空的（暫時）
"""

    st.markdown(markdown_text)

# 模擬地圖互動
with st.expander("🗺️ 模擬地圖互動"):
    location = st.radio("選擇地點探索：", ["星落湖邊的壞掉硬碟", "孤雲閣的USB插槽", "蒙德圖書館裡的備份幻影"])
    if location == "星落湖邊的壞掉硬碟":
        st.write("你發現了一個 2008 年的外接式硬碟，裡面是某人高中時期的音樂資料和.txt備忘錄。")
    elif location == "孤雲閣的USB插槽":
        st.write("你試圖將 trash 裡的某個 .fits 插入，但插槽發出悲鳴，USB自我彈出。")
    elif location == "蒙德圖書館裡的備份幻影":
        st.write("一位圖書館員給了你一張紙條，上面寫著『請善用雲端硬碟。』")

st.markdown("---")
st.success("再撐一下。你會從 trash 把你未來拉出來的。")

