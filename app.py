

import streamlit as st

# Set page configuration
st.set_page_config(page_title="MiniDeng Animal Charity", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f8ff;
            color: #333;
            text-align: center;
            padding: 20px;
        }
        .title {
            color: #5b9aa0;
            font-size: 3em;
            margin-top: 0.5em;
            margin-bottom: 0.5em;
        }
        .section {
            background-color: #e8f5e9;
            padding: 15px;
            margin: 15px 0;
            border-radius: 10px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        }
        .highlight-links {
            display: flex;
            justify-content: center;
            gap: 20px;
            margin-top: 10px;
        }
        .highlight-links a {
            color: #5b9aa0;
            font-weight: bold;
            text-decoration: none;
            display: flex;
            align-items: center;
        }
        .highlight-links img {
            width: 24px;
            height: 24px;
            margin-right: 8px;
        }
    </style>
""", unsafe_allow_html=True)

# Title and centered image
st.markdown('<h1 class="title">MiniDeng Animal Charity</h1>', unsafe_allow_html=True)
left_co, cen_co, last_co = st.columns(3)
with cen_co:
    st.image("minideng.jpeg", width=250)

# Right column with the buy button
# Larger button below the image
st.markdown(
    """
    <div style="text-align: center;">
        <a href="https://dexscreener.com/solana/g2gcecprvaqi6ex53egnmxig3jmpq2q7coizz7p8ebxy" target="_blank">
            <button style="
                background-color: #4CAF50; 
                color: white; 
                padding: 15px 30px; 
                font-size: 18px; 
                border: none; 
                border-radius: 8px;
                cursor: pointer;
                width: 180px;
                margin-top: 15px;
            ">
                Buy Here
            </button>
        </a>
    </div>
    """,
    unsafe_allow_html=True
)
# Highlighted Links Section
st.markdown("""
<style>
    .highlight-links {
        display: flex;
        flex-direction: row;
        justify-content: center;
        gap: 20px;
        margin-top: 10px;
        flex-wrap: wrap;
    }
    .highlight-links a, .highlight-links span {
        display: flex;
        align-items: center;
        flex-direction: column;
        text-align: center;
        width: 100px;
        margin: 5px;
    }
    .highlight-links img {
        width: 24px;
        height: 24px;
        margin-bottom: 5px;
    }
</style>
<div class="highlight-links">
    <a href="https://x.com/minideng044?s=11&t=H90QoX9jMleOIE04I4tVZA" target="_blank">
        <img src="https://img.icons8.com/ios-filled/50/000000/twitter.png" alt="Twitter"> Twitter
    </a>
    <span>
        <img src="https://img.icons8.com/ios-filled/50/000000/key.png" alt="Contract Address"> Contract Address:<br> G2gceCPRVAqi6ex53EGNmxiG3jmpQ2Q7coizz7p8EBxY
    </span>
    <a href="https://dexscreener.com/solana/g2gcecprvaqi6ex53egnmxig3jmpq2q7coizz7p8ebxy" target="_blank">
        <img src="https://img.icons8.com/ios-filled/50/000000/line-chart.png" alt="DEX View"> DEX Screener
    </a>
</div>
""", unsafe_allow_html=True)



# Mission Section
st.markdown('<div class="section">', unsafe_allow_html=True)
st.subheader("Our Mission")
st.write("MiniDeng is here to protect and care for small hippos and other vulnerable animals worldwide. We aim to raise awareness, promote conservation, and support local and international efforts to preserve natural habitats. By engaging communities and educating the public, we strive to create a future where all wildlife is protected and valued.")
st.markdown('</div>', unsafe_allow_html=True)

# Additional Sections
st.markdown('<div class="section">', unsafe_allow_html=True)
st.subheader("Our Vision")
st.write("We envision a world where hippos and other wildlife thrive in safe and secure habitats, free from human-induced threats. Our vision includes partnering with global conservation groups, supporting habitat restoration, and inspiring a new generation of wildlife advocates. Together, we can create lasting impacts that benefit both the environment and the creatures within it.")
st.markdown('</div>', unsafe_allow_html=True)



st.markdown('<div class="section" style="text-align: left;">', unsafe_allow_html=True)
st.subheader("How to Buy MiniDeng ($MINIDENG)")

# Step 1
st.markdown('<div style="text-align: left;"><strong>Step 1: Set Up a Wallet</strong></div>', unsafe_allow_html=True)
st.write("Head to [phantom.app](https://phantom.app) and follow the instructions to create an account using the Phantom app or browser extension.")

# Step 2
st.markdown('<div style="text-align: left;"><strong>Step 2: Acquire $SOL</strong></div>', unsafe_allow_html=True)
st.write("In the Phantom app, tap **BUY** to purchase Solana (\$SOL) directly, or transfer \$SOL from a cryptocurrency exchange to your Phantom wallet.")

# Step 3
st.markdown('<div style="text-align: left;"><strong>Step 3: Swap $SOL for $MINIDENG</strong></div>', unsafe_allow_html=True)
st.write("Select **SWAP** in your Phantom wallet, paste the **\$MINIDENG** token address **G2gceCPRVAqi6ex53EGNmxiG3jmpQ2Q7coizz7p8EBxY**, and exchange your **\$SOL** for **\$MINIDENG**.")

# Step 4
st.markdown('<div style="text-align: left;"><strong>Step 4: Join the MiniDeng Community</strong></div>', unsafe_allow_html=True)
st.write("Congratulations on joining the MiniDeng family! For added convenience, **\$MINIDENG** will be available for purchase via Apple Pay on Moonshot soon.")

# Close the main section div
st.markdown('</div>', unsafe_allow_html=True)






