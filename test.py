import os
import csv

# 设置输入文件夹路径
input_folder = './input_folder'  # 输入文件夹路径，包含 .jpg 文件
output_csv = './filelist.csv'  # 输出的 CSV 文件路径

# 获取输入文件夹中的所有 .jpg 文件
jpg_files = [f for f in os.listdir(input_folder) if f.endswith('.jpg')]

# 为每个文件指定元数据（这里以假设为例，可以根据实际情况修改）
slide_mpp = 0.25  # 假设所有图像的缩放因子为 0.25，可以根据需要修改
magnification = 40  # 假设所有图像的放大倍数为 40，可以根据需要修改

# 创建 CSV 文件并写入数据
with open(output_csv, mode='w', newline='') as csvfile:
    fieldnames = ['wsi_path', 'slide_mpp', 'magnification']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # 写入表头
    writer.writeheader()

    # 遍历所有图像文件，记录路径和元数据
    for jpg in jpg_files:
        wsi_path = os.path.join(input_folder, jpg)  # 图像文件的路径

        # 写入每个图像的元数据
        writer.writerow({
            'wsi_path': wsi_path,
            'slide_mpp': slide_mpp,
            'magnification': magnification
        })

print(f"CSV 文件已生成：{output_csv}")
