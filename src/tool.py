import shutil
import os


def get_all_files(dir_path: str, extensions=None):
    """取得所有檔案

    Args:
        dir_path (_type_): 檔案資料夾
        extensions (_type_, optional): 指定副檔名,若無指定則全部列出. Defaults to None.

    Returns:
        _type_: _description_
    """
    target_file_path = []
    path = os.path.abspath(dir_path)

    for file in os.listdir(path):
        _, file_extension = os.path.splitext(file)
        if extensions:
            allow_extension = [f'.{e}' for e in extensions]
            if file_extension in allow_extension:
                target_file_path.append(f'{dir_path}/{file}')
        else:
            target_file_path.append(f'{dir_path}/{file}')

        # 遞迴
        if os.path.isdir(f'{dir_path}/{file}'):
            files = get_all_files(f'{dir_path}/{file}', extensions)
            for file in files:
                target_file_path.append(file)
    target_file_path.sort()
    return target_file_path


def move_files_and_remove_subdirectories(source_path: str):
    """移動子資料夾檔案至資料夾並刪除子資料夾

    Args:
        source_path (str): 資料夾路徑
    """
    for subfolder_name in os.listdir(source_path):
        subfolder_path = os.path.join(source_path, subfolder_name)

        if os.path.isdir(subfolder_path):
            for file_name in os.listdir(subfolder_path):
                # print(f'source_path:{source_path}')
                destination_path = os.path.join(subfolder_path, file_name)
                # print(f'destination_path:{destination_path}')
                shutil.copy2(destination_path, source_path)
            shutil.rmtree(subfolder_path)
