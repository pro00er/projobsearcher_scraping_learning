## 전제조건
- 형식이 유효한 파일만 읽음
```    
    Ling,Mai,55900
    Johnson,Jim,56500
    Jones,Aaron,46000
    Jones,Chis,34500
    Switft,Geoffrey,14200
    Xiong,Fong,65000
    Zarnecki,Sabrina,51500
```


## TODO 요구사항
- 쉼표단위로 단어 파싱
- 단어 출력   
- 컬럼의 줄을 맞추기 위해 공백 글자를 사용

## 설계
- [ ] 결과값이 만들어졌다는 전제
- parsing -> result 생성
- 요구사항을 충족한 각 row와 column 단위를 합쳐서 최종결과 만듦
- test
   - parsing 제대로 해왔는지
   - result 값 요구조건에 맞는지
   - row 조건과 column 조건을 분리해서 테스트케이스 설계 


## 요구사항 TestCase list
### 파싱이 제대로 되었는지 확인
- 쉼표단위로 파싱되었는지 확인

### 단위 결과값 요구조건에 맞는지
- row parsing 
  - 한 열의 단어가 세 개인지
- column parsing
  - n번째 컬럼의 스트링 가져오는지
    - 첫번째 컬럼의 스트링 가져오는지
  - 컬럼길이가 가장 긴 단어 더하기 공백 한글자인지 확인
    - 한 칼럼의 최대 길이 단어 가져오는지 확인
  - 같은 열의 (공백을 포함한)단어가 같은 길이를 가지는지 확인

### 결과가 제대로 나왔는지 확인
- last값 단어가 첫번째 열에 있는지 확인
- first값 단어가 두번째 열에 있는지 확인
- salary값 단어가 세번째 열에 있는지 확인