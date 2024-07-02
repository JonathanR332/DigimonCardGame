import streamlit as st
import requests

api_key = "03ad47f37fee6eb17ddbadf089f9df1069e28b61c4040cf5faab54cf30be9096" #my api key



def fetch_cards_by_name_and_color(name, color): # Fetching data from API based on name and color
    url = "https://digimoncard.io/api-public/search.php"
    params = {
        "n": name,
        "color": color
    }
    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Main 
def main():
    st.title("Digimon Card Search")

  
    card_name = st.text_input("Enter Card Name")   # asking users for their search terms.
    card_color = st.selectbox("Select Card Color", ["", "Black", "Blue", "Colorless", "Green", "Purple", "Red", "White", "Yellow"]) #digimon is a colorbased card game, many cards are printed in different colors.

    
    if st.button("Search"): # search button
        if card_name and card_color:
           
            cards = fetch_cards_by_name_and_color(card_name, card_color) # grabbing data

            
            if cards:     # displays that data
                st.subheader("Search Results")
                for card in cards:
                    st.markdown(f"## {card.get('name', 'N/A')} ({card.get('id', 'N/A')})")

                   
                    if 'image_url' in card and card['image_url']:  # API currently does not support images, i have this here in case that changes.
                        try:
                            response = requests.get(card['image_url'])
                            if response.status_code == 200:
                                st.image(card['image_url'], caption="Card Image", use_column_width=True)
                            else:
                                st.warning(f"Failed to load image: {response.status_code}")
                        except Exception as e:
                            st.error(f"Error loading image: {e}")
                    
                    st.write(f"**Type:** {card.get('type', 'N/A')}") # card type it ask what type of playable card it is, digimon, tamer, option etc
                    st.write(f"**Level:** {card.get('level', 'N/A')}") # digimon start generally at level 2 and go upwards.
                    st.write(f"**Play Cost:** {card.get('play_cost', 'N/A')}") # memory counter, the bigger stronger card cost more memory, concept best explained by knowing how to play.
                    st.write(f"**Evolution Cost:** {card.get('evolution_cost', 'N/A')}") # evolution and play cost are similar but play cost rewards players for their combos and stacking.
                    st.write(f"**Evolution Color:** {card.get('evolution_color', 'N/A')}") # color is very important as blue cards can only work with blue cards and etc.
                    st.write(f"**DP (Digimon Power):** {card.get('dp', 'N/A')}") # dp is how digimons fight, the higher dp will always win.
                    st.write(f"**Attribute:** {card.get('attribute', 'N/A')}") # specific attributes that can be used to search for cards and other effects.
                    st.write(f"**Rarity:** {card.get('rarity', 'N/A')}") # cards need rarities :D
                    st.write(f"**Main Effect:**") # displays main effects.
                    st.write(card.get('main_effect', 'N/A'))
                    st.write("---")
            else:
                st.write("No cards found matching the search criteria.") #error meesage
        else:
            st.warning("Please enter both a card name and select a color.")

if __name__ == "__main__":
    main()
