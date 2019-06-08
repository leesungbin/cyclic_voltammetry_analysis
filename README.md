## 초기 Setting 방법

(1) python 3.7 버전을 설치합니다.(2019.06.08 기준 latest 버전 : 3.7.3)

https://www.python.org/downloads/ 

(2) 설치 파일을 실행시, 맨 처음 화면 하단에 있는, **"Add Python 3.7 to PATH"** 를 체크해주고, **"Install Now"** 로 설치합니다.

(3) `pip install -r requirements.txt` 명령어로 의존 라이브러리들을 설치합니다.



## 실행 Manual

(1) 파일 명 앞에 `py`를 붙인 `.xlsx` 확장자를 가진 파일 대상으로 분석을 실시합니다.

(2) 파일들은 `CV_analysis.py` 와 같은 폴더 내에 있어야 합니다.

(3) `py`를 붙였던 파일들은 분석 후, 다시 원래 이름으로 돌아갑니다.

(4) CV_analysis.py 파일의 연결프로그램을 python으로 설정해줍니다.

(6) 각 상황별 마지막 cycle에 대한 CV 그래프를 한번에 출력해준 후 종료됩니다.

(7) 그래프에 붙는 라벨은 파일명의 첫 괄호 '( )' 안에 들어가는 이름으로 설정됩니다.

(8) https://github.com/leesungbin/cyclic_voltammetry_analysis.git 에서 현재 파일을 확인할 수 있습니다.