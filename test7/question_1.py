def merged_files(file1_path, file2_path, merged_file_path):
    try:
        with open(file1_path, 'r', encoding='utf-8') as f1:
            content1 = f1.read()

        with open(file2_path, 'r', encoding='utf-8') as f2:
            content2 = f2.read()

        merged_content = content1 + '\n' + content2
        with open(merged_file_path, 'w', encoding='utf-8') as f3:
            f3.write(merged_content)

        print("追加成功！")

    except Exception as err:
        print(f'错误信息：{err}')



if __name__ == "__main__":
    file1 = "file1.txt"
    file2 = "file2.txt"
    merged_file = "merged_file.txt"
    merged_files(file1, file2, merged_file)
