#!/bin/bash

# activate virtual environment
source venv/bin/activate

# run the test suite
pytest test_app.py

# return exit code 0 if passed, 1 if failed
if [ $? -eq 0 ]; then
    echo "All tests passed!"
    exit 0
else
    echo "Tests failed!"
    exit 1
fi