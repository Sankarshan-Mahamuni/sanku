import streamlit as st
import pandas as pd
from prettytable import PrettyTable
from PIL import Image
import io


# Set page configuration
st.set_page_config(layout="wide")

# Title and description
st.title("Experiment 5: Determining the Electrochemical Equivalent of Copper")
st.write("This web app allows you to determine the electrochemical equivalent of copper.")

# Display prior concepts and apparatus details
st.header("Prior Concepts")
st.write("Electrolysis, ECE, Ionization, Faraday's law of electrolysis.")

st.header("Apparatus")
st.write("""6.0 APPARATUS:
6.1 Equipments:
Two copper plates, glass beakers (1000 ml), conducting wires, 12 volts D.C. Eliminator.
Digital Ammeter, Polish paper, Drier, Digital Electronic balance.
6.2 Chemicals:
10% Copper sulfate solution, 1% Sulphuric acid, Dil HCl.""")

# Instructions
st.sidebar.header("Instructions")
st.sidebar.write("Follow the instructions to perform the experiment.")
image_path = "tha.png"
image = Image.open(image_path)
resized_image = image.resize((500,500))

    # Convert PIL Image to BytesIO object
image_bytes = io.BytesIO()

resized_image.save(image_bytes, format="PNG")  # Adjust the format based on your image type
st.image(image_bytes, caption="concept", use_column_width=False)

image_path2 = "tha2.png"
image = Image.open(image_path2)
resized_image = image.resize((300,300))

    # Convert PIL Image to BytesIO object
image_bytes = io.BytesIO()

resized_image.save(image_bytes, format="PNG")  # Adjust the format based on your image type
st.image(image_bytes, caption="concept", use_column_width=False)
st.title("STEPS:- ")
st.subheader("1.Clean the copper cathode using polish paper, dilute HCl and then wash with water.")
st.subheader("2.Dry it in oven.")
st.subheader("3.Weigh the copper cathode.")
st.subheader("4.Set up the apparatus as indicated in the diagram.")
st.subheader("5.Connect the circuit as shown in diagram.")
st.subheader("6.Adjust the required current between 0.5 to 1.5 ampere and pass the current for 15 minutes.")
st.subheader("7.Remove the cathode and dry it.")
st.subheader("8.Weight the copper cathode accurately.")
st.subheader("9.Tabulate the observations""")


# Sidebar for input
st.sidebar.header("Input Values")
w1 = st.sidebar.number_input("Weight of copper cathode before deposition (w1):")
w2 = st.sidebar.number_input("Weight of copper cathode after deposition (w2):")
I = st.sidebar.number_input("Current in ampere:")
t = st.sidebar.number_input("Time in seconds:")

# Calculate and display equivalent weight
if st.sidebar.button("Calculate Equivalent Weight"):
    st.write("Calculating...")
    w = round(w2 - w1, 3)
    z = w / (I * t)

    # Create a table of input values
    value_list = [w1, w2, w, I, t]
    data = {
        'Observations': [
            'Weight of copper cathode before deposition',
            'Weight of copper cathode after deposition',
            'Weight of copper deposited',
            'Current in ampere',
            'Time in seconds'
        ],
        'Sub-Observations': [
            'W1',
            'W2',
            'W=W2-W1',
            'I',
            'T'
        ],
        'Value': value_list
    }
    df = pd.DataFrame(data)

    # Use PrettyTable to create a well-structured table
    table = PrettyTable()
    table.field_names = df.columns
    for row in df.itertuples(index=False):
        table.add_row(row)

    # Display the table of input values and the equivalent weight
    st.write("User-Entered Data:")
    st.write(table)
    st.write(f"The equivalent weight is {z:.2e}")


