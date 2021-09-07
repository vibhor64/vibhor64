# Fyle Data Extraction Challenge

## Who is this for?

This challenge is meant for candidates who wish to intern at Fyle and work with the ML team. 

* You should be available to start by Sept 7, 2021
* You should be able to commit to at least 3 months (we strongly prefer 6 months)

## Why intern at Fyle?

Fyle is a fast-growing Expense Management SaaS product. We are ~40 strong engineering team at the moment. About 60% of our engineers started off as interns. Interns at Fyle do extremely challenging and impactful work.


People love working at Fyle. Check out our Glassdoor reviews [here](https://www.glassdoor.co.in/Reviews/Fyle-Reviews-E1723235.htm). You can read stories from our teammates [here](https://stories.fylehq.com).


## Challenge outline

Under the `data` directory, you will find 20 `receipt` directories. Each directory has the following files:
* An image file that corresponds to a receipt (e.g. `data/receipt1/recpu6in7u.jpeg`)
* OCR output that was obtained by running the receipt through AWS Textract (e.g. `data/receipt1/ocr.json`). You can learn about this file's structure in this document by AWS ([link](https://docs.aws.amazon.com/textract/latest/dg/textract-dg.pdf)).
* An `expected.json` file that contains the receipt amount that should've been extracted

You'll need to fill in a stub function in extract.py called `extract_amount` that extracts the amount, given the receipt directory. You can choose to extract from the receipt or the ocr.json or combination of both.

Please don't use specific markers in the given receipts in your submission - you need to write a generic solution that works across the test data. You will be disqualified if we see hacks like this.

## Local setup

First, fork this repo to your github account (keep it public so it is easy for us to check the submission later). 

Then, clone the repo to your laptop.

This codebase requires Python 3.7+. It is recommended to use virtualenv.

Then install all the dependencies.
```
    pip install -r requirements.txt
```

You're ready to begin your task.

## Your task

Your task is to fix up `extract_amount` function so that all the tests pass i.e. amounts in all 20 receipts are extracted correctly. You are free to
use the receipt image or the AWS Textract output for this purpose - please do not ask us which one to use.

Once all the tests pass locally, take a screenshot of the successful run with 100% tests passing. Commit and push your code to your repository.

Please do not spend more than 3 hours on this task.

## Running tests

Run the tests that validate if your `extract_amount` is working fine against the test data. You can run all the tests using:

```
    python -m pytest
```
You will initially see failures. This is expected since the stub function returns a constant 0.0. The output should look like this.

```
collected 20 items                                                                                                                                               

test_extract.py::test_extract[./data/receipt8] FAILED                                                                                                                      [  5%]
test_extract.py::test_extract[./data/receipt1] FAILED                                                                                                                      [ 10%]
test_extract.py::test_extract[./data/receipt6] FAILED                                                                                                                      [ 15%]
test_extract.py::test_extract[./data/receipt7] FAILED                                                                                                                      [ 20%]
test_extract.py::test_extract[./data/receipt9] FAILED                                                                                                                      [ 25%]
...
```

If you'd like to run the test against a single directory, run it like this:

```
    python -m pytest test_extract.py::test_extract[./data/receipt1]
```

Once you finish your task successfully, all tests should pass.

## Fixing styling

Please run this command to check for any linting errors. You can run this command:

```
    pylint extract.py
```

If this shows any warnings or errors, please fix them and commit your changes.

## Submission

Once you are done with your task, please use [this form](https://forms.gle/hJAKfXdcdqgUVKfY8) to complete your submission.

## What happens next?

You will hear back within 48 hours from us via email. We may request for some changes based on reviewing your code.

Subsequently, we will schedule a phone interview with a Fyle Engineer.

If that goes well, we'll make an offer. 
