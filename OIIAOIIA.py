import pygame
import os
import re

# 設定影片路徑與幀數儲存路徑
video_path = r"C:\Users\User\Desktop\程式\python\OIIAOIIA cat\videoplayback.mp4"
frames_dir = r"C:\Users\User\Desktop\OIIAOIIA frames"
sound_path = r"C:\Users\User\Desktop\OIIAOIIA frames\soundpack.mp3"


# 確保幀數資料夾存在
if not os.path.exists(frames_dir):
    os.makedirs(frames_dir)

# 指定動畫範圍
animation_frames = list(range(43, 95)) + list(range(128, 189)) + list(range(230, 349))

# 初始化 Pygame
pygame.init()
pygame.mixer.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("OIIAOIIA CAT Game")

# 設定字型與顏色
font = pygame.font.SysFont("Microsoft JhengHei", 24)  # 使用微軟正黑體
text_color = (255, 255, 255)  # 白色文字
box_color = (50, 50, 50)  # 灰色背景框
border_color = (200, 200, 200)  # 白色邊框

# 載入音效
move_sound = None
if os.path.exists(sound_path):
    try:
        move_sound = pygame.mixer.Sound(sound_path)
    except pygame.error as e:
        print(f"[警告] 音效載入失敗: {e}")
else:
    print("[警告] 找不到音效檔案，將不播放音效。")

# 載入圖片
all_frames = sorted([f for f in os.listdir(frames_dir) if f.endswith('.png')])

# 使用正規表達式提取數字
def extract_frame_number(filename):
    match = re.search(r"frame_(\d+)\.png", filename)
    return int(match.group(1)) if match else None

selected_frames = [f for f in all_frames if extract_frame_number(f) in animation_frames]
image_frames = [pygame.image.load(os.path.join(frames_dir, f)) for f in selected_frames]

# 確保影格數量不為空
if not image_frames:
    print("[錯誤] 沒有成功載入動畫影格，請檢查 frames 目錄。")
    exit()

# 設定靜態圖片
static_image = pygame.image.load(os.path.join(frames_dir, "frame_0000.png")) if "frame_0000.png" in all_frames else image_frames[0]

# 遊戲狀態變數
running = True
clock = pygame.time.Clock()
current_frame = 0
playing_animation = False

# 遊戲主循環
while running:
    screen.fill((0, 0, 0))  # 清空畫面

    # 繪製操作說明
    instructions = [
        "按住 ← 或 → 鍵 : Play OIIAOIIA",
        
        "放開按鍵 : Reset OIIAOIIA",
    ]
    
    box_width, box_height = 350, len(instructions) * 35 + 20
    pygame.draw.rect(screen, box_color, (5, 5, box_width, box_height))  # 背景框
    pygame.draw.rect(screen, border_color, (7, 5, box_width, box_height), 2)  # 邊框
    
    for i, line in enumerate(instructions):
        text_surface = font.render(line, True, text_color)
        screen.blit(text_surface, (15, 15 + i * 35))  # 調整間距並置入邊框內

    # 事件處理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                playing_animation = True
                current_frame = 0
                if move_sound:
                    try:
                        move_sound.play(-1)  # 循環播放
                    except pygame.error as e:
                        print(f"[警告] 音效播放失敗: {e}")
        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                playing_animation = False
                if move_sound:
                    move_sound.stop()  # 停止音效

    # 確保影格數量 > 0，否則不更新動畫
    if playing_animation and image_frames:
        frame_image = image_frames[current_frame % len(image_frames)]
        current_frame += 1
    else:
        frame_image = static_image

    rect = frame_image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(frame_image, rect.topleft)

    pygame.display.flip()
    clock.tick(30)  # 控制 FPS，避免 CPU 過載

pygame.quit()
