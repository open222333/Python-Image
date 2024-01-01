from argparse import ArgumentParser
from src.image import ImageWebp
from src.tool import get_all_files
from src import DIR_PATH
import os

parser = ArgumentParser()
parser.add_argument('-d', '--dir_path', type=str, help='來源資料夾位置', default=DIR_PATH)
parser.add_argument('--remove_source', action='store_true', help='開啟 轉檔後刪除原檔 功能')
args = parser.parse_args()

if __name__ == '__main__':
    if os.path.exists(args.dir_path):
        files = get_all_files(args.dir_path)
        for file in files:
            # print(file)
            iw = ImageWebp(source_path=file)
            if args.remove_source:
                iw.enable_remove_source()
            iw.convert_webp_to_jpg()
