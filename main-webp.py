from argparse import ArgumentParser
from src.image import ImageWebp
from src.progress_bar import ProgressBar
from src.tool import get_all_files, move_files_and_remove_subdirectories
from src import DIR_PATH
import os

parser = ArgumentParser()
parser.add_argument('-d', '--dir_path', type=str, help='來源資料夾位置', default=DIR_PATH)
parser.add_argument('-r', '--remove_source', action='store_true', help='開啟 轉檔後刪除原檔 功能')
parser.add_argument('-R', '--remove_subdirectories', action='store_true', help='開啟 移動子資料夾檔案至資料夾並刪除子資料夾 功能')
args = parser.parse_args()

if __name__ == '__main__':
    if os.path.exists(args.dir_path):

        files = get_all_files(args.dir_path)
        p = ProgressBar()
        for file in files:
            if args.remove_subdirectories:
                if os.path.isdir(file):
                    move_files_and_remove_subdirectories(file)
            p(total=len(files), in_loop=True)
            iw = ImageWebp(source_path=file)

            if args.remove_source:
                iw.enable_remove_source()
            iw.convert_webp_to_jpg()
