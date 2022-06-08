import os
import zipfile

# указать полный путь к папке `detalization`, куда предварительно помещены архивы с детализацией
path = '\\WB\\detalization'
os.chdir(path)

list_zip_files = os.listdir()

for f in list_zip_files:
    if zipfile.is_zipfile(f) is True:
        z = zipfile.ZipFile(f, 'r')
        filename = z.namelist()[0]
        # указать полный путь
        z.extract(filename, path='\\WB\\detalization\\unzip')
        z.close()
        # указать полный путь
        path = '\\WB\\detalization\\unzip'
        os.chdir(path)
        os.rename(filename, f[:-4]+'.xlsx')
        # указать полный путь
        path = '\\WB\\detalization'
        os.chdir(path)
