import streamlit as st

st.subheader('自己紹介')
st.text('Pythonに関する情報をYoutube上で発信しているPython Vtuber さぷーです\n'
        'よければチャンネル登録よろしくお願いします!')

code = '''
    import streamlit as st

    st.title('サプーアプリ')
    '''
st.code(code,language='python')