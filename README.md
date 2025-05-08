# shaksz
All coding and design solutions as package


# Unit Tests
`python -m unittest discover -s tests`

# Build package


    python setup.py sdist bdist_wheel

    pip install twine

    twine upload dist/*

# Publish Test

    twine upload --repository testpypi dist/*

# Publish Prod
