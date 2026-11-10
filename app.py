
import streamlit as st
import ollama

# 페이지 설정
st.set_page_config(
    page_title="Neuron Chat AI",
    page_icon="🤖",
    layout="centered"
)

# 제목
st.title("🤖 Neuron Chat AI")
st.caption("Powered by Qwen2.5 3B | Local Open Source LLM")

# 대화 기록 초기화
if "messages" not in st.session_state:
    st.session_state.messages = []

# 대화 초기화 버튼
if st.button("🗑️ 대화 기록 초기화"):
    st.session_state.messages = []
    st.rerun()

# 이전 대화 표시
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 질문 입력
if prompt := st.chat_input("AI에게 질문해 보세요..."):

    # 사용자 질문 저장 및 표시
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # AI 답변 생성
    with st.chat_message("assistant"):
        with st.spinner("AI가 답변을 생성하고 있습니다..."):
            try:
                response = ollama.chat(
                    model="qwen2.5:3b",
                    messages=st.session_state.messages
                )

                answer = response["message"]["content"]
                st.markdown(answer)

                st.session_state.messages.append(
                    {"role": "assistant", "content": answer}
                )

            except Exception as e:
                st.error(f"오류가 발생했습니다: {e}")
