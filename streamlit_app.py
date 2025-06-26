import streamlit as st
import numpy as np
import pickle
import random

# Load trained model
with open("diet_model.pkl", "rb") as f:
    model = pickle.load(f)

# ---------- 🎨 Custom Background Style ----------
st.markdown("""
    <style>
    body {
        background-color: #f2f9f2;
    }
    .stApp {
        background-color: #f2f9f2;
    }
    </style>
""", unsafe_allow_html=True)

# ---------- 🚀 Page Header ----------
st.set_page_config(page_title="Calorie Predictor", page_icon="🥗", layout="centered")

st.markdown("""
    <h1 style='text-align: center; color: #2E8B57;'>🥗 Smart Calorie Recommendation System</h1>
    <p style='text-align: center;'>Powered by Machine Learning • Optimized for You</p>
    <hr style='border: 1px solid #2E8B57;' />
""", unsafe_allow_html=True)

st.markdown("### 👤 Personal Information")

# ---------- 🧱 Input Layout ----------
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("📅 Age", min_value=1, max_value=120)
    height = st.number_input("📏 Height (cm)", min_value=100, max_value=250)
    activity_level = st.selectbox("🏃‍♂️ Activity Level", ['Sedentary', 'Lightly Active', 'Moderately Active', 'Very Active', 'Extra Active'])
    medical_conditions = st.selectbox("💊 Medical Conditions", ['None', 'Diabetes', 'Heart Issues'])
    diet_preference = st.selectbox("🥦 Diet Preference", ['Vegetarian', 'Non-Vegetarian', 'Vegan', 'Keto'])

with col2:
    gender = st.selectbox("👨‍🦰 Gender", ['Male', 'Female'])
    weight = st.number_input("⚖️ Weight (kg)", min_value=30, max_value=200)
    fitness_goal = st.selectbox("🎯 Fitness Goal", ['Weight Loss', 'Muscle Gain', 'Endurance', 'General Fitness'])
    preferred_activity = st.selectbox("🏋️ Preferred Activity", ['Walking', 'Running', 'Swimming', 'Gym'])
    bmi = st.number_input("🧮 BMI", min_value=10.0, max_value=50.0)

workout_duration = st.slider("⏱️ Workout Duration (mins/day)", 0, 120, value=45)

# ---------- 🔁 Feature Encoding ----------
gender_val = 1 if gender == 'Male' else 0
activity_val = activity_level.index(activity_level)
goal_val = fitness_goal.index(fitness_goal)
condition_val = medical_conditions.index(medical_conditions)
activity_pref_val = preferred_activity.index(preferred_activity)
diet_val = diet_preference.index(diet_preference)

# ---------- 🍱 Meal Plan Generator ----------
def get_random_meal_plan():
    meal_plans = [
        {
            "Breakfast": "Oats with banana and almond butter",
            "Lunch": "Grilled chicken salad with quinoa",
            "Snack": "Greek yogurt with berries",
            "Dinner": "Stir-fried tofu with vegetables and brown rice"
        },
        {
            "Breakfast": "Avocado toast with eggs",
            "Lunch": "Paneer wrap with whole wheat tortilla",
            "Snack": "Fruit smoothie",
            "Dinner": "Grilled salmon with steamed veggies"
        },
        {
            "Breakfast": "Poha with peanuts and veggies",
            "Lunch": "Mixed veg curry with brown rice",
            "Snack": "Boiled eggs or roasted chickpeas",
            "Dinner": "Chicken soup with whole grain toast"
        },
        {
            "Breakfast": "Smoothie bowl with granola and chia seeds",
            "Lunch": "Lentil dal with roti and cucumber salad",
            "Snack": "Apple slices with peanut butter",
            "Dinner": "Stuffed bell peppers with tofu and spinach"
        },
        {
            "Breakfast": "Idli with coconut chutney",
            "Lunch": "Rajma-chawal with salad",
            "Snack": "Buttermilk and banana",
            "Dinner": "Grilled fish with roasted sweet potato"
        },
        {
            "Breakfast": "Multigrain paratha with curd",
            "Lunch": "Quinoa upma with vegetables",
            "Snack": "Trail mix and lemon water",
            "Dinner": "Egg curry with brown rice"
        }
    ]
    return random.choice(meal_plans)

# ---------- 📊 Prediction ----------
st.markdown("### 📊 Prediction")
if st.button("🔍 Get My Recommended Calories"):
    input_features = np.array([[age, gender_val, height, weight,
                                activity_val, goal_val, condition_val,
                                activity_pref_val, diet_val, bmi, workout_duration]])
    
    prediction = model.predict(input_features)[0]
    st.success(f"🔥 **Estimated Daily Calorie Intake:** {round(prediction, 2)} kcal")

    meal_plan = get_random_meal_plan()
    st.markdown("### 🍽️ Sample Meal Plan Suggestion")

    with st.container():
        for meal, item in meal_plan.items():
            st.markdown(f"**{meal}:** {item}")
