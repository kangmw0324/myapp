import streamlit as st 

st.title("상자그림 수업 도구!!")
st.info("먼저 학번을 입력해주세요. 활동 결과는 이 학번으로 저장이 됩니다. ")
# alt + z(window) / option + z(mac)

student_id = st.text_input("학번 (예:30101)", 
value = st.session_state.get("학번", ""))

if student_id:
    st.session_state["학번"] = student_id
    st.success(f"{student_id}학생 환영합니다! 왼쪽 메뉴에서 활동을 시작해주세요.") # fstring
    