from PIL import Image
import os

# โฟลเดอร์ที่เก็บภาพ
folder_path = 'C:/Users/araya/Desktop/zung/2.mp4/video1'  # เปลี่ยนเป็น path ที่เก็บภาพจริง
folder_path = 'C:/Users/araya/Desktop/zung1/กรรมการ.mp4/video2'  # เปลี่ยนเป็น path ที่เก็บภาพจริง

# อ่านไฟล์ภาพ .jpg ทั้งหมด และเรียงตามเลข frame
image_files = sorted(
    [f for f in os.listdir(folder_path) if f.endswith('.jpg')],
    key=lambda x: int(x.split('_')[-1].split('.')[0])
)

# เปิดภาพทั้งหมด
images = [Image.open(os.path.join(folder_path, f)) for f in image_files]

# สร้าง gif
images[0].save('output4.gif',
               save_all=True,
               append_images=images[1:],
               duration=100,  # ms ต่อเฟรม
               loop=0)        # 0 = วนลูปตลอด