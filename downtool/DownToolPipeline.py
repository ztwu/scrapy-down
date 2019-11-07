import os
import urllib

class DownToolPipeline(object):
    def process_item(self, item, spider):
        dir_path = 'D:/python/scrapy-down/save'

        # print'dir_path',dir_path

        if item['img'] is not None:

            for image_url in item['img']:

                list_name = image_url.split('/')

                file_name = list_name[len(list_name) - 1]  # 图片名称

                file_path = '%s/%s' % (dir_path, file_name)

                if os.path.exists(file_name):
                    continue

                with  open(file_path, 'wb') as file_writer:

                    conn = urllib.request.urlopen(image_url)  # 下载图片

                    file_writer.write(conn.read())

                    file_writer.close()

        if item['gif'] is not None:

            for image_url in item['gif']:

                list_name = image_url.split('/')

                file_name = list_name[len(list_name) - 1]  # 图片名称

                file_path = '%s/%s' % (dir_path, file_name)

                if os.path.exists(file_name):
                    continue

                with  open(file_path, 'wb') as file_writer:

                    conn = urllib.request.urlopen(image_url)  # 下载图片

                    file_writer.write(conn.read())

                    file_writer.close()

        return item
