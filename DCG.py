import streamlit as st
import requests

DIGIMON_API_KEY = "03ad47f37fee6eb17ddbadf089f9df1069e28b61c4040cf5faab54cf30be9096"


# Function to fetch data from API based on name and color
def fetch_cards_by_name_and_color(name, color):
    url = "https://digimoncard.io/api-public/search.php"
    params = {
        "n": name,
        "color": color
    }
    headers = {
        "Authorization": f"Bearer {DIGIMON_API_KEY}"
    }
    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Main Streamlit app
def main():
    st.title("Digimon Card Search")

    # Input fields
    card_name = st.text_input("Enter Card Name")
    card_color = st.selectbox("Select Card Color", ["", "Black", "Blue", "Colorless", "Green", "Purple", "Red", "White", "Yellow"])

    # Button to trigger search
    if st.button("Search"):
        if card_name and card_color:
            # Fetch data from API
            cards = fetch_cards_by_name_and_color(card_name, card_color)

            # Display results
            if cards:
                st.subheader("Search Results")
                for card in cards:
                    st.markdown(f"## {card.get('name', 'N/A')} ({card.get('id', 'N/A')})")

                    # Display image if available
                    if 'image_url' in card and card['image_url']:
                        try:
                            st.image(card['image_url'], caption="Card Image", use_column_width=True)
                        except Exception as e:
                            st.error(f"Error loading image: {e}")
                    
                    st.write(f"**Type:** {card.get('type', 'N/A')}")
                    st.write(f"**Level:** {card.get('level', 'N/A')}")
                    st.write(f"**Play Cost:** {card.get('play_cost', 'N/A')}")
                    st.write(f"**Evolution Cost:** {card.get('evolution_cost', 'N/A')}")
                    st.write(f"**Evolution Color:** {card.get('evolution_color', 'N/A')}")
                    st.write(f"**DP (Digimon Power):** {card.get('dp', 'N/A')}")
                    st.write(f"**Attribute:** {card.get('attribute', 'N/A')}")
                    st.write(f"**Rarity:** {card.get('rarity', 'N/A')}")
                    st.write(f"**Main Effect:**")
                    st.write(card.get('main_effect', 'N/A'))
                    st.write("---")
            else:
                st.write("No cards found matching the search criteria.")
        else:
            st.warning("Please enter both a card name and select a color.")

if __name__ == "__main__":
    main()