# Challenge-2
Challenge 2 for Columbia FinTech Bootcamp

## Technologies
This program uses version 3 of the Python programming language with the following imported libraries:
* sys
* fire
* questionary
* pathlib
* csv

## Installation
None required.

## Usage
This program prompts a user for the following inputs:
* The location of a bank data csv (file path) that specifies: 
    * The name of the bank
    * The maximum loan amount from that bank
    * The maximum LTV (loan-to-value ratio) they will allow
    * The maximum DTI (debt-to-income ratio) they will allow
    * The minimum credit score to take out a loan
    * The interest rate attached to their loans
* The user's credit score (integer)
* The user's current monthly debt (float)
* The user's monthly income (float)
* The user's desired loan amount (float)
* The user's home value (float)

The program then finds the loans in the provided dataset that match the user's inputted credit profile. The user is then prompted to save these qualifying loans in a new csv file.

## Example

Suppose a user with a credit score of 750, monthly income of \$15,000, and no current monthly debt wants to take out a \$100,000 loan to finance the purchase of a new home worth \$150,000.  

The user would run `python  app.py` in a development environment supporting the aforementioned packages, then enter in their information described above in response to each questionary prompt. The program would then calculate the qualifying loans for that user and prompt the user to save these loans in a location specified by the user. See an example of this flow below:

![](./images/Challenge 2 Code Example)

## Contributors
The starter code was provided by the Columbia Fintech Engineering Bootcamp. The additions required were made solely by me.

## License
None