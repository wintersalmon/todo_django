# ToDo Django

* 프로젝트 소개
	* [**개요**](#개요)
	* [**기술스택**](#기술스택)
	* [**요구사항**](#요구사항)
* 프로젝트 설명
    * [**기능**](#포르젝트-기능)
    * [**모델**](#프로젝트-모델)

## 프로젝트 소개

### 개요
- 파이썬/장고를 활용한 간단한 ToDo 리스트

### 기술스택
- python (3.6.3)
- Django (2.1.2)
- DjangoRestFramework (3.9.0)
- Bootstrap (4.1.3)
- FontAwesome (5.5.0)

## 프로젝트 설명

### 프로젝트 실행 방법

```
$ cd PROJECT_ROOT
$ pip -r install requirements.txt
$ cd django_app
$ python manage.py runserver

## 로컬 브라우져에서 접속 http://localhost:8000/

```

### 프로젝트 기능
- Task 추가 (제목, 내용, 마감일)
- Task 상태 변경 (완료/미완료 토글)
- Task 목록 내 순서 변경
- 기간이 지난 Task 보기
- 전체 Task 보기

### 프로젝트 모델

**Category**


| name  | type | etc       |
|-------|------|-----------|
| title | char | max=32 PK |


**Task**


| name       | type     | etc                      |
|------------|----------|--------------------------|
| title      | FK       | Category                 |
| content    | char     | max=100                  |
| status     | char     | choices(A,O,D) default=A |
| priority   | int      | positive                 |
| position   | int      | positive                 |
| created_at | datetime | auto now                 |
| due_date   | datetime | nullable                 |

