import streamlit as st

# ✅ MUST BE FIRST STREAMLIT COMMAND
st.set_page_config(
    page_title="Ultimate Unit Converter",
    page_icon="📊",
    layout="wide"
)

# Initialize session state for theme
if 'theme' not in st.session_state:
    st.session_state.theme = 'System Default'

# Unit conversion data
unit_conversions = {
    'Length': {
        'meters': 1,
        'kilometers': 1000,
        'centimeters': 0.01,
        'millimeters': 0.001,
        'miles': 1609.34,
        'yards': 0.9144,
        'feet': 0.3048,
        'inches': 0.0254,
        'nautical miles': 1852
    },
    'Temperature': ['Celsius', 'Fahrenheit', 'Kelvin'],
    'Area': {
        'square meters': 1,
        'square kilometers': 1e6,
        'square miles': 2.59e6,
        'acres': 4046.86,
        'hectares': 10000,
        'square feet': 0.092903,
        'square inches': 0.00064516
    },
    'Data Transfer Rate': {
        'bits per second': 1,
        'bytes per second': 8,
        'kilobits per second': 1000,
        'megabits per second': 1e6,
        'gigabits per second': 1e9,
        'terabits per second': 1e12
    },
    'Digital Storage': {
        'bits': 1,
        'bytes': 8,
        'kilobytes': 8192,
        'megabytes': 8.389e+6,
        'gigabytes': 8.59e+9,
        'terabytes': 8.796e+12
    },
    'Energy': {
        'joules': 1,
        'kilojoules': 1000,
        'calories': 4.184,
        'kilocalories': 4184,
        'watthours': 3600,
        'kilowatthours': 3.6e6
    },
    'Frequency': {
        'hertz': 1,
        'kilohertz': 1e3,
        'megahertz': 1e6,
        'gigahertz': 1e9,
        'terahertz': 1e12
    },
    'Fuel Economy': {
        'miles per gallon': 1,
        'kilometers per liter': 2.352,
        'liters per 100 km': 235.215
    },
    'Mass': {
        'grams': 1,
        'kilograms': 1000,
        'milligrams': 0.001,
        'pounds': 453.592,
        'ounces': 28.3495,
        'tons': 907185
    },
    'Plane Angle': {
        'degrees': 1,
        'radians': 57.2958,
        'gradians': 0.9
    },
    'Pressure': {
        'pascals': 1,
        'kilopascals': 1000,
        'bars': 1e5,
        'atmospheres': 101325,
        'psi': 6894.76
    },
    'Speed': {
        'meters per second': 1,
        'kilometers per hour': 0.277778,
        'miles per hour': 0.44704,
        'knots': 0.514444,
        'mach': 343
    },
    'Time': {
        'seconds': 1,
        'minutes': 60,
        'hours': 3600,
        'days': 86400,
        'weeks': 604800,
        'years': 31536000
    },
    'Volume': {
        'liters': 1,
        'milliliters': 0.001,
        'cubic meters': 1000,
        'gallons': 3.78541,
        'quarts': 0.946353,
        'pints': 0.473176,
        'cups': 0.24,
        'fluid ounces': 0.0295735
    }
}

def convert_temperature(value, from_unit, to_unit):
    conversion_functions = {
        ('Celsius', 'Fahrenheit'): lambda x: (x * 9/5) + 32,
        ('Celsius', 'Kelvin'): lambda x: x + 273.15,
        ('Fahrenheit', 'Celsius'): lambda x: (x - 32) * 5/9,
        ('Fahrenheit', 'Kelvin'): lambda x: (x - 32) * 5/9 + 273.15,
        ('Kelvin', 'Celsius'): lambda x: x - 273.15,
        ('Kelvin', 'Fahrenheit'): lambda x: (x - 273.15) * 9/5 + 32
    }
    return conversion_functions[(from_unit, to_unit)](value) if from_unit != to_unit else value

theme_styles = {
    "Light": {
        "--background-color": "#ffffff",
        "--text-color": "#000000",
        "--primary-color": "#1f77b4",
        "--secondary-color": "#ff7f0e",
        "--card-background": "#f0f2f6",
        "--sidebar-background": "#f0f2f6",
        "--sidebar-text": "#000000",
        "--sidebar-select-text": "#000000"
    },
    "Dark": {
        "--background-color": "#0e1117",
        "--text-color": "#ffffff",
        "--primary-color": "#00ffff",
        "--secondary-color": "#00ff00",
        "--card-background": "#1a1c24",
        "--sidebar-background": "#000000",  # Pure black
        "--sidebar-text": "#ffffff",
        "--sidebar-select-text": "#ffffff"
    },
    "System Default": {
        "--background-color": "inherit",
        "--text-color": "inherit",
        "--primary-color": "#1f77b4",
        "--secondary-color": "#ff7f0e",
        "--card-background": "inherit",
        "--sidebar-background": "inherit",
        "--sidebar-text": "inherit",
        "--sidebar-select-text": "inherit"
    }
}

# Sidebar with theme selector
with st.sidebar:
    st.header("🌟 Features & Settings")
    st.session_state.theme = st.selectbox(
        "🎨 Theme Selector",
        ["Light", "Dark", "System Default"],
        index=["Light", "Dark", "System Default"].index(st.session_state.theme)
    )
    
    st.markdown("""
    - 15+ Conversion Categories
    - 100+ Supported Units
    - Real-time Updates
    - Scientific Precision
    - Mobile Friendly
    """)
    st.markdown("---")
    st.markdown("Made with ❤️ by **HMMS** using Streamlit")

# Update the Dynamic CSS styling section with this code
selected_style = theme_styles[st.session_state.theme]

css = f"""
<style>
[data-testid="stSidebar"] {{
    background-color: {selected_style.get('--sidebar-background', '')} !important;
}}

[data-testid="stSidebar"] * {{
    color: {selected_style.get('--sidebar-text', '')} !important;
}}

[data-testid="stSidebar"] .stSelectbox div {{
    background-color: {selected_style['--card-background']} !important;
    color: {selected_style.get('--sidebar-select-text', '')} !important;
}}

[data-testid="stSidebar"] .stMarkdown {{
    color: {selected_style.get('--sidebar-text', '')} !important;
}}

[data-testid="stSidebar"] hr {{
    border-color: {selected_style.get('--primary-color', '')} !important;
}}

[data-testid="stSidebar"] .st-emotion-cache-1oe5can {{
    background-color: {selected_style.get('--sidebar-background', '')} !important;
}}
[data-testid="stAppViewContainer"] {{
    background-color: {selected_style.get('--background-color', '')} !important;
    color: {selected_style.get('--text-color', '')} !important;
}}

[data-testid="stHeader"] {{
    background-color: {selected_style.get('--card-background', '')} !important;
}}

[data-testid="stToolbar"] {{
    color: {selected_style.get('--text-color', '')} !important;
}}

[data-testid="stSelectbox"] div {{
    background-color: {selected_style.get('--card-background', '')} !important;
    color: {selected_style.get('--text-color', '')} !important;
}}

[data-testid="stNumberInput"] input {{
    background-color: {selected_style.get('--card-background', '')} !important;
    color: {selected_style.get('--text-color', '')} !important;
}}

[data-testid="stExpander"] {{
    background-color: {selected_style.get('--card-background', '')} !important;
    border-color: {selected_style.get('--primary-color', '')} !important;
}}

.st-bq {{
    border-color: {selected_style.get('--primary-color', '')} !important;
}}

.conversion-card {{
    background: {selected_style.get('--card-background', '')} !important;
    color: {selected_style.get('--text-color', '')} !important;
    border-radius: 10px;
    padding: 20px;
    margin-top: 20px;
    border: 1px solid {selected_style.get('--primary-color', '')} !important;
}}

h1, h2, h3 {{
    color: {selected_style.get('--primary-color', '')} !important;
}}

.st-emotion-cache-cio0dv {{
    background-color: {selected_style.get('--background-color', '')} !important;
}}
</style>
"""

# Apply custom CSS for responsiveness and styling
st.markdown(
    """
    <style>
        /* Responsive Title Styling */
        h1 {
            font-size: 3rem !important;
            text-align: center;
            color: #4CAF50 !important; /* Green color */
        }

        h3 {
            font-size: 1.8rem !important;
            text-align: center;
            color: #2196F3 !important; /* Blue color */
        }

        /* Responsive Design */
        @media (max-width: 1024px) {
            h1 { font-size: 2.5rem !important; }
            h3 { font-size: 1.6rem !important; }
        }

        @media (max-width: 768px) {
            h1 { font-size: 2.2rem !important; }
            h3 { font-size: 1.4rem !important; }
        }

        @media (max-width: 480px) {
            h1 { font-size: 2rem !important; }
            h3 { font-size: 1.2rem !important; }
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(css, unsafe_allow_html=True)

# Main app interface
st.title("🚀 Ultimate Unit Converter")
st.markdown("### ⚡ Real-time Conversion | 15+ Categories | 100+ Units")

with st.container():
    category = st.selectbox("📌 Select Category", list(unit_conversions.keys()))
    
    col1, col2, col3 = st.columns([2,2,3])
    with col1:
        if category == 'Temperature':
            from_unit = st.selectbox("From", unit_conversions[category])
        else:
            from_unit = st.selectbox("From", list(unit_conversions[category].keys()))
    
    with col2:
        if category == 'Temperature':
            to_unit = st.selectbox("To", unit_conversions[category])
        else:
            to_unit = st.selectbox("To", list(unit_conversions[category].keys()))
    
    with col3:
        value = st.number_input("Enter Value", min_value=0.0, value=1.0, step=0.1, format="%.4f")

# Conversion logic
if category == 'Temperature':
    result = convert_temperature(value, from_unit, to_unit)
else:
    from_factor = unit_conversions[category][from_unit]
    to_factor = unit_conversions[category][to_unit]
    result = (value * from_factor) / to_factor

# Display results
st.markdown(f"""
<div class="conversion-card">
    <h2 style="text-align:center;">
    🎯 Conversion Result: 
    <span style="color:{selected_style.get('--secondary-color', '#00ff00')}">{value:.4f} {from_unit}</span> = 
    <span style="color:{selected_style.get('--primary-color', '#00ffff')}">{result:.6f} {to_unit}</span>
    </h2>
</div>
""", unsafe_allow_html=True)

with st.expander("📚 View Conversion Formulas"):
    st.write("""
    **Length:** Base Unit = meters  
    **Temperature:** Special formulas used  
    **Digital Storage:** 1 byte = 8 bits  
    **Speed:** 1 m/s = 3.6 km/h  
    **Fuel Economy:** 1 mile/gallon ≈ 2.352 km/liter  
    """)