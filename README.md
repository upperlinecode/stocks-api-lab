# Stock Explorer

Now that you've had some practice with functions, dictionaries, and lists, it's time to put them all together and start writing some code that might be useful if you decide to pursue a FinTech career.

#### The Goal

We're going to build an stock market simulator! This application will eventually give a user an opportunity to role-play a decade as an investor. They'll start the decade off with $10,000, and be offered choices about how to manage their money over time.

That version will take some time, and when you're building something complicated, one strategy is to start with the hardest part first - in this case, that's going to be accessing all stock prices for some certain companies over an entire decade.

* If you wanted to look up one stock price on a certain day, you could just search that up and copy the price over into your code.
* If you needed to copy over 10 prices for your application to work, that could start to feel tedious.
* If you needed an entire decade of stock prices copied over into your application, you might start to feel like you were doing busywork, even if it were just for one single company. 
* If you had do it for 10, 20, or 100 companies, you'll probably start to feel like there has to be a better way, and luckily for you, there is!

That's where APIs come in. An API (Application Program Interface) allows two different applications to interact. For our purposes today, this means that our program (which needs to know stock prices) will interface with a service someone _else_ made (which essentially answers questions about stock prices).

APIs are especially useful any time your application needs to access already-existing knowledge. Especially if you think to yourself "surely there's a record of this somewhere..." there probably is!

Some APIs are totally free and open, supported through donations or government and company initiatives. Most others require you to sign up and pay a fee to support all the work that goes into keeping those records up-to-date. When you sign up and pay a fee, you'll receive some credentials (usually an API key, which functions like a password you add to the address of your request or question) so that the API knows you've paid for the information you're accessing.

Luckily, a lot of those paid APIs are easy to sign up for and have a free tier you can use while you're just learning, and that's what we'll do today.

**Note that this is a STRETCH lab, which means that most participants will only get through level 1 and maybe level 2 in a normal block of lab time.**

## Environment Setup

In order for this application to work, you may need a few things:

1. A program that will "get" the quiz question. In other words, if we think of the url (the 'link') as an address, we need a way to go get the data waiting for us at that address. We will use a python library called "Requests."
2. An API key that lets the server know we're authorized to access the information we're requestiong.

#### 1. Install a requests handler

**This is pre-installed on Replit. If you're using Replit, skip this step.**

To install Requests, type the following into the console:

```bash
pip3 install requests
```

We also need to tell the Python program to actually USE the library we just installed. That's why line 1 of `stocks.py` looks like this:

```Python
import requests
```

#### 2. Sign up for an API key

Before you can use an API, you have to sign up for the service. We'll be using the free tier of a service called [Polygon](https://polygon.io/). To make things quick and easy, you're encouraged to sign up with your GitHub account.

To find your API key after you've signed up, go to your [Dashboard](https://polygon.io/dashboard/api-keys) and you should see a default key listed. Add this key into the empty string `my_api_key` where indicated in the `stocks.py` file

## API Basics

We're going to use an api called [Polygon](https://polygon.io/), which has some incredible interactive documentation. While you can still access your API key in the menu on the left at any time, you'll find that it's also embedded into the examples in their [documentation](https://polygon.io/docs/stocks/get_v1_open-close__stocksticker___date).

## The Challenges

Before starting, and before even running the script for the first time, you may want to read the request that's listed there - can you figure out which company it's accessing prices for? Can you tell what day in history it's requesting the data for?

Then go ahead and run the program and read the response that gets printed. What was the opening price for that stock that day? What was the closing price? What was the highest price? What was the lowest?

#### LEVEL 1: Parsing the Response

1. Print out the opening price.

2. Print out the closing price.

3. Find the HML (high minus low) indicator by subtracting the lowest price from the highest and printing it out.

4. If someone owned 10 shares of this stock, how much would their investment have grown or depreciated between open and close? Find that number and print it out.

5. What percentage did the stock price increase or decrease by? Find that percentage and print it out.

6. Write a function that takes in the entire dictionary of the response from our API call, and prints out a readable summary like this one:

```
Symbol: AAPL
Open: 121
Close: 121.19
Change: +0.19 or 0.15%
```

#### LEVEL 2: Changing the Request

To complete the level 2 challenges, you'll need to write new requests, mirroring line 4. You can start numbering each variable to keep them organized (like `request2` etc.) or you could just name things a bit more precisely - how you name the variables won't change the responses you get.

7. Using the function from earlier, print out summaries for the following companies:

- Companies
- To
- Be
- Determined
- By
- Citadel

8. Using your function from earlier, print out 12 summaries for [COMPANY_NAME] for the first of every month in the year 2020.

#### LEVEL 3: Changing the Endpoint

So far we've only use one URL format to request data. This specific format is called an endpoint, and it's defined really clearly in their documentation. The one we've used so far is called ["Daily Open / Close"](https://polygon.io/docs/stocks/get_v1_open-close__stocksticker___date) and it gives us data about a single company on a single day.

The [Aggregate (Bars)](https://polygon.io/docs/stocks/get_v2_aggs_ticker__stocksticker__range__multiplier___timespan___from___to) endpoint lets you look at the data you could use to generate a bar graph (or any graph, really) and group data about a company over time into time intervals of various sizes - that means you can look at daily reports for a quick snapshot, or introduce some level of smoothing if you want to look at long-term trends.

###### NOTE: since the API we're using only allows 5 requests per minute from a free account, you may find you need to comment out earlier requests before making new ones - otherwise it makes every request in the script each time you run it.

8. Access the data for [COMPANY_NAME] for the first 7 days of March 2020. Print out the highest opening price.

9. Print out monthly data for all of 2020. Which month was the best month for [COMPANY_NAME] and how did you determine that?

10. Print out yearly data for the 2010s decade (2010 - 2019) - Which year would have the highest payout if you bought $10,000 worth of stock on January 1 and sold it on December 31?

#### LEVEL 4: Build the Simulator

Level 4 is much more unstructured. Instead of breaking down specific tasks, it's going to ask you to envision certain versions of a simulation or a game. This is just a basic interactive command line application, like Oregon Trail, except set in more recent times, and with a more financial focus.

The [MVP](https://www.productplan.com/glossary/minimum-viable-product/): Start on January 1, 2010. Offer the user $10,000 and a single company to invest some, none, or all of it in. For each "turn" in the simulation, advance forward 1 year. Then let them know how their investment has done, and allow the to buy more, sell more, or leave things as is. Also give them $2,000 additional dollars to invest that they've saved up over the course of the year. At the end of 10 turns (10 years), their score is the total value of their investments.

One the MVP is done, you can implement any of the following improvements to refine the game to your tastes.

- Allow the user to choose how far they want to advance (e.g. 1 week, 1 month, 3 months, or 1 year) at each turn, instead of locking them into a year.
- Allow the user a choice of 3-5 companies instead of just 1.
- Allow the user to choose their decade (the 80's, the 90's, the 00's, or the 10's).
- Allow the user to buy into an index fund or a mutual fund of your design instead. If these terms are unfamiliar to you, you will need to look them up before trying to create them.
