# app.py
import streamlit as st
import random

# -----------------------------
# 남자 아이돌 16명 (이름 + 이미지 URL 자리)
# ⚠ 이미지는 나중에 직접 URL로 교체해도 되고 임시로 넣어둔 상태
# -----------------------------
idols = [
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

# 캐릭터 섞기
random.shuffle(idols)

st.title("남자 아이돌 이상형 월드컵 👑")
st.write("16강 → 8강 → 4강 → 결승 → 우승자!")

# 초기화
if "round" not in st.session_state:
    st.session_state.round = idols
    st.session_state.next_round = []
    st.session_state.index = 0
    st.session_state.stage = 16

def choose_idol(idol):
    st.session_state.next_round.append(idol)
    st.session_state.index += 2

    # 라운드 끝나면 다음 라운드 세팅
    if st.session_state.index >= len(st.session_state.round):
        st.session_state.round = st.session_state.next_round
        st.session_state.next_round = []
        st.session_state.index = 0
        st.session_state.stage //= 2

# 우승자 한 명만 남은 경우
if len(st.session_state.round) == 1:
    winner = st.session_state.round[0]
    st.header("🏆 최종 우승자!")
    st.subheader(winner["name"])
    st.image(winner["img"], width=300)
    st.button("다시 시작하기", on_click=lambda: st.session_state.clear())

else:
    # 현재 대결 중인 두 명
    left = st.session_state.round[st.session_state.index]
    right = st.session_state.round[st.session_state.index + 1]

    st.subheader(f"{st.session_state.stage}강")
    col1, col2 = st.columns(2)

    with col1:
        st.image(left["img"], width=250)
        if st.button(left["name"] + " 선택"):
            choose_idol(left)

    with col2:
        st.image(right["img"], width=250)
        if st.button(right["name"] + " 선택"):
            choose_idol(right)
          # app.py
import streamlit as st
import random

# -----------------------------
# 남자 아이돌 16명 (이름 + 이미지 URL 자리)
# -----------------------------
idols = [
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


random.shuffle(idols)
st.title("남자 아이돌 이상형 월드컵 👑")
st.write("16강 → 8강 → 4강 → 결승 → 우승자!")

# -------------------------------
# AI 분석 메시지 함수
# -------------------------------
def analyze_winner(name):
    if "성한빈" in name:
        return "당신은 순수하고 청량한 리더십 있는 타입을 좋아하네요!"
    elif "원빈" in name:
        return "멋있고 카리스마 있는 청춘영화 주인공 같은 스타일을 좋아하네요!"
    elif "차은우" in name:
        return "말 그대로 얼굴 천재! 완벽한 외모를 중요한 기준으로 보는군요!"
    elif "정국" in name or "뷔" in name or "지민" in name:
        return "아이돌 중에서도 다정하고 재능 있는 멀티형을 좋아하는군요!"
    else:
        return "감각적이고 매력적인 스타일을 선호하는 것 같아요!"

# 초기화
if "round" not in st.session_state:
    st.session_state.round = idols
    st.session_state.next_round = []
    st.session_state.index = 0
    st.session_state.stage = 16

def choose_idol(idol):
    st.session_state.next_round.append(idol)
    st.session_state.index += 2

    if st.session_state.index >= len(st.session_state.round):
        st.session_state.round = st.session_state.next_round
        st.session_state.next_round = []
        st.session_state.index = 0
        st.session_state.stage //= 2

# 우승자 한 명만 남은 경우
if len(st.session_state.round) == 1:
    winner = st.session_state.round[0]
    st.header("🏆 최종 우승자!")
    st.subheader(winner["name"])
    st.image(winner["img"], width=300)

    # 여기 추가된 부분
    comment = analyze_winner(winner["name"])
    st.markdown(f"**AI 분석 결과**: {comment}")

    st.button("다시 시작하기", on_click=lambda: st.session_state.clear())

else:
    left = st.session_state.round[st.session_state.index]
    right = st.session_state.round[st.session_state.index + 1]

    st.subheader(f"{st.session_state.stage}강")
    col1, col2 = st.columns(2)

    with col1:
        st.image(left["img"], width=250)
        if st.button(left["name"] + " 선택"):
            choose_idol(left)

    with col2:
        st.image(right["img"], width=250)
        if st.button(right["name"] + " 선택"):
            choose_idol(right)


