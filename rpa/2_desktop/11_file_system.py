# 파일 기본
import datetime
import time
import os
# print(os.getcwd())  # 작업디렉토리
# os.chdir("rpa")
# print(os.getcwd())  # 작업디렉토리
# os.chdir("../..")
# print(os.getcwd())  # 작업디렉토리
# os.chdir("c:/")
# print(os.getcwd())  # 작업디렉토리


# 파일경로 만들기
# print(os.path.join(os.getcwd(), "my_file.txt"))

# file_path = os.path.join(os.getcwd(), "my_file.txt")
# print(file_path)


# 파일경로에서 폴더 정보 가져오기.
# print(os.path.dirname(r"C:\workSpace\PYTHON_WORKSPACE\my_file.txt"))

# 파일 정보 가져오기.

# 파일의 생성날짜

# file_path = "rpa/2_desktop/11_file_system.py"
# ctime = os.path.getctime(file_path)

# print(datetime.datetime.fromtimestamp(ctime).strftime("%Y-%m-%d %H:%M:%S"))


# mtime = os.path.getmtime(file_path)

# print(datetime.datetime.fromtimestamp(mtime).strftime("%Y-%m-%d %H:%M:%S"))

# atime = os.path.getatime(file_path)

# print(datetime.datetime.fromtimestamp(atime).strftime("%Y-%m-%d %H:%M:%S"))

# # 파일크기
# size = os.path.getsize(file_path)
# print(size)


# print(os.listdir())  # 모든 폴더, 파일목록 가져오기.
# print(os.listdir("rpa"))

# 파일목록 하위폴더 모두 포함
# result = os.walk(".")
# for root, dirs, files in result:
#     print(root, dirs, files)


# 만약 폴더 내에서 특정 파일들을 찾으려면?
# name = "11_file_system.py"
# result = []
# for root, dirs, files in os.walk("."):
#     if name in files:
#         result.append(os.path.join(root, name))

# print(result)


# 확장자 찾기
# *.xlsx, *.txt,
# import fnmatch
# name = "11_file_system.py"
# pattern = "file*.png"  # .py 로 끝나는 모든파일 읽기
# result = []
# for root, dirs, files in os.walk("."):
#     for name in files:
#         if fnmatch.fnmatch(name, pattern):
#             result.append(os.path.join(root, name))

# print(result)

# 주어진 경로가 파일인지 ? 폴더인지?
# print(os.path.isdir("rpa"))
# print(os.path.isfile("rpa"))


# print(os.path.isdir("run_btn.png"))
# print(os.path.isfile("run_btn.png"))


# 만약 지정된 경로에 파일, 폴더가 없다면?
# print(os.path.isdir("drun_btn.png"))
# print(os.path.isfile("drun_btn.png"))

# 주어진 경로가 존재하는가?
# if os.path.exists("f"):
#     print("파일 또는 폴더가 있어여")
# else:
#     print("파일 또는 폴더 없어요.")


# 파일 만들기
# open("new_file.txt", "a").close()

# 파일명 변경하기
# os.rename("new_file.txt", "new_file_rename.txt")

# 파일삭제
# os.remove("new_file_rename.txt")

# 폴더생성
# os.mkdir("new_folder")
# os.mkdir("c:/")
# 현재폴더, 절대경로 지정해서 만들수있다.


# os.mkdir("new_folders/a/b/c")
# os.makedirs("new_folders/a/b/c")  # 하위폴더까지 만들기.
# os.rename("new_file.txt", "new_file_rename.txt")
# os.rmdir("new_folders")  # 폴더안이 비어있을떄만


import shutil
# shutil.rmtree("new_folders")
# 모든파일이 지워질수있으므로 조심해야한다.
# shutil.copy("run_btn.png", "test_folder/copied_run_btn.png")  # 원본vs대상경로
# shutil.copyfile("run_btn.png", "test_folder/copied_run_btn.png")  # 원본vs대상경로

# 원본파일 경로, 대상 폴더(파일 경로)
# shutil.copy("run_btn.png", "test_folder/copied1.png")
# shutil.copy2("run_btn.png", "test_folder/copied2.png")
# copy, copyfile (메타복사X)
# copy2 : 메타정보 복사 O


# shutil.copytree("test_folder", "test_folder2")  # 트리복사
# shutil.copytree("test_folder", "test_folder3")  # 트리복사

# shutil.move("test_folder", "test_folder3")  # 폴더이동
# shutil.move("test_folder2", "test_folder3")  # 폴더이동
#   shutil.move("test_folder3", "test_folder")  # 폴더이동 rename 효과를 얻을수도 있따.
