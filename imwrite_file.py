import pygame
import os
import shutil
import cv2

# 嘗試導入 OpenCV，如未安裝則提示
##   import cv2
#except ImportError:
##  exit()

# 設定影片路徑與幀數儲存路徑
video_path = r"C:\Users\User\Desktop\程式\python\OIIAOIIA cat\videoplayback.mp4"
frames_dir = r"C:\Users\User\Desktop\OIIAOIIA frames"

# 確保幀數資料夾存在
if not os.path.exists(frames_dir):
    os.makedirs(frames_dir)

# 嘗試開啟影片
video_capture = cv2.VideoCapture(video_path)
video_capture.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'mp4v'))

if not video_capture.isOpened():
    print(f"[錯誤] 無法開啟影片: {video_path}")
    print("請檢查影片是否存在，或轉換為 H.264 格式。")
    exit()

# 測試擷取第一幀
ret, frame = video_capture.read()
if ret:
    test_frame_path = os.path.join(frames_dir, "test_frame.png")
    cv2.imwrite(test_frame_path, frame)
    print(f"[成功] 已成功擷取第一幀並儲存為 {test_frame_path}")
else:
    print("[錯誤] 無法擷取影片的第一幀，可能是格式或解碼器問題。")
    exit()

# 逐幀擷取並儲存
frame_count = 0
while True:
    ret, frame = video_capture.read()
    if not ret:
        print(f"[錯誤] 在 frame {frame_count} 讀取失敗，可能是影片結束或解碼問題。")
        break  # 影片讀取結束
    frame_filename = os.path.join(frames_dir, f"frame_{frame_count:04d}.png")
    if cv2.imwrite(frame_filename, frame):
        print(f"[成功] 已擷取並儲存: {frame_filename}")
    else:
        print(f"[錯誤] 無法儲存 {frame_filename}，請檢查寫入權限。")
    frame_count += 1

video_capture.release()

# 檢查是否成功擷取幀數
frames = sorted([f for f in os.listdir(frames_dir) if f.endswith('.png')])
if not frames:
    print("[錯誤] 影片幀擷取失敗，請檢查影片格式或權限。")
    print("建議: 1. 嘗試將影片轉換為 MP4 (H.264) 格式。")
    print("       2. 以管理員身份執行程式，確保有權限讀取影片。")
    exit()
else:
    print(f"[成功] 已擷取 {len(frames)} 幀，儲存於 {frames_dir}")