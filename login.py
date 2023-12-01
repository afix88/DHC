import streamlit as st

def main():
    # Menambahkan CSS dan latar belakang
    page_bg_img = '''
    <style>
    body {
        background-image: url("https://github.com/afix88/DHC/blob/main/Background.jpg");
        background-size: cover;
        margin: 0;
        padding: 0;
    }
    </style>
    '''
    st.set_page_config(page_title="DHC&DPO!!!",
                   page_icon=":bar_chart:", layout="wide")
    st.markdown(page_bg_img, unsafe_allow_html=True)

    st.title("DHC & DPO ")

    if "login_status" not in st.session_state:
        st.session_state.login_status = False

    if not st.session_state.login_status:
        # Input username
        username = st.text_input("Username")

        # Input password
        password = st.text_input("Password", type="password")

        # Tombol Login
        if st.button("Login"):
            if username == "afix" and password == "salamsahabat":
                st.session_state.login_status = True
                st.success("Login berhasil!")
            else:
                st.error("Login gagal. Periksa kembali username dan password.")
    else:
        # Embed Power BI setelah login berhasil
        power_bi_url = "https://app.powerbi.com/view?r=eyJrIjoiOWQ1YjYzNTItNjgyOC00YzdmLTllOGEtZjVhNWZkOWZlMTQyIiwidCI6ImM4NThlYTJiLWFhNjUtNDg0MC05ZWVlLWU5MTM0OWE2OTY5ZSIsImMiOjEwfQ%3D%3D"
        embed_code = f'<iframe id="myIframe" src="{power_bi_url}" frameborder="0" allowfullscreen="true" style="position:fixed; top:0; left:0; bottom:0; right:0; width:100%; height:100%; border:none; margin:0; padding:0; overflow:hidden; z-index:999999;"></iframe>'
        st.markdown(embed_code, unsafe_allow_html=True)

        # Menambahkan JavaScript untuk memanggil fungsi postMessage saat laman dimuat
        st.markdown("""
        <script>
        document.addEventListener('DOMContentLoaded', function() {
            var iframe = document.getElementById('myIframe');
            iframe.onload = function() {
                iframe.contentWindow.postMessage('fullscreen', '*');
            };
        });
        </script>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
