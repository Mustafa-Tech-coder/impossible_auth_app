import streamlit as st
st.set_page_config(page_title="impossible system", page_icon=" lock", layout="wide")
st.title("نظام المصادقة")
st.header("بوابة الدخول")
st.caption("يرجى إدخال بياناتك لتسجيل الدخول")
st.divider()
mode=st.radio( "اختيار العملية", ["تسجيل الدخول", "إنشاء حساب"])
st.markdown("**---**")
if mode=="تسجيل الدخول":
    st.subheader("تسجيل الدخول")
    col1,col2=st.columns(2)
    with col1:
        username=st.text_input("اسم المستخدم")
        pin=st.text_input("كلمة المرور",type="password")
    with col2:
        auth_code=st.text_input("رمز المصادقة")
        secret_key=st.text_input("المفتاح السري",type="password")
if st.button("تسجيل الدخول"):
    if not username and not auth_code :
         st.error("يرجى إدخال اسم المستخدم ورمز المصادقة.")
    elif pin %2==0 :
         st.error("كلمة المرور يجب أن تكون رقم فردي.")
    elif secret_key < 1000 or secret_key > 9999:
         st.error("المفتاح السري غير صحيح.")    
    else:
         st.success("تم تسجيل الدخول بنجاح!")
if mode=="إنشاء حساب":
    st.subheader("إنشاء حساب جديد")
    col1,col2=st.columns(2)
    with col1:
        new_username=st.text_input("اسم المستخدم الجديد")
        new_pin=st.text_input("كلمة المرور الجديدة",type="password")
    with col2:
        new_auth_code=st.text_input("رمز المصادقة الجديد")
        new_secret_key=st.text_input("المفتاح السري الجديد",type="password")
if st.button("إنشاء حساب"):
    if not new_username and not new_auth_code:
         st.error("يرجى إدخال اسم المستخدم ورمز المصادقة.")
    elif new_pin %2==0 :
         st.error("كلمة المرور يجب أن تكون رقم فردي.")
    elif new_secret_key < 1000 or new_secret_key > 9999:
         st.error("المفتاح السري غير صحيح.")    
    else:
         st.success("تم إنشاء الحساب بنجاح!")

