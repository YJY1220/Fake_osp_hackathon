# OSP09_Final_Project
오픈소스프로그래밍 기말대체과제 팀프로젝트 9조 결과물

## 구현 일정
|**날짜**|내용|
|----|-----|
|**0531**|1.인턴채용정보 크롤링 구현|
|        |2.github repo 파기|
|**0601**|1.대면회의 - 전체적 개발 일정 결정|
|        |2. github issue 활용법 전체 습득|
|        |3. 크롤링 기능 및 db 구현 기능 논의|
|        |4. 다음 대면회의 날짜 fix 및 구현할 것 정하기|

## Github Issue 사용법
> 1. issue template 등록
> * Bug report
> * Feature request
> 2. github issue Milestone 등록
> * 프론트엔드
> * 백엔드
> * 향후 완성 시, 전체 main으로 push 후 실행되면 완성용 마일스톤 하나 생성
> 3. issue 기반 branch들 생성
>> **프론트엔드**
>> *크게 5개의 issue, branch 생성*
>> * main page 화면 (검색창 포함)
>> * main page의 직군 선택 후 기업 보여주는 화면 html
>> * 해당 기업 아이콘 누르면 나오는 크롤링 화면 html
>> * 크롤링 내역의 제목, 요약 내용 클릭 시 해당공고 사이트로 연결되는 하이퍼링크 기능 구현
>> * 검색창에 검색어 입력 시, 검색결과 보여주는 html
>>
>> **백엔드**
>> *크게 5개의 issue, branch 생성*
>> * 분야별 채용 공고 내용 제목, 세부 내용 크롤링 구현
>> * 크롤링 내용 elasticsearch database 저장
>> * 검색 input data와 database 유사도 분석
>> * 유사도 높은 내용 있을 시, 해당 채용 공고 내용 elasticsearch에서 호출
>> * 호출 내용 list로 page에 보여줌 → 이 내용 누르면 위의 프론트에서처럼 하이퍼링크로 해당 세부사항 채용공고 페이지로 넘어감
> 4. 각 issue 설명 적은 후 assigners, label, milestone(백이면 백, 프론트면 프론트) 설정 후 issue 생성
> 5. 해당 기능 branch 생성
> 6. 해당 기능 구현은 해당 branch 내에서 코드 구현 및 push
> 7. 해당 기능 구현 종료 시, main에 pull request (원격 수동)
> 8. pull request 시, commit message "#issue-number message" 이 형식으로 적어서 linked issue 할 것
> *linked issue의 commit message 적는 방법은 default branch(main)에 타 브랜치에서 PR 할 경우만 가능*
> 9. pull request 및 merge
> 10. milestone 및 issue closed 확인
> 11. **본인 local git pull 꼭 하기**

