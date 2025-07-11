# Jump_Marks: Student Performance Analysis Tool

Jump_Marks is a modular Python program to calculate CGPA, analyze weak subjects, provide improvement suggestions, visualize performance trends, and display a final report — all from the terminal.

## Features

- Interactive subject data input
- CGPA calculation with grade point logic
- Weak subject detection
- Smart suggestions to reach your target CGPA
- Radar chart visualization of subject performance
- Final summary shown neatly in terminal (no Excel export needed)

## Project Structure

```
Jump_Marks/
│
├── main.py
├── input_module/
│   └── input_handler.py
├── cgpa_calculator/
│   └── cgpa_calc.py
├── analytics_module/
│   └── performance_analysis.py
├── prediction_module/
│   └── predictive_module.py
├── visualization_module/
│   └── visualization_module.py
```

## Requirements

Install the required packages:

```bash
pip install pandas matplotlib seaborn plotly tabulate scikit-learn
```

## How to Run

Run the program from your terminal:

```bash
python main.py
```

Then follow the prompts:

1. Enter number of subjects  
2. For each subject, provide:
   - Subject name  
   - Credit  
   - Marks  
3. Enter your target CGPA for improvement suggestions

The program will:
- Calculate and show your CGPA
- Highlight weak subjects (below Grade Point 7)
- Suggest score improvements
- Plot a radar chart
- Print the final summary report in the terminal

## Sample Input

```
Enter number of subjects: 3

Subject 1:
Name: DSA
Credit: 4
Marks: 78

Subject 2:
Name: Math
Credit: 3
Marks: 60

Subject 3:
Name: OS
Credit: 3
Marks: 50

Enter target CGPA: 8.0
```

## Notes

- Marks are converted to Grade Points using internal logic.
- Radar chart is displayed in a separate window.
- All outputs are printed directly in the terminal.