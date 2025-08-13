# app.py
import streamlit as st

# --------------------------------
# 데이터: MBTI별 추천 콘텐츠
# --------------------------------
recommendations = {
    "INTJ": {
        "movie": ["인셉션", "인터스텔라", "셜록 홈즈"],
        "music": ["Hans Zimmer - Time", "Ludovico Einaudi - Experience"],
        "travel": ["아이슬란드", "스위스 알프스", "교토"]
    },
    "ENFP": {
        "movie": ["라라랜드", "월터의 상상은 현실이 된다", "모아나"],
        "music": ["Coldplay - Adventure of a Lifetime", "Pharrell Williams - Happy"],
        "travel": ["발리", "바르셀로나", "뉴질랜드 퀸스타운"]
    },
    "ISTJ": {
        "movie": ["포레스트 검프", "캐스트 어웨이", "그린 마일"],
        "music": ["The Beatles - Hey Jude", "Simon & Garfunkel - The Sound of Silence"],
        "travel": ["스위스", "노르웨이 피오르드", "교토"]
    },
    "ENTP": {
        "movie": ["아이언맨", "캐치 미 이프 유 캔", "데드풀"],
        "music": ["Queen - Don't Stop Me Now", "Imagine Dragons - Believer"],
        "travel": ["라스베이거스", "뉴욕", "두바이"]
    },
    # 필요에 따라 더 추가 가능
}

# --------------------------------
# Streamlit UI
# --------------------------------
st.set_page_config(page_title="MBTI 추천 앱", page_icon="🎯", layout="centered")

st.title("🎯 MBTI 기반 영화/음악/여행 추천")
st.write("당신의 MBTI를 선택하면 맞춤형 콘텐츠를 추천해드립니다!")

# MBTI 선택
mbti_list = sorted(recommendations.keys())
selected_mbti = st.selectbox("당신의 MBTI를 선택하세요", mbti_list)

if selected_mbti:
    st.subheader(f"📌 {selected_mbti} 추천 콘텐츠")
    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("🎬 **영화 추천**")
        for movie in recommendations[selected_mbti]["movie"]:
            st.write(f"- {movie}")

    with col2:
        st.markdown("🎵 **음악 추천**")
        for music in recommendations[selected_mbti]["music"]:
            st.write(f"- {music}")

    with col3:
        st.markdown("🌍 **여행 추천**")
        for travel in recommendations[selected_mbti]["travel"]:
            st.write(f"- {travel}")

    st.markdown("---")
    st.success("추천이 마음에 드셨나요? 다른 MBTI도 선택해 보세요!")

# Footer
st.caption("© 2025 MBTI Recommendation App")
