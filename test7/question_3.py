import csv


def read_name_email(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8', newline='') as f:
            # 使用 DictReader 读取为字典格式
            csv_reader = csv.DictReader(f)
            ls = list(csv_reader)

            for row in ls:
                print(f"名字: {row['name']}, 邮件地址: {row['email']}")
    except Exception as err:
        print(f'1错误信息: {err}')


def write_to_usercopy(raw_path, new_path):
    try:
        with open(raw_path, 'r', encoding='utf-8', newline='') as f:
            csv_read = csv.DictReader(f)
            fieldnames = csv_read.fieldnames  # 获取原文件的字段名
            with open(new_path, 'w', encoding='utf-8', newline='') as f_copy:
                csv_write = csv.DictWriter(f_copy, fieldnames=fieldnames)
                csv_write.writeheader()  # 写入表头
                csv_write.writerows(csv_read)  # 写入数据
    except Exception as err:
        print(f"2出错信息: {err}")





if __name__ == "__main__":
    raw_file_csv = "user.csv"
    read_name_email(raw_file_csv)
    new_file_csv = "usercopy.csv"
    write_to_usercopy(raw_file_csv, new_file_csv)
