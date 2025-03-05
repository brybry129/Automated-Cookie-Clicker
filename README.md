# Automated Cookie Clicker

The addictive idle game Cookie Clicker just got more idle. Sit back, relax and watch your cookies multiply with this automated program built in Python using the Selenium webdriver module. This version uses the experimental cookie clicker website.

## Dependencies

```sh
pip install selenium
```

## Usage

The program is currently set up to only run for 5 minutes before automatically closing. To change the time modify the number 5 found in this line of code to however long you want to run the program for:
```sh
stop = time.time() + 60*5
```

The upgrades are set up to automatically purchase every 5 seconds until 3 minutes have passes. Once 3 minutes have passed the time until a new upgrade is purchased is increased slightly to allow for the higher value upgrades to be purchased. This can be modified by changing the numbers in these lines of code:
```sh
purchase_time = time.time() + 10 # 5 seconds
increase_purchase = time.time() + 60*3 # 3 minutes
```
