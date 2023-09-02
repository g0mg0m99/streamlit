import streamlit as st

st.set_page_config(
    page_title='공동교육과정',
    page_icon='¯\_(ツ)_/¯'
)

menu = st.sidebar.selectbox('MENU',['BMI 지수 계산기','원의 넓이 계산기','전화번호 맞추기'])

if menu == 'BMI 지수 계산기':
    st.subheader('BMI 지수 계산기')
    #몸무게 / 키의 제곱

    height = st.number_input('키를 입력해주세요(M) : ')
    weight = st.number_input('몸무게를 입력해주세요(Kg) : ',step=1)
    BMI = weight/(height*height)
    weight = weight/100
    # 과제 1 저체중 / 정상 / 과체중 / 경도 비만 / 중증도 비만 등등 만들기.
    btn = st.button('계산하기')
    if btn:
        st.write('당신의 BMI 지수는',BMI,'입니다.')
        if BMI < 20:
            st.write('당신의 BMI 수치는 저체중 입니다.')
        elif BMI <= 20 and BMI >= 24:
            st.write('당신의 BMI 수치는 정상 입니다.')
        elif BMI <= 25 and BMI >= 29:
            st.write('당신의 BMI 수치는 과체중 입니다.')
        else:
            st.write('당신의 BMI 수치는 비만 입니다.')

# 괴제 2 반지름 입력 받고 원의 넓이 구하기.
elif menu == '원의 넓이 계산기':
    st.subheader('원의 넓이 게산기')
    r = st.number_input('반지름을 입력하세요 : ',step=1)
    btn = st.button('원의 넓이를 계산하기')
    if btn:
        st.write('원의 넓이는',(r*r*3.14),'입니다.')

# 과제 3 나만의 프로그램 만들기. ( 전부 잘못 된거 같아요)
elif menu == '전화번호 맞추기':
    st.subheader('제가 당신의 전화번호를 맞춰볼게요.')
    nun1 = st.sidebar.text_input('당신의 전화번호 앞자리(4개)를 적어주세요(010 제외) : ',step=1,type='password')
    nun2 = st.sidebar.text_input('당신의 전화번호 뒷자리(4개)를 적어주세요(010 제외) : ',step=1,type='password')
    btn = st.button('제가 당신의 번호를 맞춰보겠습니다.')
    if btn:
        st.write('당신의 번호는',((nun1*80*250)+nun2)/2,'입니다.')



