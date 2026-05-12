import streamlit as st
import streamlit.components.v1 as components

# 1. DANH SÁCH NHÂN VIÊN (Bạn có thể thêm tiếp vào đây)
USERS = {
    "admin": "phuongchau3080",
    "PC-00645": "phuongchau",
    "PC-00245": "phuongchau",
    "PC-00950": "phuongchau",
    "PC-00067": "phuongchau",
    "PC-00505": "phuongchau",
    "PC-20082": "phuongchau",
    "PC-20271": "phuongchau",
    "PC-20139": "phuongchau",
    "PC-10222": "phuongchau",
    "PC-10142": "phuongchau",
    "PC-00076": "phuongchau",
    "PC-30210": "phuongchau",
    "PC-30067": "phuongchau",
    "PC-30081": "phuongchau",
    "PC-30080": "phuongchau",
    "PC-01817": "phuongchau"
}

if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if not st.session_state['logged_in']:
    st.title("QTKT Điều Dưỡng Tập Đoàn")
    user_id = st.text_input("Mã nhân viên")
    password = st.text_input("Mật khẩu", type="password")
    if st.button("Đăng nhập"):
        if user_id in USERS and USERS[user_id] == password:
            st.session_state['logged_in'] = True
            st.rerun()
        else:
            st.error("Sai thông tin!")
else:
    st.title("QTKT Điều Dưỡng Tập Đoàn")
    if st.button("Đăng xuất"):
        st.session_state['logged_in'] = False
        st.rerun()

    # THAY LINK POWER BI CỦA BẠN VÀO GIỮA DẤU NGOẶC KÉP DƯỚI ĐÂY
    power_bi_link = "https://app.powerbi.com/view?r=eyJrIjoiYWUxN2I1NzQtOTBiNy00MzYzLWFlY2YtNWVjMThjMjdiNzZiIiwidCI6IjhiZDRiMTQ5LTdmODItNDY3Ny1iNDQzLWQyNDk3NWRkOTAzMCIsImMiOjEwfQ%3D%3D"

    components.iframe(power_bi_link, height=800, scrolling=True)
