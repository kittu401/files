import shutil, time, os
s_path = "C:\\Users\\kishore\\Downloads"
sql_dir = "C:\\Users\\kishore\\Desktop\\"

folder_names = ["sql_files", "informatica"]

while True:
    time.sleep(5)

    x = os.listdir(s_path)
    for i in x:

        if "sql" in i.lower():
            print("SQL present so moving file")
            os.chdir(sql_dir)
            if os.path.isdir(folder_names[0]):
                shutil.move(s_path + "\\" + i, sql_dir + "\\" + folder_names[0] + "\\" + i)
            else:
                os.chdir(sql_dir)
                os.mkdir(folder_names[0])

                shutil.move(s_path + "\\" + i, sql_dir + "\\" + folder_names[0] + "\\" + i)
        else:
            pass

        if "informatica" in i.lower():
            print("informatica present so moving file")
            if os.path.isdir(folder_names[1]):
                shutil.move(s_path + "\\" + i, sql_dir + "\\" + folder_names[1] + "\\" + i)
            else:
                os.mkdir(folder_names[1])
                shutil.move(s_path + "\\" + i, sql_dir + "\\" + folder_names[1] + "\\" + i)
        else:
            pass
