from input_module.input_handler import get_student_data
from cgpa_calculator.cgpa_calc import calculate_cgpa
from analytics_module.performance_analysis import identify_weak_subjects, improvement_suggestions
from visualization_module.visualization_module import plot_cgpa_trend, radar_chart
import pandas as pd

# Step 1: Get user input
df = get_student_data()

# Step 2: CGPA Calculation
cgpa = calculate_cgpa(df)
print(f"\nYour CGPA is: {cgpa}")

# Step 3: Weak Subject Analysis
weak = identify_weak_subjects(df)
print("\nWeak Subjects:\n", weak)

# Step 4: Suggestions
target = float(input("\nEnter target CGPA to get suggestions: "))
suggestions = improvement_suggestions(df, target)
print("\nImprovement Suggestions:\n", suggestions)

# Step 5: Visualization (optional)
radar_chart(df)

# Step 6: Show final report in terminal
print("\nFinal Report:\n")
print(df.to_markdown(index=False))
