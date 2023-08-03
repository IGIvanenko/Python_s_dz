import os

main_path = 'd:\\down'

extensions = {

    'video': ['mp4', 'mov', 'avi'],

    'data': ['sql', 'sqlite', 'csv', 'xml'],

    'audio': ['mp3', 'wav', 'flac', 'wma'],

    'image': ['jpg', 'png', 'tiff'],

    'archive': ['zip', 'rar', 'z', 'pkg'],

    'text': ['pdf', 'txt', 'doc', 'docx', 'tex'],

    '3d': ['stl', 'obj', 'fbx'],

    'presentation': ['pptx', 'ppt', 'pps', 'key'],

    'spreadsheet': ['xlsx', 'xls'],

    'font': ['otf', 'ttf', 'fon'],

    'gif': ['gif'],

    'exe': ['exe'],

    'bat': ['bat'],

    'apk': ['apk']
}


# also creates folders from dictionary keys
def create_folders_from_list(folder_path, folder_names):
    for folder in folder_names:
        if not os.path.exists(f'{folder_path}\\{folder}'):
            os.mkdir(f'{folder_path}\\{folder}')


def get_subfolder_paths(folder_path) -> list:
    subfolder_paths = [f.path for f in os.scandir(folder_path) if f.is_dir()]

    return subfolder_paths


def get_file_paths(folder_path) -> list:
    file_paths = [f.path for f in os.scandir(folder_path) if not f.is_dir()]

    return file_paths


def sort_files(folder_path):
    file_paths = get_file_paths(folder_path)
    ext_list = list(extensions.items())

    for file_path in file_paths:
        extension = file_path.split('.')[-1]
        file_name = file_path.split('\\')[-1]

        for dict_key_int in range(len(ext_list)):
            if extension in ext_list[dict_key_int][1]:
                print(f'Moving {file_name} in {ext_list[dict_key_int][0]} folder\n')
                os.rename(file_path, f'{main_path}\\{ext_list[dict_key_int][0]}\\{file_name}')


def remove_empty_folders(folder_path):
    subfolder_paths = get_subfolder_paths(folder_path)

    for p in subfolder_paths:
        if not os.listdir(p):
            print('Deleting empty folder:', p.split('\\')[-1], '\n')
            os.rmdir(p)


if __name__ == "__main__":
    create_folders_from_list(main_path, extensions)
    sort_files(main_path)
    remove_empty_folders(main_path)