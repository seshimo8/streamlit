import streamlit as st
import time

st.title('Streamlit 入門')

st.write('プレグレスバーの表示')
'start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!'


st.write('Intaractive Widgets')

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです')

expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ内容を書く')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ内容を書く')
expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせ内容を書く')



# option = st.text_input('あなたの趣味を教えてください')
# condition = st.slider('あなたの今の調子を教えてください。', 0, 100, 50)



# 'コンディション:', condition  
# 'あなたの趣味:', option,

# 'あなたの好きな数字は、', option, 'です'

# if st.checkbox('Show Image'):
#     img = Image.open('sample1.png')
#     st.image(img, caption='Yusuke Seshimo', use_column_width=True)


