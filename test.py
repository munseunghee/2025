# app.py
import streamlit as st
import random

# [1] 기본 아이돌 목록
default_idols = [
    {"name": "정국 (BTS)", "img": "https://example.com/jungkook.jpg"},
    {"name": "뷔 (BTS)", "img": "https://example.com/v.jpg"},
    {"name": "성한빈 (ZB1)", "img": "https://example.com/hanbin.jpg"},
    {"name": "민현 (뉴이스트)", "img": "https://example.com/minhyun.jpg"},
    {"name": "지성 (NCT)", "img": "https://example.com/jisung.jpg"},
    {"name": "태용 (NCT)", "img": "https://example.com/taeyong.jpg"},
    {"name": "차은우 (Astro)", "img": "https://example.com/cha_eunwoo.jpg"},
    {"name": "제이홉 (BTS)", "img": "https://example.com/jhope.jpg"},
    {"name": "백현 (EXO)", "img": "https://example.com/baekhyun.jpg"},
    {"name": "카이 (EXO)", "img": "https://example.com/kai.jpg"},
    {"name": "도영 (NCT)", "img": "https://example.com/doyoung.jpg"},
    {"name": "원빈 (RIIZE)", "img": "https://example.com/wonbin.jpg"},
    {"name": "김요한(엑스원)", "img": "https://example.com/kim_yohan.jpg"},
    {"name": "박지훈(워너원)", "img": "https://example.com/park_jihun.jpg"},
    {"name": "시온 (NCT WISH)", "img": "https://example.com/shion.jpg"},
    {"name": "박성훈(엔하이픈)", "img": "https://example.com/sunghoon.jpg"}
]

st.title("남자 아이돌 이상형 월드컵 👑")
st.write("16강 → 8강 → 4강 → 결승 → 우승자!")

# ------------------- AI 분석 함수 -----------------
def analyze_winner(name):
    if "성한빈" in name:
        return "당신은 순수하고 청량한 리더십 있는 타입을 좋아하네요!"
    elif "원빈" in name:
        return "멋있고 카리스마 있는 청춘영화 주인공 같은 스타일을 좋아하네요!"
    else:
        return "감각적이고 매력적인 스타일을 선호하는 것 같아요!"

# ------------------ 사이드바 옵션 -----------------
st.sidebar.header("⚙ 옵션 설정")
custom_mode = st.sidebar.checkbox("커스텀 모드 (직접 멤버 입력)", value=False)

if custom_mode:
    user_input = st.sidebar.text_area(
        "아이돌 이름을 쉼표 또는 줄바꿈으로 8명 이상 입력",
        placeholder="예: 지민, 정국, 성한빈, 차은우..."
    )
    apply_custom = st.sidebar.button("커스텀 적용하기")

# 초기 라운드 설정 (기본값)
if "round" not in st.session_state:
    st.session_state.round = default_idols
    st.session_state.next_round = []
    st.session_state.index = 0
    st.session_state.stage = len(default_idols)

# 커스텀 적용 버튼 눌렀을 때 처리
if custom_mode and 'apply_custom' in locals() and apply_custom:
    names = [x.strip() for x in user_input.replace('\n', ',').split(',') if x.strip()]
    if len(names) < 8:
        st.sidebar.warning("8명 이상 입력해야 시작할 수 있어요!")
    else:
        # 커스텀 이름만으로 idol 리스트 생성 (img는 임시 공용)
        custom_idols = [{"name": name, "img": "https://example.com/default.jpg"} for name in names]
        random.shuffle(custom_idols)
        # 세션 초기화 + 반영
        st.session_state.round = custom_idols
        st.session_state.next_round = []
        st.session_state.index = 0
        st.session_state.stage = len(custom_idols)
        st.experimental_rerun()

# ------------------- 라운드 로직 -----------------
def choose_idol(idol):
    st.session_state.next_round.append(idol)
    st.session_state.index += 2
    if st.session_state.index >= len(st.session_state.round):
        st.session_state.round = st.session_state.next_round
        st.session_state.next_round = []
        st.session_state.index = 0
        st.session_state.stage //= 2

# --------------- 메인화면: 토너먼트 ---------------
if len(st.session_state.round) == 1:
    winner = st.session_state.round[0]
    st.header("🏆 최종 우승자!")
    st.subheader(winner["name"])
    st.image(winner["img"], width=300)
    comment = analyze_winner(winner["name"])
    st.markdown(f"**AI 분석 결과**: {comment}")

    if st.button("다시 시작하기"):
        st.session_state.clear()
        st.experimental_rerun()

else:
    left = st.session_state.round[st.session_state.index]
    right = st.session_state.round[st.session_state.index + 1]
    st.subheader(f"{st.session_state.stage}강")
    col1, col2 = st.columns(2)

    with col1:
        st.image(left["img"], width=250)
        if st.button(left["name"] + " 선택", key=f"left_{st.session_state.index}"):
            choose_idol(left)

    with col2:
        st.image(right["img"], width=250)
        if st.button(right["name"] + " 선택", key=f"right_{st.session_state.index}"):
            choose_idol(right)



