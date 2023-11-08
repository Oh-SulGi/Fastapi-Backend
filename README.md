# FastAPI를 이용한 웹개발 프로젝트

- Python의 FastAPI를 이용해 Rest API와 데이터베이스를 구축해보고 <br>
이를 통해 백엔드 인사이트를 얻기 위해 기획되었습니다. 

<br>

# 전체 프로젝트 구조

<img src='./img/flow.jpg' >
<img src='./img/aa.png'>

<br>

## REST API 구조

<img src='./img/Untitled.png'>

<br>

<b>domain<b>
<details>
  <summary><b>create_data : 사용자 행동의 기반이 되는 주식 데이터 ETL</b></summary>

  <img src='./img/1.png'>

  - data : MySQL에 적재하기 전 Raw Data
  - create_schema.py : MySQL에 생성할 테이블 스키마 정보
  - insert_data.py : 정제된 데이터를 스키마에 맞춰 적재
  - stock_daily_price.py : 수집하고자 하는 기업의 종목코드를 리스트로 만들고 시작일과 종료일을 입력하여 해당 기간 동안의 일봉 데이터 수집
  - stock_price_now.py : 수집하고자 하는 기업의 종목 코드를 리스트로 만들고, 수집 시점의 현재가를 시간데이터와 함께 수집
  - top50_information.py : 한국투자증권 API와 DART openAPI를 이용, 코스피와 코스닥 시가총액 상위 25개씩 총 50개 기업의 재무정보 수집

</details>

<details>
  <summary><b>quiz : 경제 퀴즈 관련 CRUD</b></summary>
  
  <img src='./img/2.png'>

  - quiz_crud.py : 입력한 숫자에 해당하는 난이도의 문제를 무작위로 1개 출력
  - quiz_router.py : 무작위로 출력된 문제를 풀었을 때, 로그인한 유저의 cash가 증가하고 틀렸을 때에는 문제의 힌트가 출력

</details>

<details>
  <summary><b>trade : 주식 거래 관련 CRUD</b></summary>
  
  <img src='./img/3.png'>

  - trade_crud.py
    - buy_stock : 기업코드와 수량을 입력했을 때 유저의 cash 잔액이 충분하다면 금액과 수량을 각각 wallet과 portfolio 테이블에 반영
    - sell_stock : 기업코드와 수량을 입력했을 때 유저의 portfolio에 있는 주식 수량이 충분하다면 금액과 수량을 각각 wallet과 portfolio 테이블에 반영
    - eval_stock : 함수를 실행한 당시의 현재가를 기준으로 유저의 portfolio 테이블에 있는 모든 주식의 가치를 계산하여 wallet 테이블에 반영
  - trade_router.py : 주식을 거래할 때마다 총 주식 평가액을 재계산하여 반영

</details>

<details>
  <summary><b>user : 유저 정보 관련 CRUD</b></summary>
  
  <img src='./img/4.png'>

  - user_crud.py : 유저가 입력한 정보로 회원가입 및 관련 db 생성
  - user_router.py : 로그인, 로그아웃, 현재 유저 정보 출력
  - user_schema.py : validator를 이용해 유효성 검사 진행

</details>

wallet : 유저의 자산 정보 업데이트 <br>
<br>
scheduler : 주식의 장중 가격을 주기적으로 업데이트 <br>
database.py <br>
main.py <br>
models.py

## API 문서 / DB

<details>
  <summary><b>/user/create</b></summary>
  
  <img src='./img/api1.png'>
  <br>

  - ID, 비밀번호, 이름, 이메일을 입력 받아 유효성 검사를 진행

  <img src='./img/api2.png'>
  <img src='./img/api3.png'>
  <img src='./img/api4.png'>
  <br>

  - 가입이 완료되면 DB에 유저정보/자산/포트폴리오 테이블이 생성,
  비밀번호는 암호화되어 유저정보에 저장되고 쿠키에 접속 정보 저장

</details>

<details>
  <summary><b>/user/login</b></summary>
  
  <img src='./img/api5.png'>
  <br>

  - ID와 비밀번호를 입력하면 DB와 대조하여 로그인 진행 로그인에 성공하면 jwt 토큰값 반환

</details>

<details>
  <summary><b>/user/current_user</b></summary>
  
  <img src='./img/api6.png'>
  <br>

  - 쿠키에 저장된 유저정보와 토큰값을 반환

</details>

<details>
  <summary><b>/quiz/random</b></summary>
  
  <img src='./img/api7.png'>
  <img src='./img/api8.png'>
  <img src='./img/api9.png'>
  <img src='./img/api10.png'>
  <br>

  - 선택한 난이도에 해당하는 숫자와 답을 입력하면 정답일 경우 로그인한 유저의 자산에 cash 추가, 오답일 경우 문제의 힌트 출력

</details>

<details>
  <summary><b>/trade/trade</b></summary>
  
  <img src='./img/api11.png'>
  <img src='./img/api12.png'>
  <img src='./img/api13.png'>
  <img src='./img/api14.png'>
  <br>

  - 거래하고자 하는 주식의 코드 / 수량 / buy, sell을 입력했을때 자산에 cash가 충분하다면 거래가 진행되고 포트폴리오와 거래 원장에 반영

</details>

<details>
  <summary><b>/trade/eval</b></summary>
  
  <img src='./img/api15.png'>
  <br>

  - 현재 접속한 유저의 총 주식평가액을 출력

</details>

<br>

# Tech Stack

### FastAPI

> 이 기술을 프로젝트에 선택한 이유는?
> 
- rest api개발이 처음이었고 3주라는 한정된 기간 내에 구현해야 했던 만큼, 코드 작성이 간단하고 배우기 쉬우며 버그가 적다는 점에서 적합하다고 판단하였다.

> 어떻게 사용했는가?
> 
- passlib 과 jwt 토큰을 이용하여 비밀번호 해시와 인증을 구현하고 한국투자증권 API와 연동하여 주식데이터를 크롤링하여 모의주식 매매와 포트폴리오 CRUD를 구현하였다.

> 사용하면서 어려웠던 점
> 
- 관련 레퍼런스가 적어 퀵스타트 예제를 벗어나는 기능은 구현하는 데 어려움이 있었다. rest api에 대해 복습을 하고 유닛 테스트를 통해 crud가 어떻게 적용되는지 숙달되면서 해결하였다.

<br>

### MySQL

> 이 기술을 프로젝트에 선택한 이유는?
> 
- 해당 프로젝트는 주된 데이터가 추후에 확장되기보다, 데이터의 구조가 명확한 정형 데이터라고 판단하였다. 따라서 RDBMS는 데이터를 2차원 테이블 형태로 관리할 수 있다는 점에서 적합하다고 판단하였다.

> 어떻게 사용했는가?
> 
- schema를 작성하고 기본 데이터를 입력할 때에는 python의 mysqldb 라이브러리를 사용해 SQL 쿼리를 직접 작성하였고 FastAPI 상에서 데이터를 전송할 때에는 ORM 기반의 sqlalchemy 라이브러리를 이용하였다.

> 사용하면서 어려웠던 점
> 
- 미리 스키마 구조를 설계하지 않고 데이터베이스를 구축했더니 잘 쓰이지 않는 칼럼이나 필요하지만 없는 테이블이 있거나 테이블 간의 1:N, N:1 구조가 명확하지 않았다. 이전까지는 ER다이어그램을 통해 스키마를 설계하는 것을 글로만 보고 대수롭지 않게 생각했었지만 이번 프로젝트를 계기로 그 중요성을 체감하게 되었다.

<br>

# 프로젝트 회고

### KTP 회고

> Keep (지속할 것) : 긍정적인 요소
> 
- 백엔드 Rest API부터 데이터베이스 설계까지 모두 경험해 볼 수 있던 점
- 피드백을 받았을 때 빠르게 수용하고 개선해 나간 점

> Problem (해결할 것) : 부정적인 요소
> 
- FastAPI와 Rest API의 숙련도가 충분하지 않아 일정이 지체된 점
- Front-end와 연결하지 못하여 배포까지 이루어지지 못한 점

> Try (시도할 것) : Problem에 대한 해결책, 잘 하고 있는 것을 더 잘하기 위해서는?
> 
- 사용자 인터페이스까지 완성해서 배포까지 이루어지는 3-Tier 아키텍쳐를 완성해 보는 것
- 웹개발 숙련도를 높여 상용 서비스까지 구현해 보는 것

### 느낀점

- 데이터 엔지니어링을 위해 백엔드 지식이 필수적이라는 것을 체감하게 되었고 서비스 유지보수를 위해 어떤 지점을 모니터링 해야하는지 알게 되어 좋은 경험이 되었다.
- 숙련도가 부족하다는 것이 일정과 결과물에 어떤 영향을 미치는지 깨닫게 되었고 평소에 숙달시키는 것이 중요하다는 것을 잘 알게 되었다.
- 개인적으로 남는 시간에 했더라면 절대 같은 시간동안 못할 만큼 구현이 이루어 져서 짧은 시간에 몰입하는 경험을 할 수 있었다.