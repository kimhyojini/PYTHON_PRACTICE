# [실습 4] 
# 과목별 점수가 담긴 리스트(scores)를 입력받아 합격 여부를 판정하는 함수를 만드시오.

# [합격 조건]
# 1. 모든 과목의 평균 점수가 60점 이상이어야 합니다.
# 2. 단, 한 과목이라도 40점 미만(과락)이 있으면 평균과 관계없이 'FAIL'입니다.

# [반환값]
# 합격일 경우 "PASS", 불합격일 경우 "FAIL"을 반환

# mean=sum(scores)/len(scores)
# def check_result(scores):
    # pass를 지우고 로직을 작성합니다.
#내가 처음에 적은답 
    # if mean == >60:
    #     print(PASS)
    # elif scores <40 :
    #     print(FALE)

def check_result(scores):
#1.과락확인
    for score in scores:
        if score<40:
            return "FAIL"
#2.평균값 계산하기 
    mean= sum(scores)/len(scores)
    
#3.평균값에 대한 과락 설정하기 
    if mean >= 60 :
        return "PASS"
    else:
        return "FAIL"
      
# 첫답안def check_result(scores):
#1.과락체크
    for score in scores:
        if score < 40 :
            return "FAIL" 
#2.평균계산
    avg = sum(scores)/len(scores)
#3.평균조건검사
    if avg > 60:
        return "PASS"
    else:
        return "FAIL"






# 테스트 코드
print(f"결과 1 (PASS 예상): {check_result([80, 90, 75])}")
print(f"결과 2 (FAIL 예상): {check_result([100, 100, 35])}")
print(f"결과 3 (FAIL 예상): {check_result([50, 50, 50])}")
