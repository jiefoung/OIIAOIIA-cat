# OIIAOIIA CAT Game

## 介紹

本專案是一個使用 `Pygame` 和 `OpenCV` 來製作的簡單遊戲，允許玩家控制 **OIIAOIIA 貓咪的動畫**。

當玩家按住 `←` 或 `→` 鍵時，貓咪會播放對應的動畫並同時播放音效。當玩家鬆開按鍵時，貓咪會回到靜態圖片。

---

## 需求

### **環境需求**

- Python 3.x
- `pip` 相關套件（見安裝步驟）

### **安裝所需套件**

請使用以下指令安裝必要的 Python 套件：

```sh
pip install pygame 
```

---

## 使用方式

### **步驟 1：準備檔案**

請確保下列檔案和資料夾存在：

- 影片檔案：`videoplayback.mp4`
- 音效檔案：`sound.mp3`(放在OIIAOIIA frames資料夾裡面)
- 影格資料夾：`OIIAOIIA frames/`（解壓縮圖片檔案後，請創立一個資料夾命名為OIIAOIIA frames）

### **步驟 2：執行程式**

請在終端機或命令提示字元（CMD）執行：

```sh
python OIIAOIIA.py
```

### **步驟 3：遊戲操作**

- \*\*按住 ****`←`**** 或 \*\***`→`** → 貓咪開始 **OIIAOIIA 旋轉動畫** 並播放音效。
- **放開按鍵** → 貓咪回到靜態圖片。

---

## 程式結構

- `OIIAOIIA.py` ：主程式，負責載入圖片、播放音效及遊戲邏輯。
- `OIIAOIIA frames/` ：存放擷取的動畫幀數。
- `sound.mp3` ：貓咪動畫播放時對應的音效。

---

## 主要功能

- **影片影格讀取** : 讀取影格frames資料夾內容，並存成animation_frames。
- **Pygame 動畫播放**：當按下左、右按鍵時，貓咪的動畫會播放對應的影格。
- **音效播放**：當貓咪開始旋轉時播放音效，放開按鍵時停止播放。

---

### **重要**
1. 下載zip壓縮檔後，先打開裡面的OIIAOIIA frames.zip
2. 在桌面上或是你記得的地方創建OIIAOIIA frames資料夾
3. 打開主要OIIAOIIA cat程式，確認裡面程式檔案的路徑是否有對應到

例如放在桌面，檔案路徑應對應到C:\Users\User\Desktop
- frames_dir = r"C:\Users\User\Desktop\OIIAOIIA frames"
- sound_path = r"C:\Users\User\Desktop\OIIAOIIA frames\soundpack.mp3"

---
   
4. 安裝上面所提到的pygame套件
5. 若以上步驟都有進行，即可進行遊戲。

## 未來改進方向
- **新增 UI 介面**。
- **支援遊戲手把操作**。

---

## 聯絡資訊

如果有任何問題或改進建議，請聯絡ig : jiefoung_0818。

