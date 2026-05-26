"""
Exercise 3 Solution: Interactive Grade Management System (Advanced)
===================================================================
Run: python3 03_grade_management_system.py

Demonstrates:
- while True loop for menu-driven program
- for loops for iterating over students/grades
- Nested loops for multi-subject processing
- break and continue for flow control
- enumerate() for numbered displays
- zip() for parallel data processing
- range() for generating chart bars
- Loop else clause for search operations
"""


def grade_management_system():
    """
    Interactive student grade management system.

    Features:
    - Add/remove students
    - Record grades for multiple subjects
    - Calculate statistics (mean, median, highest, lowest)
    - Search students by name (partial match)
    - Display grade distribution as text bar chart
    - Filter by grade range
    - Export summary
    """
    students = {}  # {"name": {"math": 85, "science": 90, ...}}

    def get_student_average(name):
        """Calculate a student's average grade."""
        grades = students[name]
        if not grades:
            return 0.0
        return sum(grades.values()) / len(grades.values())

    def get_all_grades():
        """Get a flat list of all grades across all students."""
        all_grades = []
        for name in students:
            for subject, grade in students[name].items():
                all_grades.append(grade)
        return all_grades

    def get_letter_grade(score):
        """Convert numeric score to letter grade."""
        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        else:
            return "F"

    # Main program loop
    while True:
        print("\n" + "=" * 50)
        print("    STUDENT GRADE MANAGEMENT SYSTEM")
        print("=" * 50)
        print("  1. Add Student")
        print("  2. Add/Update Grade")
        print("  3. View All Students")
        print("  4. Search Student")
        print("  5. Class Statistics")
        print("  6. Grade Distribution Chart")
        print("  7. Filter by Grade Range")
        print("  8. Remove Student")
        print("  9. Exit")
        print("-" * 50)

        choice = input("  Select option: ").strip()

        match choice:
            case "1":
                # ── Add Student ──────────────────────────────────
                print("\n  --- Add Student ---")

                # Input validation loop
                while True:
                    name = input("  Enter student name: ").strip()

                    if not name:
                        print("  Name cannot be empty. Try again.")
                        continue

                    # Check for duplicates (case-insensitive)
                    duplicate = False
                    for existing_name in students:
                        if existing_name.lower() == name.lower():
                            print(f"  '{existing_name}' already exists!")
                            duplicate = True
                            break

                    if duplicate:
                        continue

                    break

                students[name] = {}
                print(f"  Student '{name}' added successfully!")

            case "2":
                # ── Add/Update Grade ─────────────────────────────
                print("\n  --- Add/Update Grade ---")

                if not students:
                    print("  No students yet! Add a student first.")
                    continue

                # Show student list
                print("  Available students:")
                for i, name in enumerate(students, 1):
                    print(f"    {i}. {name}")

                # Select student
                student_input = input("  Enter student name or number: ").strip()

                # Allow selection by number
                selected_name = None
                if student_input.isdigit():
                    idx = int(student_input) - 1
                    names_list = list(students.keys())
                    if 0 <= idx < len(names_list):
                        selected_name = names_list[idx]
                else:
                    # Search by name
                    for name in students:
                        if name.lower() == student_input.lower():
                            selected_name = name
                            break

                if selected_name is None:
                    print("  Student not found!")
                    continue

                # Get subject
                subject = input(f"  Enter subject for {selected_name}: ").strip().lower()
                if not subject:
                    print("  Subject cannot be empty!")
                    continue

                # Get grade with validation
                while True:
                    grade_input = input(f"  Enter grade (0-100): ").strip()
                    try:
                        grade = float(grade_input)
                        if 0 <= grade <= 100:
                            break
                        else:
                            print("  Grade must be between 0 and 100.")
                    except ValueError:
                        print("  Invalid number. Try again.")

                students[selected_name][subject] = grade
                print(f"  Grade recorded: {selected_name} -> {subject}: {grade}")

            case "3":
                # ── View All Students ────────────────────────────
                print("\n  --- All Students ---")

                if not students:
                    print("  No students registered yet.")
                    continue

                print(f"  {'Name':<15} {'Subjects':<30} {'Average':>8}")
                print(f"  {'─' * 55}")

                for name, grades in students.items():
                    if grades:
                        subjects_str = ", ".join(
                            f"{subj}: {g:.0f}" for subj, g in grades.items()
                        )
                        avg = get_student_average(name)
                        letter = get_letter_grade(avg)
                        print(f"  {name:<15} {subjects_str:<30} {avg:>5.1f} ({letter})")
                    else:
                        print(f"  {name:<15} {'(no grades)':<30} {'N/A':>8}")

                print(f"  {'─' * 55}")
                print(f"  Total students: {len(students)}")

            case "4":
                # ── Search Student ───────────────────────────────
                print("\n  --- Search Student ---")

                if not students:
                    print("  No students to search.")
                    continue

                query = input("  Enter name to search: ").strip().lower()

                if not query:
                    print("  Search query cannot be empty!")
                    continue

                # Partial match search using loop + continue
                found_count = 0
                for name, grades in students.items():
                    if query not in name.lower():
                        continue  # Skip non-matching students

                    found_count += 1
                    print(f"\n  Found: {name}")
                    if grades:
                        print(f"    Subjects: {len(grades)}")
                        for subject, grade in grades.items():
                            letter = get_letter_grade(grade)
                            print(f"      {subject.title()}: {grade:.0f} ({letter})")
                        avg = get_student_average(name)
                        print(f"    Average: {avg:.1f} ({get_letter_grade(avg)})")
                    else:
                        print("    No grades recorded yet.")

                # Using a check after the loop (alternative to loop-else)
                if found_count == 0:
                    print(f"  No students matching '{query}' found.")
                else:
                    print(f"\n  Found {found_count} student(s).")

            case "5":
                # ── Class Statistics ─────────────────────────────
                print("\n  --- Class Statistics ---")

                all_grades = get_all_grades()

                if not all_grades:
                    print("  No grades recorded yet.")
                    continue

                # Calculate stats using loops
                total = 0
                highest = all_grades[0]
                lowest = all_grades[0]

                for grade in all_grades:
                    total += grade
                    if grade > highest:
                        highest = grade
                    if grade < lowest:
                        lowest = grade

                average = total / len(all_grades)

                # Calculate median
                sorted_grades = sorted(all_grades)
                n = len(sorted_grades)
                if n % 2 == 0:
                    median = (sorted_grades[n // 2 - 1] + sorted_grades[n // 2]) / 2
                else:
                    median = sorted_grades[n // 2]

                # Find top students using loop
                print(f"\n  Total grades recorded: {len(all_grades)}")
                print(f"  Total students:        {len(students)}")
                print(f"  {'─' * 35}")
                print(f"  Class Average:  {average:.1f}")
                print(f"  Median:         {median:.1f}")
                print(f"  Highest Grade:  {highest:.0f}")
                print(f"  Lowest Grade:   {lowest:.0f}")
                print(f"  Range:          {highest - lowest:.0f}")

                # Top performers
                print(f"\n  --- Top Performers ---")
                student_avgs = []
                for name in students:
                    if students[name]:  # Skip students with no grades
                        avg = get_student_average(name)
                        student_avgs.append((name, avg))

                # Sort by average (descending) using simple bubble sort loop
                for i in range(len(student_avgs)):
                    for j in range(i + 1, len(student_avgs)):
                        if student_avgs[j][1] > student_avgs[i][1]:
                            student_avgs[i], student_avgs[j] = student_avgs[j], student_avgs[i]

                # Show top 5
                for rank, (name, avg) in enumerate(student_avgs[:5], 1):
                    letter = get_letter_grade(avg)
                    print(f"    {rank}. {name}: {avg:.1f} ({letter})")

            case "6":
                # ── Grade Distribution Chart ─────────────────────
                print("\n  --- Grade Distribution ---")

                all_grades = get_all_grades()

                if not all_grades:
                    print("  No grades recorded yet.")
                    continue

                # Count grades in each bucket using loops
                buckets = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
                ranges = {
                    "A": "90-100",
                    "B": "80-89",
                    "C": "70-79",
                    "D": "60-69",
                    "F": "0-59",
                }

                for grade in all_grades:
                    letter = get_letter_grade(grade)
                    buckets[letter] += 1

                # Find max count for scaling the bar
                max_count = 0
                for count in buckets.values():
                    if count > max_count:
                        max_count = count

                # Draw chart
                bar_max_width = 25
                print(f"\n  {'─' * 48}")

                for letter, count in buckets.items():
                    range_str = ranges[letter]
                    # Scale bar width
                    if max_count > 0:
                        bar_width = int((count / max_count) * bar_max_width)
                    else:
                        bar_width = 0

                    filled = "█" * bar_width
                    empty = "░" * (bar_max_width - bar_width)
                    label = "student" if count == 1 else "students"
                    print(f"  {letter} ({range_str:>6}): {filled}{empty} {count} {label}")

                print(f"  {'─' * 48}")
                avg = sum(all_grades) / len(all_grades)
                print(f"  Total: {len(all_grades)} grades | Class Average: {avg:.1f}")

            case "7":
                # ── Filter by Grade Range ────────────────────────
                print("\n  --- Filter by Grade Range ---")

                if not students:
                    print("  No students to filter.")
                    continue

                # Get range with validation
                while True:
                    min_input = input("  Enter minimum grade (0-100): ").strip()
                    try:
                        min_grade = float(min_input)
                        if 0 <= min_grade <= 100:
                            break
                        print("  Must be between 0 and 100.")
                    except ValueError:
                        print("  Invalid number.")

                while True:
                    max_input = input("  Enter maximum grade (0-100): ").strip()
                    try:
                        max_grade = float(max_input)
                        if 0 <= max_grade <= 100:
                            break
                        print("  Must be between 0 and 100.")
                    except ValueError:
                        print("  Invalid number.")

                # Swap if needed
                if min_grade > max_grade:
                    min_grade, max_grade = max_grade, min_grade

                print(f"\n  Students with grades between {min_grade:.0f} and {max_grade:.0f}:")
                print(f"  {'─' * 45}")

                found = 0
                for name, grades in students.items():
                    # Check each subject grade
                    matching_subjects = []
                    for subject, grade in grades.items():
                        if min_grade <= grade <= max_grade:
                            matching_subjects.append((subject, grade))

                    if matching_subjects:
                        found += 1
                        print(f"  {name}:")
                        for subject, grade in matching_subjects:
                            print(f"    {subject.title()}: {grade:.0f}")

                if found == 0:
                    print("  No students found in this range.")
                else:
                    print(f"  {'─' * 45}")
                    print(f"  Found {found} student(s) with grades in range.")

            case "8":
                # ── Remove Student ───────────────────────────────
                print("\n  --- Remove Student ---")

                if not students:
                    print("  No students to remove.")
                    continue

                # Show list
                print("  Current students:")
                for i, name in enumerate(students, 1):
                    print(f"    {i}. {name}")

                name_input = input("  Enter name to remove: ").strip()

                # Find student (case-insensitive)
                found_name = None
                for name in students:
                    if name.lower() == name_input.lower():
                        found_name = name
                        break
                else:
                    print(f"  Student '{name_input}' not found!")
                    continue

                # Confirmation
                confirm = input(f"  Are you sure you want to remove '{found_name}'? (y/n): ").strip().lower()
                if confirm == "y":
                    del students[found_name]
                    print(f"  '{found_name}' removed successfully.")
                else:
                    print("  Cancelled.")

            case "9":
                # ── Exit ─────────────────────────────────────────
                print("\n  --- Session Summary ---")
                if students:
                    print(f"  Students managed: {len(students)}")
                    total_grades = len(get_all_grades())
                    print(f"  Total grades recorded: {total_grades}")
                print("\n  Goodbye! Keep studying!")
                break

            case _:
                print("  Invalid option. Please enter 1-9.")


# Run the system
if __name__ == "__main__":
    grade_management_system()
