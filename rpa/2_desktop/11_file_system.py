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

file_path = os.path.join(os.getcwd(), "my_file.txt")
print(file_path)


# 파일경로에서 폴더 정보 가져오기.
print(os.path.dirname(r"C:\workSpace\PYTHON_WORKSPACE\my_file.txt"))

# 파일 정보 가져오기.

# 파일의 생성날짜
ctime = os.path.getctime("run_btn.png")

print(datetime.datetime.fromtimestamp(ctime).strftime("%Y-%m-%d %H:%M:%S"))
