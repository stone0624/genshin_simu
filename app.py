import streamlit as st
import random

# 標題與主畫面
st.set_page_config(page_title="資料復原期間模擬原神", page_icon="🌌")
st.title("🌌 資料復原期間模擬原神系統")
st.markdown("你目前正在 PhotoRec 還魂中，禁止登入提瓦特。請使用下列模擬系統來抒發悲傷。")

# 角色池設定
characters = [
    {"name": "博士", "rarity": 5, "message": "你抽到了博士。他正在把你USB裡的靈魂拆成sector觀察。"},
    {"name": "納西妲", "rarity": 5, "message": "納西妲問你：你為什麼不備份？"},
    {"name": "多莉", "rarity": 4, "message": "多莉說：要不要買我這顆1TB SSD？只要八百萬摩拉。"},
    {"name": "芭芭拉", "rarity": 4, "message": "芭芭拉正在為你毀損的 .fits 檔唱歌療傷。"},
    {"name": "派蒙", "rarity": 3, "message": "派蒙：欸你那資料夾怎麼叫 trash 啊？"},
    {"name": "凱亞", "rarity": 4, "message": "凱亞：聽說你硬碟快壞了，來點冰元素冷靜一下？"},
    {"name": "鐘離", "rarity": 5, "message": "鐘離：記得，資料長存，靠的是備份與穩固。"},
    {"name": "空氣", "rarity": 1, "message": "你抽到了空氣，也就是你那 114 小時掃描前 60 小時的成果。"},
]

# 抽卡按鈕互動
if st.button("🔮 抽角色"):
    result = random.choices(characters, weights=[2 if c["rarity"] == 5 else 5 if c["rarity"] == 4 else 8 for c in characters])[0]
    st.subheader(f"✨ 你抽到了：{result['name']} ({result['rarity']}★)")
    st.write(result["message"])

# 模擬存檔狀況
with st.expander("📁 查看 trash 資料夾狀況"):
    st.write("目前有：")
    st.markdown("- `recup_dir.1/`: 79 個無法辨識的 JPEG
- `recup_dir.2/`: 1 個 29GB 的 `.fits` 無法打開
- `recup_dir.3/`: 一個你自己都忘記寫過的 `.py` 腳本
- `recup_dir.4/`: `~$報告1.docx` 殘骸
- `recup_dir.5/`: 空的")
    st.info("🧼 別急。正在努力復原中。你可以繼續抽卡，但不能開原神。")

# 一些勵志結語
st.markdown("---")
st.success("再撐一下。你會從 trash 把你未來拉出來的。")
