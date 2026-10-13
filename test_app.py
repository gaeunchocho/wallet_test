import streamlit as st

st.set_page_config(page_title="내 지갑 속 캐릭터는?", page_icon="👛", layout="centered")

TYPES = {
    "planner": {"emoji": "🐿️", "name": "계획형 다람쥐", "tag": "차곡차곡, 계획대로!", "description": "예산과 목표를 세우고 차근차근 소비하는 편이에요. 지출을 관리하는 습관이 강점이에요.", "watch": "계획을 너무 엄격하게 지키다가 작은 즐거움까지 미루지는 않는지 살펴보세요.", "missions": ["이번 주에 쓸 수 있는 작은 즐거움 예산 정하기", "이번 달 저축 목표와 실제 저축액 비교하기", "최근 지출 중 만족도가 높았던 소비 3개 적기"]},
    "impulse": {"emoji": "🐱", "name": "즉흥형 고양이", "tag": "마음에 들면 일단 담아!", "description": "새로운 물건이나 순간의 즐거움에 마음이 움직이는 편이에요. 취향이 뚜렷하고 새로운 경험에 열려 있어요.", "watch": "작은 결제가 쌓이면 예상보다 큰 지출이 될 수 있어요.", "missions": ["예정에 없던 구매는 장바구니에 넣고 24시간 기다리기", "이번 주 자유롭게 쓸 금액을 미리 정하기", "최근 충동구매 한 건의 만족도를 5점 만점으로 기록하기"]},
    "bargain": {"emoji": "🦊", "name": "할인형 여우", "tag": "같은 물건도 똑똑하게!", "description": "가격 비교와 할인 혜택을 챙기는 편이에요. 필요한 물건을 합리적인 가격에 찾는 능력이 강점이에요.", "watch": "할인율보다 정말 필요한 물건인지 먼저 확인해 보세요.", "missions": ["할인 상품 결제 전에 원래 구매할 계획이 있었는지 확인하기", "무료배송 금액을 맞추려고 추가한 물건 한 개 빼기", "쿠폰 알림 중 자주 충동구매로 이어지는 알림 끄기"]},
    "experience": {"emoji": "🐬", "name": "경험형 돌고래", "tag": "물건보다 추억이 좋아!", "description": "여행, 모임, 취미처럼 경험에 돈을 쓰는 편이에요. 자신에게 의미 있는 즐거움을 찾는 것이 강점이에요.", "watch": "모임이나 취미 비용이 겹치는 달에는 전체 지출을 확인해 보세요.", "missions": ["이번 달 모임·취미 예산을 따로 정하기", "돈이 적게 드는 즐거운 활동 하나 찾아 실행하기", "잘 이용하지 않는 취미 구독 한 개 확인하기"]},
}

# 모든 문항의 선택지는 서로 다른 네 유형에 한 점씩 부여합니다.
QUESTIONS = [
    ("예상치 못한 용돈이 생겼어요. 가장 먼저 할 일은?", [("저축 목표에 보탠다", "planner"), ("평소 눈여겨본 물건을 바로 산다", "impulse"), ("할인 중인 필요한 물건을 찾는다", "bargain"), ("여행이나 친구와의 약속을 잡는다", "experience")]),
    ("마음에 드는 물건을 발견했을 때 나는?", [("예산과 구매 목록을 확인한다", "planner"), ("지금 끌리면 구매한다", "impulse"), ("다른 판매처의 가격과 쿠폰을 비교한다", "bargain"), ("이 돈으로 할 수 있는 경험을 떠올린다", "experience")]),
    ("주말에 돈을 쓴다면 가장 가까운 모습은?", [("정해 둔 생활비 안에서 쓴다", "planner"), ("그날 기분에 따라 쇼핑한다", "impulse"), ("특가나 할인 행사를 활용한다", "bargain"), ("맛집, 공연, 취미 활동을 즐긴다", "experience")]),
    ("월말 카드 내역을 보면 어떤 생각이 드나요?", [("예산과 실제 지출을 비교해야겠다", "planner"), ("언제 이렇게 많이 썼지?", "impulse"), ("혜택을 잘 챙겼는지 확인해야겠다", "bargain"), ("이번 달도 즐거운 추억이 많았네", "experience")]),
    ("무료배송까지 1만 원이 부족하다면?", [("총비용을 보고 필요한 것만 결제한다", "planner"), ("눈에 들어오는 물건을 하나 더 담는다", "impulse"), ("필요한 소모품으로 배송비를 아낀다", "bargain"), ("친구와 함께 주문할 수 있는지 물어본다", "experience")]),
    ("큰 지출을 앞두고 나는?", [("목표 금액을 정하고 미리 모은다", "planner"), ("마음이 확실하면 먼저 구매를 결정한다", "impulse"), ("가격이 내려가는 시점이나 혜택을 찾는다", "bargain"), ("내게 얼마나 의미 있는 경험인지 생각한다", "experience")]),
    ("가장 만족스러운 소비는?", [("계획한 물건을 예산 안에서 샀을 때", "planner"), ("마음에 쏙 드는 물건을 발견했을 때", "impulse"), ("필요한 물건을 저렴하게 샀을 때", "bargain"), ("좋은 사람들과 특별한 시간을 보냈을 때", "experience")]),
    ("소비 습관을 하나 바꾼다면?", [("예산을 더 꾸준히 기록하고 싶다", "planner"), ("즉흥적인 구매를 조금 줄이고 싶다", "impulse"), ("할인 때문에 사는 물건을 줄이고 싶다", "bargain"), ("경험에 쓰는 비용을 잘 배분하고 싶다", "experience")]),
]


def calculate_scores(answers):
    scores = {key: 0 for key in TYPES}
    for answer, (_, options) in zip(answers, QUESTIONS):
        scores[dict(options)[answer]] += 1
    return scores


def restart():
    st.session_state.pop("result", None)
    for index in range(len(QUESTIONS)):
        st.session_state.pop(f"q_{index}", None)


st.markdown("""
<style>
.stApp {background: #fffaf3;}
.block-container {max-width: 760px; padding-top: 2.5rem;}
h1, h2, h3 {color: #332b25;}
div.stButton > button, div.stFormSubmitButton > button {border-radius: 14px;}
.hero {text-align:center; padding:20px 0 26px;}
.hero p {color:#74695f; font-size:17px;}
.result-card {background:#fff; border:1px solid #f0dfc5; border-radius:24px; padding:28px; text-align:center; margin-bottom:24px;}
.character {font-size:80px; line-height:1.2;}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="hero"><h1>👛 내 지갑 속 캐릭터는?</h1><p>8개의 질문으로 알아보는 나의 소비 습관</p></div>', unsafe_allow_html=True)

if "result" not in st.session_state:
    st.info("약 2분 소요 · 가장 나다운 답을 하나씩 골라주세요.")
    with st.form("character_test"):
        answers = []
        for index, (question, options) in enumerate(QUESTIONS):
            st.markdown(f"### {index + 1}. {question}")
            answers.append(st.radio("답변 선택", [label for label, _ in options], index=None, key=f"q_{index}", label_visibility="collapsed"))
        submitted = st.form_submit_button("내 소비 캐릭터 확인하기 ✨", type="primary", use_container_width=True)
    if submitted:
        missing = [str(i + 1) for i, answer in enumerate(answers) if answer is None]
        if missing:
            st.warning(f"아직 답하지 않은 문항이 있어요: {', '.join(missing)}번")
        else:
            st.session_state.result = calculate_scores(answers)
            st.rerun()
else:
    scores = st.session_state.result
    highest = max(scores.values())
    winners = [key for key, score in scores.items() if score == highest]
    if len(winners) == 1:
        character = TYPES[winners[0]]
        st.markdown(f'<div class="result-card"><div class="character">{character["emoji"]}</div><h2>{character["name"]}</h2><p>{character["tag"]}</p></div>', unsafe_allow_html=True)
        st.write(character["description"])
        st.markdown("#### 🌱 살펴볼 습관")
        st.write(character["watch"])
    else:
        st.markdown('<div class="result-card"><div class="character">🌈</div><h2>복합형 소비 캐릭터</h2><p>여러 소비 성향이 함께 나타났어요!</p></div>', unsafe_allow_html=True)
        st.caption("최고 점수가 같으면 특정 유형을 우선하지 않고 함께 보여드려요.")
        for key in winners:
            character = TYPES[key]
            st.markdown(f'#### {character["emoji"]} {character["name"]}')
            st.write(character["description"])
            st.write(f'살펴볼 습관: {character["watch"]}')

    st.markdown("#### 📊 내 답변의 성향 비중")
    for key, character in TYPES.items():
        score = scores[key]
        st.write(f'{character["emoji"]} {character["name"]} · {score}/8개 ({score / 8:.0%})')
        st.progress(score / 8)
    st.caption("비중은 해당 유형에 연결된 답변의 비율이며, 심리검사 점수나 진단 확률이 아니에요.")

    st.markdown("#### 🎯 이번 주 절약 미션")
    missions = TYPES[winners[0]]["missions"] if len(winners) == 1 else [TYPES[key]["missions"][0] for key in winners]
    for index, mission in enumerate(missions):
        st.checkbox(mission, key=f"mission_{'_'.join(winners)}_{index}")

    with st.expander("결과 텍스트 복사하기"):
        names = " + ".join(TYPES[key]["name"] for key in winners)
        st.code(f"내 지갑 속 캐릭터는 {names}!\n이번 주 미션: {missions[0]}", language=None)
    st.button("다시 테스트하기 🔄", on_click=restart, use_container_width=True)

st.divider()
st.caption("재미와 자기 점검을 위한 자체 제작 테스트입니다. 전문 심리검사나 금융상품 추천이 아닙니다. 답변을 별도 파일이나 데이터베이스에 저장하지 않습니다.")
