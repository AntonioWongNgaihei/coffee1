import streamlit as st

# Caffeine content per cup for each coffee type in milligrams
coffee_caffeine = {
    'brewed coffee': 95,
    'espresso': 63,
    'instant coffee': 70
}

st.title("Coffee Caffeine Calculator")
st.write("Enter the number of cups for each coffee type:")

# Input fields for each coffee type
brewed_cups = st.number_input("Brewed coffee (cups)", min_value=0, step=1)
espresso_cups = st.number_input("Espresso (cups)", min_value=0, step=1)
instant_cups = st.number_input("Instant coffee (cups)", min_value=0, step=1)

# Ask the user which coffee they prefer
preferred_coffee = st.selectbox("Which coffee do you prefer?",
                                ['brewed coffee', 'espresso', 'instant coffee'])

# Calculate total caffeine intake
total_caffeine = (brewed_cups * coffee_caffeine['brewed coffee'] +
                  espresso_cups * coffee_caffeine['espresso'] +
                  instant_cups * coffee_caffeine['instant coffee'])

# Display the total caffeine intake
st.write(f"Your total caffeine intake today is: {total_caffeine} mg.")

# Warn if caffeine intake exceeds 400 mg
if total_caffeine > 400:
    st.warning("Warning: You have exceeded the recommended caffeine intake of 400 mg!")

# Suggest caffeine intake for the next day
def suggest_next_day(caffeine_today, preferred_coffee):
    # Target caffeine intake for the next day (90% of today's intake)
    target_caffeine = caffeine_today * 0.9
    remaining_caffeine = target_caffeine

    brewed_suggest = 0
    espresso_suggest = 0
    instant_suggest = 0

    if preferred_coffee == 'brewed coffee':
        brewed_suggest = remaining_caffeine // coffee_caffeine['brewed coffee']
        remaining_caffeine %= coffee_caffeine['brewed coffee']
    elif preferred_coffee == 'espresso':
        espresso_suggest = remaining_caffeine // coffee_caffeine['espresso']
        remaining_caffeine %= coffee_caffeine['espresso']
    elif preferred_coffee == 'instant coffee':
        instant_suggest = remaining_caffeine // coffee_caffeine['instant coffee']
        remaining_caffeine %= coffee_caffeine['instant coffee']

    if brewed_suggest == 0:
        brewed_suggest = remaining_caffeine // coffee_caffeine['brewed coffee']
    if espresso_suggest == 0:
        espresso_suggest = remaining_caffeine // coffee_caffeine['espresso']
    if instant_suggest == 0:
        instant_suggest = remaining_caffeine // coffee_caffeine['instant coffee']

    return int(brewed_suggest), int(espresso_suggest), int(instant_suggest)

# Calculate suggestions for next day
brewed_next, espresso_next, instant_next = suggest_next_day(total_caffeine, preferred_coffee)

# Display suggestions
st.subheader("Suggested coffee intake for tomorrow:")
st.write(f"- {brewed_next} cup(s) of brewed coffee")
st.write(f"- {espresso_next} cup(s) of espresso")
st.write(f"- {instant_next} cup(s) of instant coffee")
