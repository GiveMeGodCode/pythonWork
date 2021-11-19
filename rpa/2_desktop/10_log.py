# import logging

# logging.basicConfig(level=logging.ERROR,
#                     format="%(asctime)s [%(levelname)s] %(message)s")
# # debug < info < warning < error < critical
# logging.debug("아 이거 누가 만든거지?")
# logging.info("자동화 수행 준비")
# logging.warning("이 스크립트는 오래되어 오작동할수있음.")
# logging.error("에러가 발생하였음")
# logging.critical("복구불가오류")

# 터미널과 파일에 로그 만들기

import logging
from datetime import datetime
logFormatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger()

# 로그 레벨 설정
logger.setLevel(logging.DEBUG)

# 스트림
streamHandler = logging.StreamHandler()
streamHandler.setFormatter(logFormatter)
logger.addHandler(streamHandler)

# 파일
filename = datetime.now().strftime("mylogFile_%Y%m%d%H%M%S.log")
fileHandler = logging.FileHandler(filename, encoding="utf-8")
fileHandler.setFormatter(logFormatter)
logger.addHandler(fileHandler)


logging.debug("아 이거 누가 만든거지?")
logging.info("자동화 수행 준비")
logging.warning("이 스크립트는 오래되어 오작동할수있음.")
logging.error("에러가 발생하였음")
logging.critical("복구불가오류")
