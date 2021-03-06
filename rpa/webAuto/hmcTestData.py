from dataclasses import dataclass

@dataclass(init=True, repr=True)
class hmcTestData:
    gbn:             str = None # 구분
    emNo:            str = None # 사용자사번
    custNm:          str = None # 고객명
    prdCd:           str = None # 상품코드
    prdNm:           str = None # 상품명
    contrRrno:       str = None # 계약자생년월일 (8자리)
    contrGndr:       str = None # 계약자성별 (남/여)
    contrInsdSameYn: str = None # 계약자와 주피 동일(Y/N)
    insdRrno:        str = None # 주피생년월일
    insdGndr:        str = None # 주피성별
    insdJobCode:     str = None # 주피직종
    insd1Rrno:       str = None # 종피1생년월일
    insd1Gndr:       str = None # 종피1성별
    insd1JobCode:    str = None # 종피1직종
    insd2Rrno:       str = None # 종피1생년월일
    insd2Gndr:       str = None # 종피1성별
    insd2JobCode:    str = None # 종피1직종
    insd3Rrno:       str = None # 종피1생년월일
    insd3Gndr:       str = None # 종피1성별
    insd3JobCode:    str = None # 종피1직종
    insType1:        str = None # 보험종류1
    insType2:        str = None # 보험종류2
    insType3:        str = None # 보험종류3
    insType4:        str = None # 보험종류4
    insType5:        str = None # 보험종류5
    hbdyObjYn:       str = None # 건강체여부
    slctdPlan:       str = None # 플랜선택
    mnins:           str = None # 주계약
    insPrm:          int = None # 보험료금액(가입/합계)
    antyOpenAge:     str = None # 연금설계탭-연금개시나이
    antyExAgeGap:    str = None # 연금설계탭-예시나이간격
    swtObjPerson:    str = None # 스마트전환탭-전환대상자
    swtTime:         str = None # 스마트전환탭-전환시점
    swtInsPrd:       str = None # 스마트전환탭-보험기간
    swtInsPmPrd:     str = None # 스마트전환탭-납입기간
    antyPrePayAge:   str = None # 연금선지급탭-선지급나이
    antyPrePayRto:   float = None # 연금선지급탭-선지급비율
    antyPrePayPrd:   str = None # 연금선지급탭-선지급기간
    antyPrmPayAll:   str = None # 연금보험료(거치) (연금상품 선택시에만 입력)
    antyPrmPayPrt:   str = None # 연금보험료(적립) (연금상품 선택시에만 입력)
    antyPayTyp:      str = None # 연금지급형태    (연금상품 선택시에만 입력)
    antyOpn:         str = None # 연금개시       (연금상품 선택시에만 입력)
    antyFocusPrd:    str = None # 연금집중기간    (연금상품 선택시에만 입력)
    insPrd:          str = None # 보험기간
    pmPrd:           str = None # 납입기간
    pmCyl:           str = None # 납입주기
    rfndExcpYn:      str = None # 환급특약제외
    pmExptExcpYn:    str = None # 납입면제특약제외
    spcdCod1:        str = None # 특약코드
    spcdNm1:         str = None # 특약명
    spcdAmt1:        str = None # 특약금액
    spcdPrd1:        str = None # 특약보험기간
    spcdPmPrd1:      str = None # 특약납입기간
    spcdCod2:        str = None # 특약코드
    spcdNm2:         str = None # 특약명2
    spcdAmt2:        str = None # 특약금액2
    spcdPrd2:        str = None # 특약보험기간2
    spcdPmPrd2:      str = None # 특약납입기간2
    spcdCod3:        str = None # 특약코드3
    spcdNm3:         str = None # 특약명3
    spcdAmt3:        str = None # 특약금액3
    spcdPrd3:        str = None # 특약보험기간3
    spcdPmPrd3:      str = None # 특약납입기간3
    spcdCod4:        str = None # 특약코드4
    spcdNm4:         str = None # 특약명4
    spcdAmt4:        str = None # 특약금액4
    spcdPrd4:        str = None # 특약보험기간4
    spcdPmPrd4:      str = None # 특약납입기간4
    spcdCod5:        str = None # 특약코드5
    spcdNm5:         str = None # 특약명5
    spcdAmt5:        str = None # 특약금액5
    spcdPrd5:        str = None # 특약보험기간5
    spcdPmPrd5:      str = None # 특약납입기간5
    etc:             str = None # 비고
