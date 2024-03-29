from subprocess import run, PIPE
import os
import shutil
import pytest

B_FILE_NAME = './simple_db_find'
B_FILE_DIR = './bin'
B_FILE_FULL_PATH = os.path.join(B_FILE_DIR, B_FILE_NAME)
DB_FILE_NAME = './data/database.txt'

def test_bin_folder_contains_simple_db_find():
    assert os.path.isfile(B_FILE_FULL_PATH)

def test_simple_db_not_correct_input_1():
    result = run([B_FILE_NAME], cwd=B_FILE_DIR, input='FIND 2022', encoding='utf-8', stdout=PIPE, stderr=PIPE)
    assert result.returncode != 0
    assert "Puck you, Verter!" in result.stderr

def test_simple_db_not_correct_input_2():
    result = run([B_FILE_NAME], cwd=B_FILE_DIR, input='FIND 13', encoding='utf-8', stdout=PIPE, stderr=PIPE)
    assert result.returncode != 0
    assert "Puck you, Verter!" in result.stderr

def test_simple_db_not_correct_input_3():
    result = run([B_FILE_NAME], cwd=B_FILE_DIR, input='ass', encoding='utf-8', stdout=PIPE, stderr=PIPE)
    assert result.returncode != 0
    assert "Puck you, Verter!" in result.stderr

def test_simple_db_not_correct_input_4():
    result = run([B_FILE_NAME], cwd=B_FILE_DIR, input='FIND 2022.01.16', encoding='utf-8', stdout=PIPE, stderr=PIPE)
    assert result.returncode != 0
    assert "Puck you, Verter!" in result.stderr

def test_simple_db_not_correct_input_5():
    result = run([B_FILE_NAME], cwd=B_FILE_DIR, input='FIND -1.12.2000', encoding='utf-8', stdout=PIPE, stderr=PIPE)
    assert result.returncode != 0
    assert "Puck you, Verter!" in result.stderr

def test_simple_db_find_1():
    shutil.copy('./tests/data/simple_db_find.txt', DB_FILE_NAME)
    result = run([B_FILE_NAME], cwd=B_FILE_DIR, input='FIND 31.12.2021 EXIT', encoding='utf-8', stdout=PIPE, stderr=PIPE)
    assert result.returncode == 0
    assert os.path.isfile(DB_FILE_NAME)
    assert result.stdout.strip() == '31.12.2021 23:30:45 RedBull 220\n31.12.2021 23:30:45 BeerFromBrugge 600\n31.12.2021 13:05:16 Pasta 385'

def test_simple_db_find_2():
    shutil.copy('./tests/data/simple_db_find.txt', DB_FILE_NAME)
    result = run([B_FILE_NAME], cwd=B_FILE_DIR, input='FIND 16.06.2025 EXIT', encoding='utf-8', stdout=PIPE, stderr=PIPE)
    assert result.returncode == 0
    assert os.path.isfile(DB_FILE_NAME)
    assert result.stdout.strip() == 'NO DATA'

if __name__ == "__main__":
    pytest.main()
