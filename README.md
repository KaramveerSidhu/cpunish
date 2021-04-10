<h1 align="center">Welcome to cpunish 👋</h1>
<p>
</p>

A simple python script to punish credit card scammers

### 🏠 [Homepage](https://github.com/KaramveerSidhu/cpunish)

## How does it work?

When you visit a website that you are able to identify as a scam, they usually ask you for your credit card details. They may use these details in a number of ways to harm you. An example scam website would be a website that says you have won a ps5 from Amazon and the URL is entirely different from that of Amazon. Now, once you enter your credit card details, it is validated if it's true or fake. If the credit card is declined, most of the payment gateways usually charge a very small fee. Now since we are dealing with scammers here, with the help of this script we send them multiple credit card validation requests, and since our credit card will be declined, they will be charged by their payment gateway provider which will teach them a good lesson. 

## Requirements
- [Python](https://www.python.org/). Python is an interpreted, high-level and general-purpose programming language. 
- [requests](https://pypi.org/project/requests/) module. You may install it using
```sh
python -m pip install requests
```


## Using the script
**_NOTE:_** You can use the Google Chrome developer tools to find the required information about the request needed to be sent. 

- Copy/ download the script on your local development environment.
- Enter the URL to which the request is being made in the 'requestUrl' variable.
<p align="center">
  <img src = "https://user-images.githubusercontent.com/51775341/114270289-27fa8c00-9a29-11eb-96f9-a1ecd79e5179.png">
</p>

- Check the type of data the request requires frome the Google Chrome developer tools by making a sample request. Copy that data in the data object.
<p align="center">
  <img src = "https://user-images.githubusercontent.com/51775341/114270304-3c3e8900-9a29-11eb-8b36-94f7fb80ac57.png">
</p>

- Run the script using

```sh
python cpunish.py
```
- Use Ctrl+C to stop the script once you feel enough requests have been sent. 

## Author

👤 **Karamveer Singh Sidhu**

* Website: https://karamveer.netlify.app/
* Github: [@KaramveerSidhu](https://github.com/KaramveerSidhu)
* LinkedIn: [@karamveersidhu](https://linkedin.com/in/karamveersidhu)

## 🤝 Contributing

Contributions, issues and feature requests are welcome!<br />Feel free to check [issues page](https://github.com/KaramveerSidhu/cpunish/issues). 

## Show your support

Give a ⭐️ if this project helped you!

***
