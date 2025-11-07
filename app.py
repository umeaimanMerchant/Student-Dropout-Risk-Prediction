import streamlit as st
import pandas as pd
import pickle

# ------------------------------------------------------
# Load model, scaler, and (optionally) saved feature list
# ------------------------------------------------------
with open('model/best_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('model/scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

# If you saved your training feature names
# with open('model/features.pkl', 'rb') as f:
#     feature_columns = pickle.load(f)
# Otherwise, define them manually (as you provided)
feature_columns = [
    'marital_status', 'application_mode', 'application_order', 'course',
    'daytimeevening_attendance', 'previous_qualification', 'nacionality',
    'mothers_qualification', 'fathers_qualification', 'mothers_occupation',
    'fathers_occupation', 'educational_special_needs', 'debtor',
    'tuition_fees_up_to_date', 'gender', 'scholarship_holder',
    'age_at_enrollment', 'international',
    'curricular_units_1st_sem_credited', 'curricular_units_1st_sem_enrolled',
    'curricular_units_1st_sem_evaluations', 'curricular_units_1st_sem_approved',
    'curricular_units_1st_sem_grade', 'curricular_units_1st_sem_without_evaluations',
    'curricular_units_2nd_sem_credited', 'curricular_units_2nd_sem_enrolled',
    'curricular_units_2nd_sem_evaluations', 'curricular_units_2nd_sem_approved',
    'curricular_units_2nd_sem_grade', 'curricular_units_2nd_sem_without_evaluations',
    'course_id'
]

# ------------------------------------------------------
# Streamlit UI
# ------------------------------------------------------
st.title("🎓 Student Dropout Risk Prediction")
st.markdown("Enter student details to estimate dropout likelihood.")

# --- User Inputs ---
col1, col2 = st.columns(2)

with col1:
    marital_status = st.number_input("Marital Status (encoded)", 1, 5, 1)
    application_mode = st.number_input("Application Mode", 1, 20, 1)
    application_order = st.number_input("Application Order", 1, 10, 1)
    course = st.number_input("Course", 1, 20, 1)
    daytimeevening_attendance = st.number_input("Daytime/Evening Attendance", 0, 1, 0)
    previous_qualification = st.number_input("Previous Qualification", 1, 10, 1)
    nacionality = st.number_input("Nationality (encoded)", 1, 50, 1)
    mothers_qualification = st.number_input("Mother’s Qualification", 1, 10, 1)
    fathers_qualification = st.number_input("Father’s Qualification", 1, 10, 1)
    mothers_occupation = st.number_input("Mother’s Occupation", 1, 10, 1)
    fathers_occupation = st.number_input("Father’s Occupation", 1, 10, 1)
    educational_special_needs = st.selectbox("Educational Special Needs", ["No", "Yes"])
    debtor = st.selectbox("Debtor", ["No", "Yes"])
    tuition_fees_up_to_date = st.selectbox("Tuition Fees Up To Date", ["No", "Yes"])
    gender = st.selectbox("Gender", ["Male", "Female"])
    scholarship_holder = st.selectbox("Scholarship Holder", ["No", "Yes"])

with col2:
    age_at_enrollment = st.number_input("Age at Enrollment", 15, 60, 20)
    international = st.selectbox("International", ["No", "Yes"])
    curricular_units_1st_sem_credited = st.number_input("1st Sem Credited", 0, 10, 0)
    curricular_units_1st_sem_enrolled = st.number_input("1st Sem Enrolled", 0, 10, 5)
    curricular_units_1st_sem_evaluations = st.number_input("1st Sem Evaluations", 0, 10, 5)
    curricular_units_1st_sem_approved = st.number_input("1st Sem Approved", 0, 10, 3)
    curricular_units_1st_sem_grade = st.number_input("1st Sem Grade", 0.0, 20.0, 12.0)
    curricular_units_1st_sem_without_evaluations = st.number_input("1st Sem Without Evaluations", 0, 10, 0)
    curricular_units_2nd_sem_credited = st.number_input("2nd Sem Credited", 0, 10, 0)
    curricular_units_2nd_sem_enrolled = st.number_input("2nd Sem Enrolled", 0, 10, 5)
    curricular_units_2nd_sem_evaluations = st.number_input("2nd Sem Evaluations", 0, 10, 5)
    curricular_units_2nd_sem_approved = st.number_input("2nd Sem Approved", 0, 10, 3)
    curricular_units_2nd_sem_grade = st.number_input("2nd Sem Grade", 0.0, 20.0, 12.0)
    curricular_units_2nd_sem_without_evaluations = st.number_input("2nd Sem Without Evaluations", 0, 10, 0)
    course_id = st.number_input("Course ID", 1, 50, 1)

# --- Encoding Maps ---
yes_no_map = {"No": 0, "Yes": 1}
gender_map = {"Male": 0, "Female": 1}

# ------------------------------------------------------
# Build Input DataFrame
# ------------------------------------------------------
input_dict = {
    'marital_status': marital_status,
    'application_mode': application_mode,
    'application_order': application_order,
    'course': course,
    'daytimeevening_attendance': daytimeevening_attendance,
    'previous_qualification': previous_qualification,
    'nacionality': nacionality,
    'mothers_qualification': mothers_qualification,
    'fathers_qualification': fathers_qualification,
    'mothers_occupation': mothers_occupation,
    'fathers_occupation': fathers_occupation,
    'educational_special_needs': yes_no_map[educational_special_needs],
    'debtor': yes_no_map[debtor],
    'tuition_fees_up_to_date': yes_no_map[tuition_fees_up_to_date],
    'gender': gender_map[gender],
    'scholarship_holder': yes_no_map[scholarship_holder],
    'age_at_enrollment': age_at_enrollment,
    'international': yes_no_map[international],
    'curricular_units_1st_sem_credited': curricular_units_1st_sem_credited,
    'curricular_units_1st_sem_enrolled': curricular_units_1st_sem_enrolled,
    'curricular_units_1st_sem_evaluations': curricular_units_1st_sem_evaluations,
    'curricular_units_1st_sem_approved': curricular_units_1st_sem_approved,
    'curricular_units_1st_sem_grade': curricular_units_1st_sem_grade,
    'curricular_units_1st_sem_without_evaluations': curricular_units_1st_sem_without_evaluations,
    'curricular_units_2nd_sem_credited': curricular_units_2nd_sem_credited,
    'curricular_units_2nd_sem_enrolled': curricular_units_2nd_sem_enrolled,
    'curricular_units_2nd_sem_evaluations': curricular_units_2nd_sem_evaluations,
    'curricular_units_2nd_sem_approved': curricular_units_2nd_sem_approved,
    'curricular_units_2nd_sem_grade': curricular_units_2nd_sem_grade,
    'curricular_units_2nd_sem_without_evaluations': curricular_units_2nd_sem_without_evaluations,
    'course_id': course_id
}

input_df = pd.DataFrame([input_dict])
input_df = input_df.reindex(columns=feature_columns, fill_value=0)

# ------------------------------------------------------
# Prediction
# ------------------------------------------------------
if st.button("🔮 Predict Dropout Risk"):
    try:
        # Scale numeric features
        scaled_input = scaler.transform(input_df)

        # Predict using trained model
        prediction = model.predict(scaled_input)[0]
        probability = (
            model.predict_proba(scaled_input)[0][1]
            if hasattr(model, "predict_proba")
            else None
        )

        # Display results
        if prediction == 1:
            st.error("⚠️ Prediction: Student is likely to **DROP OUT**.")
        else:
            st.success("✅ Prediction: Student is likely to **CONTINUE**.")

        if probability is not None:
            st.write(f"**Dropout probability:** {probability:.2f}")

    except Exception as e:
        st.error(f"Error during prediction: {e}")
