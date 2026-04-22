"""Simple patient health assistant.

This script collects basic health indicators and produces individualized
best-practice recommendations using a lightweight AI-style scoring model.

Disclaimer: Educational only, not medical advice.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Tuple


@dataclass
class PatientData:
    age: int
    sex: str
    height_cm: float
    weight_kg: float
    systolic_bp: int
    diastolic_bp: int
    resting_heart_rate: int
    fasting_glucose: float
    sleep_hours: float
    weekly_activity_minutes: int
    smoker: bool


def get_float(prompt: str, minimum: float | None = None, maximum: float | None = None) -> float:
    while True:
        try:
            value = float(input(prompt).strip())
            if minimum is not None and value < minimum:
                print(f"Please enter a value >= {minimum}.")
                continue
            if maximum is not None and value > maximum:
                print(f"Please enter a value <= {maximum}.")
                continue
            return value
        except ValueError:
            print("Invalid number. Try again.")


def get_int(prompt: str, minimum: int | None = None, maximum: int | None = None) -> int:
    while True:
        try:
            value = int(input(prompt).strip())
            if minimum is not None and value < minimum:
                print(f"Please enter a value >= {minimum}.")
                continue
            if maximum is not None and value > maximum:
                print(f"Please enter a value <= {maximum}.")
                continue
            return value
        except ValueError:
            print("Invalid integer. Try again.")


def get_yes_no(prompt: str) -> bool:
    while True:
        answer = input(prompt).strip().lower()
        if answer in {"y", "yes"}:
            return True
        if answer in {"n", "no"}:
            return False
        print("Please answer y/n.")


def collect_patient_data() -> PatientData:
    print("\n=== Patient Health Intake ===")
    age = get_int("Age (years): ", minimum=1, maximum=120)
    sex = input("Sex at birth (female/male/intersex/prefer not to say): ").strip()
    height_cm = get_float("Height (cm): ", minimum=90, maximum=250)
    weight_kg = get_float("Weight (kg): ", minimum=25, maximum=350)
    systolic_bp = get_int("Systolic blood pressure (mmHg): ", minimum=70, maximum=250)
    diastolic_bp = get_int("Diastolic blood pressure (mmHg): ", minimum=40, maximum=150)
    resting_heart_rate = get_int("Resting heart rate (bpm): ", minimum=30, maximum=220)
    fasting_glucose = get_float("Fasting glucose (mg/dL): ", minimum=40, maximum=450)
    sleep_hours = get_float("Average sleep per night (hours): ", minimum=0, maximum=24)
    weekly_activity_minutes = get_int("Weekly moderate/vigorous activity (minutes): ", minimum=0, maximum=3000)
    smoker = get_yes_no("Current smoker? (y/n): ")

    return PatientData(
        age=age,
        sex=sex,
        height_cm=height_cm,
        weight_kg=weight_kg,
        systolic_bp=systolic_bp,
        diastolic_bp=diastolic_bp,
        resting_heart_rate=resting_heart_rate,
        fasting_glucose=fasting_glucose,
        sleep_hours=sleep_hours,
        weekly_activity_minutes=weekly_activity_minutes,
        smoker=smoker,
    )


def compute_features(patient: PatientData) -> Dict[str, float]:
    height_m = patient.height_cm / 100
    bmi = patient.weight_kg / (height_m * height_m)

    # Lightweight "AI-like" normalized feature vector for pattern scoring.
    return {
        "bmi": bmi,
        "bp_risk": max(0.0, (patient.systolic_bp - 120) / 40) + max(0.0, (patient.diastolic_bp - 80) / 20),
        "glucose_risk": max(0.0, (patient.fasting_glucose - 99) / 40),
        "sleep_gap": max(0.0, (7.0 - patient.sleep_hours) / 3.0),
        "activity_gap": max(0.0, (150 - patient.weekly_activity_minutes) / 150),
        "hr_risk": max(0.0, (patient.resting_heart_rate - 85) / 35),
        "smoking": 1.0 if patient.smoker else 0.0,
    }


def ai_priority_scores(features: Dict[str, float]) -> List[Tuple[str, float]]:
    """Weighted risk scoring to prioritize recommendations."""
    priorities = {
        "Blood pressure": 0.30 * features["bp_risk"],
        "Blood sugar/metabolic health": 0.24 * features["glucose_risk"] + 0.12 * max(0, features["bmi"] - 25) / 10,
        "Physical activity": 0.20 * features["activity_gap"],
        "Sleep quality": 0.15 * features["sleep_gap"],
        "Cardiorespiratory fitness": 0.11 * features["hr_risk"],
        "Smoking cessation": 0.25 * features["smoking"],
    }
    ranked = sorted(priorities.items(), key=lambda x: x[1], reverse=True)
    return ranked


def recommendation_for(topic: str, patient: PatientData, bmi: float) -> str:
    suggestions = {
        "Blood pressure": (
            "Prioritize sodium reduction, hydration, and 30+ minutes of most-day movement. "
            "Track home BP 3-4 times/week and review trends with your clinician."
        ),
        "Blood sugar/metabolic health": (
            "Center meals around vegetables, fiber, lean protein, and minimally processed carbs. "
            "Consider post-meal walks (10-15 minutes) to improve glucose control."
        ),
        "Physical activity": (
            "Aim toward at least 150 minutes/week of moderate activity plus 2 strength sessions. "
            "Start small (10-20 minute walks) and build consistency before intensity."
        ),
        "Sleep quality": (
            "Target a stable sleep window with 7-9 hours/night, reduce late caffeine, and avoid heavy screens before bed."
        ),
        "Cardiorespiratory fitness": (
            "Use progressive aerobic training (brisk walking/cycling) and monitor resting heart rate changes over time."
        ),
        "Smoking cessation": (
            "Discuss nicotine replacement or medication options with a clinician and set a structured quit date with support."
        ),
    }

    base = suggestions.get(topic, "Maintain healthy habits and continue routine preventive care.")
    if topic == "Blood sugar/metabolic health" and bmi >= 30:
        return base + " A 5-10% weight reduction can significantly improve metabolic markers."
    if topic == "Physical activity" and patient.age >= 60:
        return base + " Add balance/flexibility exercises to reduce fall risk."
    return base


def build_report(patient: PatientData) -> str:
    features = compute_features(patient)
    bmi = features["bmi"]
    ranked = ai_priority_scores(features)

    bmi_category = "Underweight" if bmi < 18.5 else "Healthy" if bmi < 25 else "Overweight" if bmi < 30 else "Obesity"

    lines = []
    lines.append("\n=== AI-Informed Health Best-Practices Report ===")
    lines.append("(Educational support only — not a diagnosis or treatment plan.)")
    lines.append(f"BMI: {bmi:.1f} ({bmi_category})")
    lines.append(
        f"BP: {patient.systolic_bp}/{patient.diastolic_bp} mmHg | Fasting glucose: {patient.fasting_glucose:.0f} mg/dL | "
        f"Activity: {patient.weekly_activity_minutes} min/week"
    )
    lines.append("\nTop focus areas (AI priority model):")

    top_items = [item for item in ranked if item[1] > 0.03][:3]
    if not top_items:
        lines.append("1) Maintain current routines: your entered metrics show no major risk spikes.")
        lines.append("2) Continue preventive screening and annual checkups.")
        lines.append("3) Keep sleep, nutrition, and activity consistent.")
    else:
        for i, (topic, score) in enumerate(top_items, 1):
            lines.append(f"{i}) {topic} (priority score: {score:.2f})")
            lines.append(f"   - {recommendation_for(topic, patient, bmi)}")

    lines.append("\nSuggested next step: share this summary with a licensed clinician for personalized medical guidance.")
    return "\n".join(lines)


def main() -> None:
    print("Patient Health AI Helper")
    print("----------------------------------")
    patient = collect_patient_data()
    report = build_report(patient)
    print(report)


if __name__ == "__main__":
    main()
