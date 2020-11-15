# Connect@Random
Read as CSV file containing email addresses and distributes them into spaces at random, of a fixed size.

## How to run
First create a bot (here)[https://developer.webex.com/] and copy the Bot access token into a `.env` file that is located somewhere in your root directory. Make sure you have a CSV file with email addresses in the first column read, place it as `sample.csv`, then run
```pip3 install -r requirements.txt```
and now you are ready to use the Webex Bot API to automatically create Spaces (aka Rooms) of a size of n people by using:
```python -f sample.csv -n 7```


