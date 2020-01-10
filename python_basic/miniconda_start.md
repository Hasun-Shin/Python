# miniconda 설치 및 가상환경 설치

주의사항 : 한글폴더, 띄어쓰기 잘 사용하지 않기 ! 

![image-20200110094021144](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20200110094021144.png)



- jupyter notebook 설치하기

  cmd 창에 

`conda install jupyter`

- jupyter notebook 구동하기.

  cmd  창에

`jupyter notebook` 입력.

만약에 자동적으로 실행이 안되면 아래와 같은 주소로 들어가기. 

http://localhost:8888/?token=26183989f653ead8ac6a2007da0b16a9aecc0998f5a068a0

ctrl c : 서버 종료 





- **가상환경** : 예를들어, 어떤 책의 프로그램을 따라한다면, 그 책의 환경과 똑같은 설정을 하기 위해 가상환경을 설치하여 그에 맞는 라이브러리를 설치해서 사용한다. 

  1. 파이썬 자체에서 생성
  2.  아나콘다의 가상환경 : 파이썬의 버전도 임의로 정할 수 있다.

- 아나콘다의 가상환경

  1. cmd 

     - conda create --name myenv
     - activate myenv : 가상환경실행
       - conda list : 이 가상환경에서 설치되어 있는 라이브러리 확인. 
       - 가상환경은 꼭 miniconda3의 env 폴더에서 만들어진다. 
     - deactivate myenv : 가상환경 종료. 오리지널에서 작업

     

