# Python 코드를 통해 가상의 브라우저를 띄우기 위해 selenium 패키지를 import 합니다.
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# selenium을 활용해 브라우저를 직접 띄우는 경우, 실제 웹서핑을 할때처럼 로딩시간이 필요합니다.
# 로딩시간 동안 대기하도록 코드를 구성하기위해 time 패키지를 import 합니다.
import time

def start():
    # Python 코드를 통해 웹페이지에 정보를 요청하기 위해 BeautifulSoup, urllib 패키지를 import 합니다.
    # from bs4 import BeautifulSoup
    # import requests

    # Chrome Driver를 호출합니다.
    chrome_options = webdriver.ChromeOptions()

    # 브라우저에 임의로 User-agent 옵션을 넣어 Python 코드로 접속함을 숨깁니다.
    chrome_options.add_argument(
        '--user-agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"')

    # Chrome Driver 파일의 경로를 지정하고 실행합니다.
    # Chrome Driver는 아래 링크에서 다운로드 가능합니다.
    # 본 Jupyter Notebook 파일과 동일한 경로에 Chrome Driver가 존재하는 경우 아래 경로를 그대로 사용합니다.

    service = Service("./chromedriver.exe")  # Windows 운영체제
    # service = Service("./chromedriver")    # MAC, Linux 운영체제
    # 경고메시지 출력시 조치 : [시스템 환경설정] > [보안 및 개인정보 보호] > "Chrome Drive ~ 확인없이 허용"

    driver = webdriver.Chrome(service=service, options=chrome_options)

    # 네이버 메인페이지로 이동합니다.
    URL = "https://naver.com"
    driver.get(URL)
    time.sleep(2)

    # 네이버 카페에 접근하기 위해서는 로그인이 필요합니다.
    # 네이버 로그인 페이지로 이동합니다.
    # click() 함수로 원하는 요소(태그)를 클릭할 수 있습니다.
    # request > .find, .findAll
    # soup.find / findALL()
    driver.find_element(By.CLASS_NAME, "link_login").click()
    # 네이버 로그인 페이지에서 아이디(ID)와 비밀번호(PW)를 입력합니다.
    # 아이디와 비밀번호를 브라우저에서 직접 입력해도 됩니다.

    time.sleep(30)

    # 수집할 카페 게시물의 링크주소를 저장할 리스트를 생성합니다.
    post_list = []

    # 브라우저에서 직접 내가 수집할 카페에 접속합니다.
    # 카페 검색기능을 활용해 수집하고 싶은 내용을 검색합니다.
    # 키워드, 기간, 정렬기준 등을 지정해 원하는 검색결과를 화면에 띄웁니다.
    # 검색 후 게시물 리스트가 포함된 "진짜 URL"을 찾아냅니다.
    # URL을 복사할 때 맨뒤에 "...%26search.page=3" 부분의 숫자(페이지번호)는 제거하고 입력합니다.
    # 예시는 네이버 카페 "디젤매니아"에서 "청바지"라는 키워드로 검색된 게시물 URL 입니다.
    # 게시물 열람이 가능한 계정으로 카페에 접근해야 수집이 가능합니다.
    URL = "https://cafe.naver.com/ArticleSearchList.nhn?search.clubid=23611966&search.searchdate=all&search.searchBy=1&search.defaultValue=1&search.sortBy=date&userDisplay=15&search.media=0&search.option=0&search.menuid=464&search.page="

    # 몇 페이지 까지 게시물의 URL을 수집할지 지정합니다.
    # 최대 페이지 수를 넘지 않도록 주의합니다.
    page_limit = 100

    # FOR 문을 활용해 페이지 번호를 반복합니다.
    for page_num in range(1, page_limit + 1):
        # 검색결과 페이지로 이동합니다.
        driver.get(URL + str(page_num))
        # 페이지에서 게시물 리스트가 포함된 프레임으로 이동합니다.
        # 21.10.16 수정
        # driver.switch_to_frame(driver.find_element(By.NAME, "cafe_main"))
        driver.switch_to.frame(driver.find_element(By.NAME, "cafe_main"))

        # 게시물 태그를 모두 불러옵니다.
        elem = driver.find_elements(By.CLASS_NAME, "article")
        for e in elem:
            # 웹페이지의 하이퍼링크 URL은 항상 href 속성에 존재합니다.
            # href 속성에 저장된 URL을 불러와 post_list에 추가합니다.
            post_list.append(e.get_attribute("href"))
        # 아래 주석부분은 위 25~29번째 라인과 동일한 코드입니다.
        # 혹시 post_list에 URL이 저장되지 않는 경우 아래처럼 태그의 Class 속성을 "article"에서 "aaa"로 변경해줍니다.
        '''
        elem = driver.find_elements(By.CLASS_NAME, "aaa")
        for e in elem:
            post_list.append(e.find_element(By.TAG_NAME, "a").get_attribute("href"))
        '''
        # 페이지의 기본 프레임으로 이동합니다.
        driver.switch_to.default_content()
        time.sleep(2)

    # 총 몇개의 게시물 URL이 저장되었는지 확인합니다.
    print("수집된 게시물 URL 개수 :", len(post_list))

    from timeit import default_timer as timer

    s = timer()


    # 게시물 URL이 저장된 post_list에서 몇번째 부터(start) 몇번째 까지(end) URL에 접근할지 지정합니다.
    start = 0
    end = len(post_list)

    # 게시물 내용을 저장할 파일을 생성합니다.
    f = open("result.txt", "w", encoding="utf-8")

    # FOR 문을 활용해 페이지 URL을 반복합니다.
    for url in post_list[start:end]:
        # 현재 수집이 진행중인 인덱스를 출력합니다.
        print(str(start+1) + "/" + str(end), end="\r")
        start += 1
        try:
            # URL을 통해 게시물 페이지로 이동합니다.
            driver.get(url)
            time.sleep(3)
            # 페이지에서 게시물 내용이 포함된 프레임으로 이동합니다.
            driver.switch_to.frame(driver.find_element(By.NAME, "cafe_main"))

            # 페이지에서 태그의 속성을 활용해 원하는 부분을 불러옵니다.
            # 1. 게시물 제목
            title = driver.find_element(By.CLASS_NAME, "title_text").text.strip()
            contents = driver.find_element(By.CLASS_NAME, "article_viewer").text.replace("\n", " ")
            # 파일에 수집한 게시물 내용을 기록합니다.
            f.write("POSTING" + "\t" + title + "\t" + contents + "\n")

            # 댓글을 모두 불러옵니다.
            reply_list = driver.find_elements(By.CLASS_NAME, "comment_box")
            # FOR 문을 활용해 댓글을 모두 반복합니다.
            for reply in reply_list:
                # 6. 댓글 내용
                comment = reply.find_element(By.CLASS_NAME, "text_comment").text.replace("\n", " ")
                # 파일에 수집한 댓글 내용을 기록합니다.
                f.write("COMMENT" + "\t" + comment + "\n")
            # 페이지의 기본 프레임으로 이동합니다.
            driver.switch_to.default_content()
            time.sleep(2)
        except:
            driver.switch_to.default_content()
            time.sleep(2)
            continue
    f.close()

    e = timer()
    print(e - s) #

    # 파일에 저장된 카페 게시글 내용을 확인합니다.
    f = open("result.txt", encoding="utf-8")
    cnt = 0
    for post in f:
        print(post.strip())
        cnt += 1
    f.close()

    print(cnt)

    # Chrome Driver를 닫습니다.
    driver.close()

