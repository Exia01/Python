import random
import os


def get_filename_ext(filepath):
    # print('from get filename, filepath: ', filepath)
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    # print('from get filename: name, ext ', name, ext, '\n')
    return name, ext   


# def upload_image_path(instance, filename):
#     new_filename = random.randint(1, 8989898989898)
#     print(instance)
#     print(filename)
#     name, ext = get_filename_ext()
#     # file will be uploaded to MEDIA_ROOT/product_<id>/<filename>
#     return 'product{0}/{1}'.format(instance.product.id, filename)
