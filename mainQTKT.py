import streamlit as st
import streamlit.components.v1 as components
st.set_page_config(layout="wide", page_title="Báo cáo Điều dưỡng")

# 1. DANH SÁCH NHÂN VIÊN (Bạn có thể thêm tiếp vào đây)
USERS = {
    "admin": "phuongchau3080",
    "PC-00645": "phuongchau",
    "PC-00245": "phuongchau",
    "PC-00950": "phuongchau",
    "PC-00067": "phuongchau",
    "PC-00076": "phuongchau",
    "PC-00505": "phuongchau",
    "PC-20082": "phuongchau",
    "PC-20271": "phuongchau",
    "PC-20139": "phuongchau",
    "PC-20102": "phuongchau",
    "PC-20351": "phuongchau",
    "PC-10222": "phuongchau",
    "PC-10142": "phuongchau",
    "PC-10398": "phuongchau",
    "PC-10139": "phuongchau",
    "PC-10075": "phuongchau",
    "PC-10136": "phuongchau",
    "PC-10391": "phuongchau",
    "PC-10063": "phuongchau",
    "PC-30067": "phuongchau",
    "PC-30081": "phuongchau",
    "PC-30080": "phuongchau",
    "PC-30562": "phuongchau",
    "PC-30165": "phuongchau",
    "PC-30206": "phuongchau",
    "PC-30308": "phuongchau",
    "PC-20351": "phuongchau",
    "PC-20066": "phuongchau",
    "PC-20176": "phuongchau",
    "PC-20252": "phuongchau",
    "PC-20211": "phuongchau",
    "PC-20467": "phuongchau",
    "PC-20376": "phuongchau",
    "PC-20036": "phuongchau",
    "PC-20031": "phuongchau",
    "PC-20035": "phuongchau",
    "PC-20062": "phuongchau",
    "PC-20467": "phuongchau",
    "PC-00080": "phuongchau",
    "PC-00075": "phuongchau",
    "PC-00358": "phuongchau",
    "PC-00380": "phuongchau",
    "PC-00117": "phuongchau",
    "PC-00824": "phuongchau",
    "PC-00533": "phuongchau",
    "PC-00070": "phuongchau",
    "PC-00132": "phuongchau",
    "PC-00361": "phuongchau",
    "PC-00595": "phuongchau",
    "PC-00066": "phuongchau",
    "PC-00571": "phuongchau",
    "PC-00871": "phuongchau",
    "PC-00475": "phuongchau",
    "PC-00079": "phuongchau",
    "PC-00341": "phuongchau",
    "PC-00094": "phuongchau",
    "PC-01533": "phuongchau",
    "PC-01671": "phuongchau",
    "PC-00825": "phuongchau",
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

    # --- CHỈNH KÍCH THƯỚC KHUNG ---
    # width=None và dùng CSS để ép chiều rộng 100%
    components.iframe(power_bi_link, width=1800, height=1000, scrolling=True)
