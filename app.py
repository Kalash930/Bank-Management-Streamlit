import streamlit as st
from bank_utils import load_data, save_data, generate_account_number, find_user

data = load_data()

st.set_page_config(page_title="Bank Management System", page_icon="🏦")
st.title("🏦 Bank Management System")

menu = st.sidebar.selectbox("Select Operation", 
    ["Create Account", "Deposit", "Withdraw", "Show Details", "Update Account", "Delete Account"])

if menu == "Create Account":
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0)
    email = st.text_input("Email")
    pin = st.text_input("PIN", type="password", max_chars=4)
    if st.button("Create Account"):
        if age < 18 or len(pin) != 4:
            st.error("You must be at least 18 and have a 4-digit PIN.")
        else:
            acc_no = generate_account_number(data)
            user = {
                "name": name,
                "age": age,
                "email": email,
                "pin": int(pin),
                "accountNo": acc_no,
                "balance": 0
            }
            data.append(user)
            save_data(data)
            st.success(f"Account created successfully! Your Account No: {acc_no}")

elif menu == "Deposit":
    acc_no = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount to deposit", min_value=1)
    if st.button("Deposit"):
        user = find_user(acc_no, pin, data)
        if user:
            if amount > 10000:
                st.error("Maximum deposit limit is ₹10,000.")
            else:
                user['balance'] += amount
                save_data(data)
                st.success("Amount deposited successfully.")
        else:
            st.error("Invalid account number or PIN.")

elif menu == "Withdraw":
    acc_no = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount to withdraw", min_value=1)
    if st.button("Withdraw"):
        user = find_user(acc_no, pin, data)
        if user:
            if user['balance'] < amount:
                st.error("Insufficient balance.")
            else:
                user['balance'] -= amount
                save_data(data)
                st.success("Amount withdrawn successfully.")
        else:
            st.error("Invalid account number or PIN.")

elif menu == "Show Details":
    acc_no = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    if st.button("Show"):
        user = find_user(acc_no, pin, data)
        if user:
            st.json(user)
        else:
            st.error("Invalid account number or PIN.")

elif menu == "Update Account":
    acc_no = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    if st.button("Authenticate"):
        user = find_user(acc_no, pin, data)
        if user:
            new_name = st.text_input("New Name", value=user["name"])
            new_email = st.text_input("New Email", value=user["email"])
            new_pin = st.text_input("New PIN (4 digits)", type="password", max_chars=4)

            if st.button("Update"):
                user['name'] = new_name
                user['email'] = new_email
                if new_pin:
                    if len(new_pin) == 4:
                        user['pin'] = int(new_pin)
                    else:
                        st.error("PIN must be 4 digits.")
                save_data(data)
                st.success("Details updated successfully.")
        else:
            st.error("Invalid account number or PIN.")

elif menu == "Delete Account":
    acc_no = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    if st.button("Delete"):
        user = find_user(acc_no, pin, data)
        if user:
            data.remove(user)
            save_data(data)
            st.success("Account deleted successfully.")
        else:
            st.error("Invalid account number or PIN.")
