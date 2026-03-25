import streamlit as st
import google.generativeai as genai
from PIL import Image

# إعداد واجهة التطبيق
st.set_page_config(page_title="Chaabi AI Analyzer", page_icon="🏺")

# دمج مفتاح الـ API الخاص بك
genai.configure(api_key="AIzaSyBm5MZaPc6Zu_FBZ_OXwE9SB_akN91AFq8")

st.title("🏺 Chaabi AI Analyzer")
st.subheader("تحليل السوق العالمي لمنتجات 'الشعبي'")
st.write("ارفع صورة منتجك التقليدي (نحاس، جلد، فخار) واحصل على استراتيجية بيع عالمية لعام 2026.")

uploaded_file = st.file_uploader("اختر صورة المنتج...", type=["jpg", "jpeg", "png", "webp"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='معاينة المنتج', use_container_width=True)
    
    if st.button("🚀 تحليل 'مفعول' المنتج في السوق العالمي"):
        with st.spinner('جاري التحليل العميق...'):
            try:
                model = genai.GenerativeModel('gemini-1.5-flash')
                prompt = """
                بصفتك خبير تجارة إلكترونية عالمي، حلل هذه الصورة لمنتج مغربي تقليدي:
                1. حدد الخامة وجودة الصنع (Craftsmanship).
                2. أعطِ 5 كلمات مفتاحية ذهبية (Etsy Tags) بالإنجليزية.
                3. حلل الطلب العالمي (Market Trend) لهذا النوع في أبريل 2026.
                4. اقترح سعراً تنافسياً بالدولار ($) للبيع في أمريكا وأوروبا.
                5. اكتب وصفاً تسويقياً قصيراً ومؤثراً بالإنجليزية.
                """
                response = model.generate_content([prompt, image])
                st.markdown("---")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"حدث خطأ: {e}")

st.markdown("---")
st.caption("تم التطوير بواسطة Chaabi Souk AI - لتمكين الحرفيين المغاربة.")