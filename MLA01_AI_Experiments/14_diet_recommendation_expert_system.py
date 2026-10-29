"""Experiment 14: Rule-based Diet Recommendation Expert System.
Educational example only; not medical/nutritional advice."""

def recommend_diet(age, bmi, condition):
    condition = condition.strip().lower()
    recommendations = []
    if age < 18:
        recommendations.append("Choose a balanced diet suitable for growth; consult a qualified professional.")
    elif bmi < 18.5:
        recommendations.append("Include balanced meals with adequate energy and protein.")
    elif bmi < 25:
        recommendations.append("Maintain a balanced diet with vegetables, fruits, whole grains and protein.")
    elif bmi < 30:
        recommendations.append("Consider balanced portions and regular activity; seek personalised advice if needed.")
    else:
        recommendations.append("Consider professional guidance for a safe, sustainable nutrition plan.")
    if condition in {"diabetes", "diabetic"}:
        recommendations.append("For diabetes, personalise carbohydrate choices with a clinician or dietitian.")
    elif condition in {"hypertension", "high blood pressure"}:
        recommendations.append("For hypertension, discuss sodium intake and a heart-healthy plan with a clinician.")
    elif condition in {"none", "no", ""}:
        recommendations.append("No additional condition specified.")
    else:
        recommendations.append(f"For {condition}, get advice tailored to your medical history.")
    return recommendations

if __name__ == "__main__":
    try:
        age = int(input("Enter age: "))
        bmi = float(input("Enter BMI: "))
        condition = input("Enter health condition (e.g., none/diabetes/hypertension): ")
        print("\nDiet recommendation:")
        for item in recommend_diet(age, bmi, condition):
            print("-", item)
    except ValueError:
        print("Please enter a valid age and BMI.")
