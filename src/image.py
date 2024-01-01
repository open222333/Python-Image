from PIL import Image
from src.logger import Log
import logging
import os


class ImagePath():

    is_remove_source = False

    def __init__(self, source_path: str, output_path: str = None, logger: logging = None, **kwargs) -> None:
        self.source_path = source_path
        directory, filename = os.path.split(source_path)
        self.filename, self.extension = os.path.splitext(filename)

        if output_path == None:
            self.output_path = directory
        else:
            self.output_path = output_path

        if logger == None:
            self.logger = Log('Image')
            self.logger.set_level(kwargs.get('log_level', 'WARNING').upper())

    def enable_remove_source(self):
        """開啟 刪除原檔案功能
        """
        self.logger.info('開啟 刪除原檔案功能')
        self.is_remove_source = True

    def remove_source(self):
        """刪除原檔案

        Args:
            func (_type_): _description_
        """
        try:
            if self.is_remove_source:
                self.logger.debug(f'刪除 {self.source_path}')
                os.remove(self.source_path)
        except Exception as err:
            self.logger.error(f'刪除 {self.source_path} 發生錯誤: {err}', exc_info=True)


class ImageWebp(ImagePath):

    def __is_webp(self):
        return (self.extension == '.webp')

    def convert_webp_to_jpg(self):
        """轉換 webp 成 jpg
        """
        try:
            if self.__is_webp():
                with Image.open(self.source_path) as img:
                    img.convert("RGB").save(f'{self.output_path}/{self.filename}.jpg', "JPEG")
                self.logger.debug(f"Conversion successful. JPEG image saved at {self.output_path}/{self.filename}")
                self.remove_source()
        except Exception as e:
            self.logger.error(f"轉換 webp 成 jpg 發生錯誤: {e}")
