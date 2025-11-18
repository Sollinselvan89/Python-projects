import simple_csv_data_reader


def test_display_csv_pretty(capsys):
    """Test printing all rows."""
    simple_csv_data_reader.display_csv_pretty("students.csv")
    captured = capsys.readouterr()

    assert captured.out.strip() != ""
    assert "Name:" in captured.out


def test_filter_age_above_15(capsys):
    """Test that age filter prints only students with age > 15."""
    simple_csv_data_reader.filter_age_above_15("students.csv")
    captured = capsys.readouterr()

    assert "Students with age > 15" in captured.out

    
    for line in captured.out.split("\n"):
        if "Age:" in line:
            age_part = line.split("|")[1].strip().replace("Age: ", "")
            assert age_part.isdigit()
            assert int(age_part) > 15


def test_filter_grade_A(capsys):
    """Test that only grade A students are printed."""
    simple_csv_data_reader.filter_grade_A("students.csv")
    captured = capsys.readouterr()

    assert "Students with Grade == A" in captured.out

    for line in captured.out.split("\n"):
        if "Grade:" in line:
            grade = line.split("|")[-1].strip().replace("Grade: ", "")
            assert grade.upper() == "A"


def test_get_filter_choice(monkeypatch):
    """Test menu choice handling."""
    monkeypatch.setattr("builtins.input", lambda _: "2")
    assert simple_csv_data_reader.get_filter_choice() == 2

    monkeypatch.setattr("builtins.input", lambda _: "4")
    assert simple_csv_data_reader.get_filter_choice() == 4
