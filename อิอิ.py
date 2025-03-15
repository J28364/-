import streamlit as st
from PIL import Image
import random


# หน้าแรก
def home():
    st.title("แอปดูดวงด้วยรูปภาพ")
    st.write("ยินดีต้อนรับสู่แอปพลิเคชันดูดวง!")
    if st.button("เริ่มต้นดูดวง"):
        st.session_state['page'] = 'quiz'


# หน้าตอบคำถาม
def quiz():
    st.title("ตอบคำถามเพื่อดูดวง")

    # รายการคำถาม
    questions = [
        {"question": "วันนี้คุณรู้สึกอย่างไร?", "options": ["มีความสุข", "เหนื่อยล้า", "ตื่นเต้น", "สงบ"]},
        {"question": "คุณต้องการพลังด้านใด?", "options": ["กำลังใจ", "ความรัก", "ความสงบ", "โชคลาภ"]},
        {"question": "คุณมองอนาคตข้างหน้าเป็นอย่างไร?", "options": ["สดใส", "ไม่แน่นอน", "น่าตื่นเต้น", "เรียบง่าย"]}
    ]

    # เก็บคำตอบทั้งหมด
    user_answers = []
    for q in questions:
        st.subheader(q["question"])
        answer = st.radio("", q["options"], key=q["question"])
        user_answers.append(answer)

    if st.button("ส่งคำตอบ"):
        st.session_state['answers'] = user_answers
        st.session_state['page'] = 'result'


# หน้าผลลัพธ์
def result():
    st.title("ผลลัพธ์ของการดูดวง")

    # รายการรูปภาพ (ปรับเส้นทางตามตำแหน่งไฟล์ของคุณ)
    images = ["happy.jpg", "sad.jpg", "happppp.jpg", "saddddd.jpg"]

    # สุ่มรูปภาพ
    selected_image = random.choice(images)

    # แสดงผลลัพธ์ตามภาพที่สุ่มได้
    if selected_image == "happy.jpg":
        st.write("ความหมายของดวง:")
    elif selected_image == "sad.jpg":
        st.write("ความหมายของดวง:")
    elif selected_image == "happppp.jpg":
        st.write("ความหมายของดวง: ")
    elif selected_image == "saddddd.jpg":
        st.write("ความหมายของดวง:")

    # แสดงภาพ
    try:
        image = Image.open(selected_image)
        st.image(image, caption="ภาพนี้สะท้อนดวงของคุณ")
    except FileNotFoundError:
        st.error("ไม่พบไฟล์รูปภาพ โปรดตรวจสอบเส้นทางหรือชื่อไฟล์อีกครั้ง!")

    # แสดงผลลัพธ์จากคำตอบ
    st.write("คำตอบของคุณคือ:")
    for answer in st.session_state['answers']:
        st.write(f"- {answer}")

    if st.button("กลับไปหน้าแรก"):
        st.session_state['page'] = 'home'


# แอปพลิเคชันหลัก
if 'page' not in st.session_state:
    st.session_state['page'] = 'home'

if st.session_state['page'] == 'home':
    home()
elif st.session_state['page'] == 'quiz':
    quiz()
elif st.session_state['page'] == 'result':
    result()