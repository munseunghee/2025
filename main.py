# app.py
# -*- coding: utf-8 -*-
import streamlit as st

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="MBTI 캐릭터 & 추천",
    page_icon="🎯",
    layout="wide",
)

# -----------------------------
# MBTI별 캐릭터 정보 + 추천 콘텐츠
# -----------------------------
MBTI_DATA = {
    "INTJ": {
        "emoji": "🦉",
        "name": "Luca",
        "gender": "남",
        "look": "sharp grey eyes, sleek black suit, neat slicked-back hair",
        "style": "minimal, modern, high-contrast",
        "vibe": "cool, strategic, charismatic",
        "tagline": "계획이 세상을 지배한다.",
        "movie": ["인셉션", "인터스텔라", "셜록 홈즈"],
        "music": ["Hans Zimmer - Time", "Ludovico Einaudi - Experience"],
        "travel": ["아이슬란드", "스위스 알프스", "교토"],
    },
    "INFJ": {
        "emoji": "🌙",
        "name": "Serah",
        "gender": "여",
        "look": "long silver hair, calm blue eyes, white flowing dress",
        "style": "soft, ethereal, luminous",
        "vibe": "mysterious yet warm",
        "tagline": "모든 선택에는 이유가 있어.",
        "movie": ["어바웃 타임", "이터널 선샤인", "라비앙 로즈"],
        "music": ["Yiruma - River Flows in You", "Adele - Someone Like You"],
        "travel": ["파리", "프라하", "산토리니"],
    },
    "ENTP": {
        "emoji": "🔥",
        "name": "Jay",
        "gender": "남",
        "look": "short blonde hair, playful smile, layered streetwear",
        "style": "dynamic, urban, candid",
        "vibe": "clever and adventurous",
        "tagline": "재밌으면 해보는 거지!",
        "movie": ["아이언맨", "캐치 미 이프 유 캔", "데드풀"],
        "music": ["Queen - Don't Stop Me Now", "Imagine Dragons - Believer"],
        "travel": ["라스베이거스", "뉴욕", "두바이"],
    },
    "ENFP": {
        "emoji": "🌈",
        "name": "Ari",
        "gender": "여",
        "look": "bob cut, bright hazel eyes, colorful casual outfit",
        "style": "vibrant, whimsical, sunny",
        "vibe": "energetic and uplifting",
        "tagline": "세상은 모험이야!",
        "movie": ["라라랜드", "월터의 상상은 현실이 된다", "모아나"],
        "music": ["Coldplay - Adventure of a Lifetime", "Pharrell Williams - Happy"],
        "travel": ["발리", "바르셀로나", "퀸스타운"],
    },
    "ISTJ": {
        "emoji": "📚",
        "name": "Ethan",
        "gender": "남",
        "look": "neat brown hair, glasses, formal navy suit",
        "style": "classic, structured, timeless",
        "vibe": "reliable and detail-oriented",
        "tagline": "규칙은 이유가 있다.",
        "movie": ["포레스트 검프", "캐스트 어웨이", "그린 마일"],
        "music": ["The Beatles - Hey Jude", "Simon & Garfunkel - The Sound of Silence"],
        "travel": ["스위스", "노르웨이 피오르드", "교토"],
    },
}

# -----------------------------
# UI
# -----------------------------
st.title("🎯 MBTI 캐릭터 & 맞춤 추천")
st.caption("MBTI별 잘생기고 예쁜 가상 캐릭터와 맞춤형 콘텐츠 추천")

# MBTI 선택
mbti = st.selectbox("당신의 MBTI를 선택하세요", sorted(MBTI_DATA.keys()))

if mbti:
    char = MBTI_DATA[mbti]

    # 캐릭터 프로필
    st.markdown(f"## {char['emoji']} {mbti} · {char['name']}")
    st.write(f"**분위기**: {char['vibe']}")
    st.write(f"**스타일**: {char['style']}")
    st.write(f"**외모 키워드**: {char['look']}")
    st.success(f"“{char['tagline']}”")

    st.markdown("---")

    # 추천 콘텐츠
    st.subheader(f"{char['emoji']} 맞춤 추천 콘텐츠")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### 🎬 영화")
        for movie in char["movie"]:
            st.write(f"- {movie}")

    with col2:
        st.markdown("### 🎵 음악")
        for music in char["music"]:
            st.write(f"- {music}")

    with col3:
        st.markdown("### 🌍 여행")
        for travel in char["travel"]:
            st.write(f"- {travel}")

st.caption("© 2025 MBTI Recommendation App")
