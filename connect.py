# yes

file_list = os.listdir(FILE_DIRNAME)
string = '\n'.join(file_list)
string2 = '\n'.join(os.listdir(os.path.dirname(FILE_DIRNAME)))
with open(os.path.join(FILE_DIRNAME, 'new.txt'), 'w', encoding='utf-8') as f:
    f.write(f'这是实时可以控制的哈哈哈哈。让我猜猜，该文件夹内应该有这些文件：\n{string}')
    f.write(f'父级文件夹啊，emm，{string2})
