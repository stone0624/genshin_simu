import streamlit as st
import random

st.set_page_config(page_title="原神模擬器陽春版", page_icon="🌌")
st.title("🌌 原神模擬器.陽春ver")
st.markdown("PhotoRec 招魂法事絕讚進行中，提瓦特立入禁止。")

# 介面
st.markdown("""
<style>
@keyframes moveStars {
    from {transform: translateY(0);}
    to {transform: translateY(-1000px);}
}

[data-testid="stAppViewContainer"]::before {
    content: '';
    position: fixed;
    top: 0;
    left: 0;
    width: 200%;
    height: 200%;
    background: radial-gradient(white 1px, transparent 1px),
                radial-gradient(white 1px, transparent 1px);
    background-size: 100px 100px;
    background-position: 0 0, 50px 50px;
    animation: moveStars 60s linear infinite;
    z-index: -1;
    opacity: 0.2;
}
</style>
""", unsafe_allow_html=True)

# 角色池設定
characters = [
    {"name": "艾爾海森", "rarity": 5, "message": "艾爾海森無視你的哀號告訴你他下班了。"},
    {"name": "卡維", "rarity": 4, "message": "維醬正在被室友氣成風史萊姆。"},
    {"name": "納西妲", "rarity": 5, "message": "納西妲拿出備份好的童話版本為你解壓縮。"},
    {"name": "多莉", "rarity": 4, "message": "多莉熱情地告訴你現在買這顆 1TB SSD 只要八億摩拉~"},
    {"name": "芭芭拉", "rarity": 4, "message": "芭芭拉正在為你毀損的 .fits 檔唱歌療傷。"},
    {"name": "溫迪", "rarity": 5, "message": "溫迪：欸你那資料夾怎麼叫 trash 啊？我來唱一首trash song"},
    {"name": "伊法", "rarity": 4, "message": "不是吧哥們?"},
    {"name": "鐘離", "rarity": 5, "message": "鐘離：記得，資料長存，靠的是備份與穩固。"},
    {"name": "阿帽同學", "rarity": 5, "message": "呵呵，不渡螻蟻----"},
    {"name": "萬葉", "rarity": 6, "message": "葉天帝把全提瓦特的usb聚到一起, 並問你丟的是這顆風usb還是這顆雷usb"},
    {"name": "空氣", "rarity": 1, "message": "你抽到了空氣，也就是你那 150 小時掃描前 60 小時的成果。"}
]

# 顏文字與對話框樣式設定
message_styles = {
    "艾爾海森": {"emoji": "(・_・)", "top": "╔═━━━═╗", "bottom": "╚═━━━═╝"},
    "卡維": {"emoji": "｡ﾟ(ﾟ´Д｀ﾟ)ﾟ｡", "top": "╭――――╮", "bottom": "╰――――╯"},
    "納西妲": {"emoji": "(◕‿◕✿)", "top": "❀❀❀❀❀", "bottom": "❀❀❀❀❀"},
    "多莉": {"emoji": "(๑•̀ㅂ•́)و✧💰", "top": "💎💎💎💎💎", "bottom": "💰💰💰💰💰"},
    "芭芭拉": {"emoji": "(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧", "top": "♪♫♪♫♪", "bottom": "♫♪♫♪♫"},
    "溫迪": {"emoji": "(～￣▽￣)～♪", "top": "🌬️🌬️🌬️", "bottom": "🌬️🌬️🌬️"},
    "伊法": {"emoji": "(╯✧▽✧)╯", "top": "❄️❄️❄️", "bottom": "❄️❄️❄️"},
    "鐘離": {"emoji": "(￣︶￣)↗", "top": "🪨🪨🪨", "bottom": "🪨🪨🪨"},
    "啊帽同學": {"emoji": "(￣︶￣)↗", "top": "🪨🪨🪨", "bottom": "🪨🪨🪨"},
    "萬葉": {"emoji": "(￣︶￣)↗", "top": "🪨🪨🪨", "bottom": "🪨🪨🪨"},
    "空氣": {"emoji": "(。_。)", "top": "░░░░░", "bottom": "░░░░░"},
}

# 抽卡
if st.button("🔮 祈願一次"):
    result = random.choices(
        characters,
        weights=[2 if c["rarity"] == 5 
                 else 5 if c["rarity"] == 4 
                 else 11 for c in characters]
    )[0]
    
    style = message_styles.get(
        result["name"],
        {"emoji": "☆彡", "top": "vvvvvvvv", "bottom": "^^^^^^^^"}
    )

    st.markdown(
    f"""
    <div style='
        align-items: center;
        height: 180px;
        width: 100%;
        background-color: #d8bfd8;
        padding: 20px;
        margin: 30px 0;
        text-align: center;
        animation: fadeIn 2s ease-in-out;
    '>
        🔮 🌀 🪄 🪬 🕯️<br>
        <strong>{result["rarity"]}星角色 {result["name"]} 登場 ✨{style["emoji"]}</strong><br>
        🔮 🌀 🪄 🪬 🕯️<br><br>
        {style["top"]}<br>
        {result["message"]}<br>
        {style["bottom"]}
    </div>

    <style>
        @keyframes fadeIn {{
            from {{opacity: 0; transform: scale(0.9);}}
            to {{opacity: 1; transform: scale(1);}}
    }}
        </style>
    """,
    unsafe_allow_html=True
)

# 模擬 trash 狀態
# 隨機檔名產生器
def random_filename(extension):
    prefixes = ["lost_sector", "USB_ghost", "WIP", "cache", "報告final", "frag"]
    suffixes = ["001", "v2", "dead", "lasthope", "backup", "x928"]
    return f"{random.choice(prefixes)}_{random.choice(suffixes)}.{extension}"

# 檔案類型清單 (name, extension, 數字是 count 還是 size)
trash_types = [
    ("jpeg", "jpg", "count"),
    ("fits", "fits", "size"),
    ("py", "py", "count"),
    ("doc", "docx", "count")
]

# 初始化 trash_state
if "trash_state" not in st.session_state:
    st.session_state.trash_state = {}

# 刷新按鈕
if st.button("🌀 刷新 trash 狀態"):
    new_state = {}
    for name, ext, numtype in trash_types:
        num_key = f"{name}_{'count' if numtype == 'count' else 'size'}"
        file_key = f"{name}_file"
        new_state[num_key] = random.randint(1, 100)
        new_state[file_key] = random_filename(ext)
    st.session_state.trash_state = new_state

# 顯示 trash 狀態
trash = st.session_state.trash_state
with st.expander("📁 查看 trash 資料夾狀況"):
    st.markdown(f"""
- 📂 recup_dir.1/: <span style='color:red'>{trash.get("jpeg_count", 0)}</span> 個無法辨識的 JPEG，例如 `{trash.get("jpeg_file", "")}`  
- 📂 recup_dir.2/: 1 個 <span style='color:red'>{trash.get("fits_size", 0)}GB</span> 的 `.fits` 無法打開，例如 `{trash.get("fits_file", "")}`  
- 📂 recup_dir.3/: <span style='color:red'>{trash.get("py_count", 0)}</span> 個你自己都忘記寫過的 `.py` 檔案，例如 `{trash.get("py_file", "")}`  
- 📂 recup_dir.4/: `~$報告1.docx` 殘骸，共 <span style='color:red'>{trash.get("doc_count", 0)}</span> 段碎片，例如 `{trash.get("doc_file", "")}`  
- 📂 recup_dir.5/: 空的（可共鳴）
""", unsafe_allow_html=True)
    

# 模擬地圖互動
place = [
        "星落湖邊的壞掉硬碟", 
        "孤雲閣的USB插槽", 
        "蒙德圖書館裡的備份幻影",
        "稻妻廢紙堆中的log.txt",
        "草神深淵中的Z碟"
    ]
if "map_options" not in st.session_state:
    st.session_state.map_options = random.sample(place, 3)

if st.button("🔄 刷新探索地點"):
    st.session_state.map_options = random.sample(place, 3)

selected = st.radio("請選擇探索地點", st.session_state.map_options)

# 對應敘述也隨機：
discovery = {
    "星落湖邊的壞掉硬碟": [
        "你發現了一個 2008 年的外接式硬碟，裡面是某人高中時期的音樂資料。",
        "硬碟裡的檔案都叫 `final_final_報告v9(1).docx`。"
    ],
    "孤雲閣的USB插槽": [
        "USB插入後發出金屬尖叫，自動彈出。",
        "你插入了一個裝著 `.fits` 的 USB，結果 Windows 要你格式化它。"
    ],
    "蒙德圖書館裡的備份幻影":  [
        "你發現了一個 2008 年的外接式硬碟，裡面是某人高中時期的音樂資料。",
        "硬碟裡的檔案都叫 `final_final_報告v9(1).docx`。"
    ],
    "稻妻廢紙堆中的log.txt":  [
        "派蒙說:這邊的區域以後再來探索吧",
        "還沒想好"
    ],
    "草神深淵中的Z碟":  [
        "那被理事之心",
        "年輕人悔恨的淚水"
    ]
}

colors = ["#f9f9f9", "#fff7e6", "#e6f7ff", "#f0f0f0", "#fff1f0","#f6ffed", "#fffbe6", "#e8f5e9", "#fff0f6", "#eaeaea"]
color1, color2 = random.sample(colors, 2)

if selected in discovery:
    message = random.choice(discovery[selected])
    st.markdown(
        f"""
        <div style='
        display: flex;
        justify-content: center;
        align-items: center;
        height: 180px;
        width: 100%;
        border: 5px solid {color1};
        border-radius: 10px;
        background-color: {color2};
        padding: 20px;
        margin: 30px 0;
        text-align: center;
        '>
        <strong>📍你在「{selected}」中發現{message}</strong><br><br>
        </div>
        """,
        unsafe_allow_html=True
    )

st.success("再撐一下。你會從深淵撈回 trash 的。")

