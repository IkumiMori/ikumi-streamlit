
import streamlit as st


st.title('Streamlit 超入門')
st.write('Interactive Widgets')



#st.table(df.style.highlight_max(axis=0))

#"""
# 章
## 節
### 項

#```python
import streamlit as st

#```
#"""



#st.line_chart(df)
#st.area_chart(df)
#st.bar_chart(df)
#st.map(df)


#if st.checkbox('Show Image'):
#    img=Image.open('denki.png')
#   st.image(img,caption='mori',use_column_width=True)

#option=st.selectbox(
 #   'あなたが好きな数字を教えてください。',
  #  list(range(1,11))
#)

#'あなたの好きな数字は，',option,'です。'

left_column,right_column=st.beta_columns(2)
button=left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです。')




option=st.text_input('あなたの趣味を教えてください')
condition=st.slider('あなたの今の調子は？',0,100,50)

'あなたの趣味:',option,'です。'
'コンディション:',condition


expander=st.beta_expander('問い合わせ')
expander.write('問い合わせ内容を書く')


