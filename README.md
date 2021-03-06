<p><h1 align="center"><strong>Pet</strong> Paradise</h1></p>


![Portfolio website](/media/website.JPG) 


<br>


[Visit Pet Paradise online here!](https://djpaul-pet-paradise.herokuapp.com/)

<br>

# Intro


<p align="center">This task is the final project for the 'Full Stack Frameworks with Django' module of the Code Institute Full Stack Software Development course. 
This project is an eCommerce shopping website for all things pet related.</p>

<p align="center">The site is worked within Django structure, sent live on Heroku, utilizes AWS S3 to have media and static records. Locally, it utilizes the inherent Django Db.sqlite3 information base, though when conveyed live it uses Heroku's Postgres information base. Authentication functionality is provided by Django's Allauth: Administrators or Superusers can add and alter things in the Products and Categories applications, while visiting clients can register and login, accessing vestige depictions and their request history in the Checkout and Profile applications.</p>


- [User Experience](#userex)
   +  [Goals](#goals)
    + [Target Audience](#target-audience)
    + [Business Goals](#business-goals)
    + [Customer goals](#customer-goals)
- [User Stories](#userstories)
    + [Viewing and Navigation](#viewing-and-navigation)
    + [Registration and User Accounts](#registration-and-user-accounts)
    + [Sorting and searching](#sorting-and-searching)
    + [Admin and Site Management](#admin-and-site-management)
- [Design](#design)
    + [Font](#font)
    + [Color Scheme](#color-scheme)
    + [Wireframes](#wireframes)
    + [Database Relationship Schema](#database-relationship-schema)
- [Testing](#testing)
    + [Product Features](#product-features)
    + [Users Features](#users-features)
- [User Stories Testing](#usertest)
- [Errors & Testing](#test)
- [Deployments](#deployments)
- [Local deployment](#local-deployment)
- [Deployment on Heroku](#deployment-on-heroku)
- [Credits](#credits)
- [Thank You](#thanks)
    

<p id="userex"><h1 align="center"><strong>USER</strong> EXPERIENCE</h1></p>

# Goals

<p>The main goal of Pet Paradise is to sell pet products to pet owners.<br>
   The user can create an account<br>
   The user can shop for products<br>
   The user can safely purchase products online</p>

# Target Audience

- The primary audience are pet owners.
- Users looking to purchase toys for their cats or dogs.
- Users looking to buy fish and bird products.
- Users who would like other products such as food and exercise products for their pets.

# Business Goals

- To create a platform that enables the customers find and purchase pet products.
- Offer a presentable design of website
- Encourage users to register for an account for ease of shopping
- Offer a simple and easy to use and navigate interface to attract the user to return for future visits.

# Customer goals

- Finding items to buy for their pets.
- Buy items through an easy payment flow system.
- Register for an account to make purchasing quicker in future
- See their previous purchases.

 <p id ="userstories"><h1 align="center"><strong>USER</strong> STORIES</h1></p>

### Viewing and Navigation		
- As a shopper I want to be able to view the list of products with the option to purchase them.
- As a shopper I want to be able to view individual product details to identify the price and description.
- As a shopper I want to be able to quickly identify special offers and deals to take advantage of special savings on products I'd like to buy.
- As a shopper I want to be able to easily view the total of my purchases at any time and to see the history of my purchases and how much I spent.

### Registration and User Accounts  
- As a registered shopper I want to be able to easily register for an account so I can have a personal account, be able to see what I purchased.
- As a registered shopper I want to be able to easily login or logout so I can access my personal account information.
- As a registered shopper I want to be able to easily recover my password in case I forget it so I can recover access to my account.
- As a registered shopper I want to be able to receive an email confirmation after registering so I can verify that my account registration was successful.
- As a registered shopper I want to be able to have a personalised user profile so I can view my personal order history and order confirmations and save my payment information.

### Sorting and searching  
- As a shopper I want to be able to sort the list of available products so I can easily identify the best rated, best priced and categorically sorted products.  
- As a shopper I want to be able to sort a specific category of products so I can find best priced or best rated product in a specific category or sort the product in that category by name.
- As a shopper I want to be able to sort multiple categories of products simultaneously so I can find the best priced or best rated product across the board categories.
- As a shopper I want to be able to search for a product by name or description so I can find a specific product I'd like to purchase.

### Purchasing and Checkout  
- As a registered shopper I want to be able to easily select the quantity of a product when purchasing it so I can ensure I am selecting the correct product and the correct quantity.
- As a registered shopper I want to be able to view items in my bag to be purchased so I can identify the total cost of my purchase and all items I will receive.
- As a registered shopper I want to be able to adjust the quantity of individual items in my bag so I can easily make changes to my purchase before checkout.
- As a registered shopper I want to be able to easily enter my payment information so I can check out quickly and without any issues.
- As a registered shopper I want to be able to feel that my personal and payment information is safe and secure so I can confidently provide the needed informatoin to make a purchase.
- As a registered shopper I want to be able to view an order confirmation after checkout so I can verify that I have not made any mistakes.
- As a registered shopper I want to be able to receive an email confirmation after checking out so I can keep the records of my purchases.

### Admin and Site Management  
- As the site owner I want to be able to add a new product as this would enable me to add new items to my site.
- As the site owner I want to be able to Edit/Update a product, to apply any changes, be it in price, description, image or any other criteria.
- As the site owner I want to be able to delete a product and remove a product if they are no longer available.


<p id="design"><h1 align="center"><strong>DES</strong>IGN</h1></p>

## Font

Throughout the project there is only one font used, which is Poppins. The aim is to make this website as minimalist and clean as possible, I used shadows in CSS and HTML to make certain headings stand out more.

## Color Scheme

The main color used throughout the page is pale and light, it's called light slate grey, as this ensures best effectivens of the design style. Black and white is used to highlight titles, headings and general top page information. Other colours used are red, blue and green for hovers, warnings, success messages and small buttons such as edit or remove.

![Colour Chart](/media/colour_chart.JPG) 

## Wireframes
<br>

<details><summary><strong>Mobile, Tablet and Desktop</strong></summary>
<br>
 
## Please click [Pet Paradise Wireframes](https://github.com/DjPaulP/pet_paradise/tree/main/pet_paradise_wireframes)
</details>
<br><br>

## Database Relationship Schema

![Database Relationship Schema](/media/petparadise_schema.png) 

<br><br>

## Technologies
<br>

[![Gitpod](https://img.shields.io/badge/IDE-Gitpod-blue)](https://www.gitpod.io/)<br>
[![CSS](https://img.shields.io/badge/Styling-CSS-blueviolet)](https://www.w3schools.com/css/)<br>
[![AWS Services](https://img.shields.io/badge/AWS%20-Services-orange)](https://aws.amazon.com/)<br>
[![JavaScript](https://img.shields.io/badge/JS%20Functionality-JS-darkgreen)](https://jquery.com/)<br>
[![HTML](https://img.shields.io/badge/Mark%20up%20text-HTML-yellow)](https://www.w3schools.com/html/html_intro.asp)<br>
[![Heroku](https://img.shields.io/badge/App%20Hosting-Heroku-%237B68EE)](https://www.heroku.com/home)<br>
[![Github](https://img.shields.io/badge/Remote%20code-Github-white)](https://github.com/)<br>
[![Balsamiq](https://img.shields.io/badge/Wireframes-Balsamiq-Orange)](https://balsamiq.com/wireframes/)<br>
[![Photoshop](https://img.shields.io/badge/Photoediting-Photoshop-lightblue)](https://www.adobe.com/ie/products/photoshop.html)<br>
[![Django](https://img.shields.io/badge/Microframework-Django-%238B0000)](https://www.djangoproject.com/)<br>
[![Shields](https://img.shields.io/badge/Readme%20Badges-Shields-lightgrey)](https://shields.io/)<br>
[![JShint](https://img.shields.io/badge/JS%2FjQuery%20Validator-JSHint-%23008e94)](https://jshint.com/)<br>
[![SureOak](https://img.shields.io/badge/SureOak-Automated%20Testing-green)](https://www.sureoak.com/)<br>
[![SQlite3](https://img.shields.io/badge/SQLite-Production%20Database-yellowgreen)](https://www.sqlite.org)<br>
[![Bootstrap](https://img.shields.io/badge/Design%20Framework-Bootstrap-%23F5A4A7)](https://getbootstrap.com/)<br>
[![Pep8 Online](https://img.shields.io/badge/Python%20Validator-PEP8%20online-white)](http://pep8online.com/)<br>
[![Python](https://img.shields.io/badge/Back%20end%20programming-Python-%09%23008000)](https://www.python.org/)<br>
[![Schema](https://img.shields.io/badge/DataBase%20Schema%20-App%20Diagrams-lightgrey)](https://app.diagrams.net/)<br>
[![W3C CSS Validator](https://img.shields.io/badge/CSS%20Validator-W3C%20CSS%20Validator-darkred)](https://jigsaw.w3.org/css-validator/)<br>
[![W3C HTML Validator](https://img.shields.io/badge/HTML%20Validator-W3C%20HTML%20Validator-red)](https://validator.w3.org/)<br>

<br><br>

## Features

- Products to purchase through an ecommerce system
- Administration panel so superuser can add, edit and delete products
- Profile page where registered user can see their order purchase history


All pages share navigation bar with logo to the left, which once clicked on, takes you home from any page.<br>
![Database Relationship Schema](/media/logo.JPG) 
<br>

In the middle there are seven call to action buttons:<br>
![Database Relationship Schema](/media/cta_buttons2.JPG) 
<br>
- All Products - Option that returns a dropdown list with Items sorted in accordance to price, rating, category and all products.
- Cat -  Option that returns a dropdown list with all cat Items sorted in accordance to Toys, Food and All Cat products
- Dog -  Option that returns a dropdown list with all dog Items sorted in accordance to Toys, Food, Exercise, Food and All Dog products
- Other -  Option that returns a dropdown list with other Items sorted in accordance to Cages, Tanks, Food and All Other products
- Special Offers -  Option that returns a dropdown list with Items sorted in accordance to New Arrivals, Deals, Clearance and All Specials
- Contact - This opens the contact form for visitors to send messages to the store owner.
- Blog - Useful information for Pet owners and also ability to leave a comment on a blog once the user is logged in
<br>

To the right corner in the Main view there are two CTA buttons: My Account and a Shopping Bag.<br>
![Database Relationship Schema](/media/cta_right.JPG) 
<br>
- My Account:
For the registered and while logged in user that is not a superuser, they will be able to Check out their Profile, which contains history of purchases. By clicking on this option, the logged in user will be able to log out from their session.
For the regisered and logged in as a superuser, the user will be able to do all of the above plus Manage all products of the ecommerce site. 
- Shopping Bag:
This option is available to both logged in and not logged in users. The difference is, only a logged in user will be able to successfully check out with the items, as this option is for the time being only made available to the logged in user.
<br>
- Footer:
At the bottom of the homepage there is a footer with links to social media. This only appears on the homepage as it looks too cluttered on shopping and product pages.<br>
![Database Relationship Schema](/media/footer.JPG)
<br>
## Future Features

- to have a reviews section so users can leave real world experiences of a product.
- to have a sign up page for a newsletter and special offers email.
- to send emails from backend to gmail from contact form

<br><br>

<p id="testing"><h1 align="center"><strong>TEST</strong>ING</h1></p>

![Testing Images](/media/testimages.jpg)

## Product Features
<br>

|  <h2>Feature</h2> |  <h2>Action</h2> | <h2>&nbsp; &nbsp;&nbsp; Effect</h2> |
|---|---|---|
| Logo (upper left corner)  |  Hover over |  <ul><li>The cursor changes to a pointer and returns the homepage</li></ul> |
| Search bar  |  Entered "Rope" |<ul><li> Returned 2 products with Rope in title or description - correct</li><li>The summary shows a message  2 Products found for "rope"</ul>|
|  All Products |  Click on Shop Now |  <ul><li>Linked correctly</li><li>All products showing</li></ul>  |
| All Products  |  Click on By Price |  <ul><li>Items appear sorted ascending, from low price to high</li></ul> |
|   |  Click on By Rating |  <ul><li>Items appear sorted descending, from high rating to low</li></ul> |
|   |  Click on Alphabetically |  <ul><li>Categories of Items become sorted alphabetically</li></ul> |
|   |  Click on All|  <ul><li>All items are displayed, sorted by SKU</li></ul> |
| Categories  |  Click on All Cat |  <ul><li>Products from that Category are displayed, the badge on top of the page also states what Category we are currently in.</li></ul> |
|   |  Click on Cat Toys|  <ul><li>Products from that Category are displayed, the badge on top of the page also states what Category we are currently in.</li></ul>|
|   |  Click on Cat Food |  <ul><li>Products from that Category are displayed, the badge on top of the page also states what Category we are currently in.</li></ul>|
|   |  Click on All Dog |  <ul><li>Products from that Category are displayed, the badge on top of the page also states what Category we are currently in.</li></ul> |
|   |  Click on Dog Food |  <ul><li>Producst from that Category are displayed, the badge on top of the page also states what Category we are currently in.</li></ul> |
|   |  Click on Dog Exercise |  <ul><li>Products from that Category are displayed, the badge on top of the page also states what Category we are currently in.</li></ul> |
|   |  Click on Other Cages |  <ul><li>Producst from that Category are displayed, the badge on top of the page also states what Category we are currently in.</li></ul> |
|   |  Click on Other Tanks |  <ul><li>Producst from that Category are displayed, the badge on top of the page also states what Category we are currently in.</li></ul> |
|   |  Click on Other Food |  <ul><li>Producst from that Category are displayed, the badge on top of the page also states what Category we are currently in.</li></ul> |
|   |  Click on All Other| <ul><li>All Other Products are displaying</li></ul> |
| Special Offers     |  Click on Recently Added |  <ul><li>New products are displayed, the badge on top of the page states same.</li></ul> |
|   |  Click on Deals |  <ul><li>Special Offers are displayed, along with badge</li></ul> |
|   |  Click on Clearance |  <ul><li>Clearance Offers are displayed, along with badge</li></ul> |
| My Account  |  Click on Register |  <ul><li>Sign up form appears</li><li>Form sends</li><li>Confirmation email appears in the email box</li><li>Clicked on the confirmation email - Confirm email address page appears</li><li>Logged in with newly created account - the success message appears and I am now logged in</li><li>Upon clicking Confirm, a success message appears and a signing page is returned</li></ul> |
|   |  Click on Login |  <ul><li>The address on hover is showing as home page</li></ul> |
| Bag  |  Bag empty |  <ul><li>Click on Continue Browsing button, brings me back to all Products page</li></ul> |
|   |  Bag with Content | <ul><li>Increase and Decrease quantity buttons work</li><li>Price updates when Update option is clicked</li><li>Price in Grand total Updates over the 10% Delivery</li><li>Free Delivery threshold is calculated correctly and called back to user</li></ul> |
| | <h3>Home Page</h3> | |
| Explore Shop Now button  |  Clicked on |  <ul><li>Brings me to a page with all products</li></ul> |
| | <h3>All Products Page</h3>  | |
| Options Dropdown  |  Sort testing each Condition |  <ul><li>Price (low to high) - sorts according to price, from cheapest to dearest</li><li> Price (high to low) - sorts according to price, from dearest to cheapest</li><li>Rating (low to high) - sorts rating from lowest</li><li>Rating (high to low) - sorts rating from highest.</li><li>Name (A-Z) - sorts Products alphabetically</li><li>Name (Z-A) - sorts products reverse-alphabetically</li><li>Category (A-Z) - sorts Categories of products alphabetically</li><li>Category (Z-A) - sorts Products by Categories sorted reverse-alphabetically</li></ul> |
| Superuser - editing the creation details  |  Click on the Edit option underneath one of the products |  <ul><li>A Manage Products Edit a Product form is rendered and a warning message is triggered in upper right corner</li><li>Changed Category and Name,saved</li><li>Name and Category successfully changed, confirmed with a success toast rendered in upper right corner </li></ul> |
|   |  Click on the Delete option |  <ul><li>Product is immediately deleted and a success toast confirming deletion is rendered in the upper right corner of the page </li></ul>|
| Adding a Product to the bag  |  Click on the Product and click Add to Bag |  <ul><li>Bag total updates to the correct amount, success toast confirms the Creation was added to the bag </li></ul> |
| Navigating from Product Detail back to All Products |  Click on the Continue Browsing button |  <ul><li>A page with all the Products is rendered</li></ul> |
| Checking Out |  Click on the Shopping Bag, click on Secure Checkout |  <ul><li>Non registered user - a sign in page renders with option to register, if user is not yet registered</li><li>Registered User - A Checkout page is rendered with most information saved as per users account. User can also see the Order Summary to the right of the form</li><li>Entered card details and name, after which clicked on the Complete Transaction button</li><li>A thank you page is rendered, with a summary of order as well as the success toast renders in upper right corner</li><li>Confirmation email arrives to the email box</li></ul> |
| Contact  |  Click on the Contact form |  <ul><li>Opens the contact form</li><li>Users input their details and message</li><li>Send message to the backend</li><li>All works as intended</li></ul> |
| Blog  |  Click on Blog Posts |  <ul><li>Opens the Blogs short view page</li><li>Clicking on a blog opens the full blog</li><li>Logged in users can leave a comment on the blog</li><li>All works as intended</li></ul> |

### For testing the Stripe checkout use the following:

```bash
 Card number: 4242 4242 4242 4242
 CVC_: any 3 digits
 Card expiry date: any future date
 ZIP/Postcode: any 5 digits
``` 



![Checkout Success Images](/media/responsive.JPG)

<br>

# Users Features

|  <h2>Feature</h2> |  <h2>Action</h2> | <h2>&nbsp; &nbsp;&nbsp; Effect</h2> |
|---|---|---|
| Registration  | Click on My Account and My Profile  |  <ul><li>Click on MyAccount and Register</li><li>A Sign Up form is rendered, fill in the blanks</li><li>User Exists - an error is rendered above the user name "User is already registered with this email address"</li><li>Register unregistered email address, press send</li><li>A confirmation email is sent to the provided email address</li></ul> |
| Login  |  Click on My Account and My Profile | <ul><li>Click on My Account and Login</li><li>A Sign In form renders</li><li>Wrong Password entered, an error is generated "The username and/or password you specified are not correct"</li><li>Log in with the correct password</li><li>Home page is rendered</li></ul>  |
| Logout  | Click on My Account and My Profile  | <ul><li>Click on MyAccount and Logout</li><li>A page renders confirming "Are you sure you want to sign out"</li><li>Click Sign Out</li><li>A success toast is rendered in upper right corner of the screen</li></ul>  |
| Change Password  |  Click on My Account and My Profile |  <ul><li>Click on MyAccount and Login</li><li>Click Forgot Password</li><li>Enter email you are registered under</li><li>A page renders confirmation "We have sent you an email. Please contact us if you do not receive it within a few minutes"</li><li>When clicked, it returns a change password form</li></ul> |
| View profile  |  Click on My Account and My Profile | <ul><li>Log in and click on MyAccount and My Profile</li><li>My Profile page is rendered with Default Delivery Informaton and history of purchasees</li></ul> |
| Update profile  |  Click on My Account and My Profile |  <ul><li>While in My Profile, fill in the new details and click Update Information</li><li>A success toast is rendered in upper right corner of the screen</li><li>Information is updated</li></ul> |

<p id="usertest"><h1 align="center"><strong>USER</strong> STORIES TESTING</h1></p>

 | <h2>User Story</h2>                                                                                                                                                                                  | <h2>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Testing<h2>                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| As a shopper I want to be able to view the list of products to purchase                                                                                                                 | <ul><li>The list of products is available as per below</li><li>Home page - click on Shop Now button  - choose the desired filtering or choose 'All Products'.</li></ul>                                                                                                                                                                                                                                                               |
| As a shopper I want to be able to view individual product details to identify the price and description.                                                                                      | <ul><li>While at All products click on a sample product</li><li>The Price and Description is clearly visible.</li></ul>                                                                                                                                                                                                                                                                                                                      |
| As a shopper I want to be able to quickly identify new special offers to take advantage of special savings on products I'd like to buy.                                                           | <ul><li>One of the CTA buttons on navbar is marked as Special offers and is visible from every page of the website.</li></ul>                                                                                                                                                                                                                                                                                                                |
| As a shopper I want to be able to easily view the total of my purchases at any time to see the history of my purchases and how much I spent.                                                  | <ul><li>This feature can be accessed on My Account -> My Profile</li><li>History of orders is visible next to the profile details.</li></ul>                                                                                                                                                                                                                                                                                                 |
| As a registered shopper I want to be able to easily register for an account so I can have a personal account, be able to see what I purchased.                                                | <ul><li>As soon as the unregistered user is ready to check out and complete a purchase, the site renders a Sign Up call to action page.</li><li>By clicking on My Account and Register, the unregistered user may easily register and from then on use their account to keep a record of their purchases.</li></ul>                                                                                                                                   |
| As a registered shopper I want to be able to easily login so I can access my personal account information.                                                                                    | <ul><li>By clicking on My Account, users acount is easily accessible and editable.</li></ul>                                                                                                                                                                                                                                                                                                                                                |
| As a registered shopper I want to be able to easily recover my password in case I forget it so I can recover access to my account.                                                            | <ul><li>Upon login attempt there is a 'Forgot Password' option</li><li>From there on, the user may request a password resetting email.</li><li>Upon receipt of the email, user will be able to click on the link and easily amend or set a new password.</li></ul>                                                                                                                                                                            |
| As a registered shopper I want to be able to receive an email confirmation after registering so I can verify that my account registration was successful.                                     | <ul><li>Shortly after registration, a confirmation email arrives to the inbox of the email provided.</li></ul>                                                                                                                                                                                                                                                                                                                               |
| As a registered shopper I want to be able to have a personalised user profile so I can view my personal order history and order confirmations and save my payment information.                | <ul><li>The profile can be accessed through My Account button in upper right corner of the page.</li></ul>                                                                                                                                                                                                                                                                                                                     |                            
| As a shopper I want to be able to sort the list of available products so I can easily identify the best rated, best priced and categorically sorted products.                                 | <ul><li>This option is available by accessing 'All Products' option within the navbar.</li></ul>                                                                                                                                                                                                                                                                                                                                               |
| As a shopper I want to be able to sort a specific category of products so I can find best priced or best rated creation in a specific category or sort the product in that category by name.   | <ul><li>The sorting option is available on every page in a format of a dropdown.</li></ul>                                                                                                                                                                                                                                                                                                                                                  |
| As a shopper I want to be able to sort multiple categories of products simultaneously so I can find the best priced or best rated products across the board of categories, such as Cat or Dog. | <ul><li>By clicking on All Products, the user may choose from all products. </li><li>Additionally there are badges displayed on top of the page, to inform what categories are being displayed.</li></ul>                                                                                                                                                                                                  |
| As a shopper I want to be able to search for a product by name or description so I can find a specific product I'd like to purchase.                                                          | <ul><li>The option of a Search bar is available at all times, it returns key words by the products name or from within a products description.</li></ul>                                                                                                                                                                                                                                                                                      |
| As a registered shopper I want to be able to easily select the quantity of a product when purchasing it so I can ensure I am selecting the correct product and a correct quantity.                    | <ul><li>While adding a product to the bag, the user chooses the quantity of the product.</li><li>While in the bag, and preparing for check out, the user can edit the quantity or delete the product entirely by clicking remove.</li></ul>                                                                                                                                                                                                |
| As a registered shopper I want to be able to view items in my bag to be purchased so I can identify the total cost of my purchases and all items I will receive.                               | <ul><li>The current total is constantly displayed in upper right corner, under the bag icon.</li></ul>                                                                                                                                                                                                                                                                                                                                            |
| As a registered shopper I want to be able to adjust the quantity of individual items in my bag so I can easily make changes to my purchase before checkout.                                   | <ul><li>The quantity can be amended when user is in the bag, preparing for check out.</li></ul>                                                                                                                                                                                                                                                                                                                                           |
| As a registered shopper I want to be able to easily enter my payment information so I can check out quickly and with no hassle.                                                               | <ul><li>The payment details are entered after clicking Check out.</li></ul>                                                                                                                                                                                                                                                                                                                                                                  |
| As a registered shopper I want to be able to feel that my personal and payment information is safe and secure so I can confidently provide the needed informatoin to make a purchase.         | <ul><li>The Check out is only possible if the user is logged in. This way users details, if they choose to save them, are securely stored.</li></ul>                                                                                                                                                                                                                                                                                        |
| As a registered shopper I want to be able to view an order confirmation after checkout so I can verify that I have not made any mistakes.                                                     | <ul><li>The order confirmation is displayed as well as emailed to the email address provided.</li></ul>                                                                                                                                                                                                                                                                                                                                      |
| As a registered shopper I want to be able to receive an email confirmation after checking out so I can keep the records of my purchases.                                                      | <ul><li>Email confirmation is sent instantanously after the products are purchased.</li></ul>                                                                                                                                                                                                                                                                                                                                           |
| As a store owner I want to be able to add a product as this would enable me to add new items to my store.                                                                                     | <ul><li>This option is available to the superuser and while logged in.</li><li>Choose My Account and Manage Products.</li><li>This will render a product management form.</li></ul>                                                                                                                                                                                                                                                             |
| As a store owner I want to be able to Edit/Update a product and to apply any changes, be it in price, description, image or other product criteria.                                                 | <ul><li>While logged in as a superuser, go to the product in question and click edit button on all products view or on a product detail page.</li><li>From there, enter any details you want to change, including images.</li><li>Upon submitting, a success toast appears.</li></ul>                                                                                                                                                         |
| As a store owner I want to be able to delete a product and remove a product if they are no longer for sale.                                                                                         | <ul><li>Whle logged in as a superuser, click on Delete option under the product that needs to be deleted</li><li>A success toast appears and the product is gone from the system.</li></ul>                                                                                                                                                                                                                                                         |
<br>

<p id="test"><h1 align="center"><strong>ERRORS &</strong> TESTING</h1></p>

### Please click  [HERE](https://github.com/DjPaulP/pet_paradise/blob/main/test.md) to guide you to a TEST MD file that has validation, testing and performance in greater detail

#
## Requirements

 - an IDE such as GitPod or Visual Studio Code - I used GitPod
 - [PIP](https://pip.pypa.io/en/stable/installing/) to install packages in Python
 - [python 3](https://www.python.org/downloads/) programming language used on the back-end
 - [git](https://git-scm.com/) version control system for code source
 - [stripe](https://stripe.com/) create an account for online payments
 - [AWS](https://aws.amazon.com/) cloud storage service for online backup of website assets. (Create an S3 bucket)


## Local deployment
1. Save a copy of the github repository at https://github.com/DjPaulP/pet_paradise by clicking the 'download.zip'
button at the top of the page and extracting the zip file, or you clone the repository with this command:
   ```
   $ git clone https://github.com/DjPaulP/pet_paradise
   ```
1. Copy the repository into your IDE.
1. Install all required modules with the command:
   ```
   pip3 install -r requirements.txt
   ```

1. Store your environment variables and save them in the 'Environment Variables'-Settings in your IDE:

    ```bash
    'DEVELOPMENT', 'True'
    'SECRET_KEY', '<your value>'
    'STRIPE_PUBLIC_KEY', '<your value>'
    'STRIPE_SECRET_KEY', '<your value>'
    'STRIPE_WH_SECRET', '<your value>'
    ```
1. Replace <your value> with the values from your own accounts
    - The SECRET KEY: you can get from a free Django Secret Key Generator
    - STRIPE_PUBLIC_KEY and STRIPE_SECRET_KEY: from Developer's API on the Stripe dashboard
    - STRIPE_WH_SECRET: from Stripe's developer API after creating a webhook
     
1. Set up the local database by running these two commands:
    ```bash
    python3 manage.py makemigrations
    python3 manage.py migrate
    ```
   
1. Create a superuser for the database, in order to access Django's admin-panel
    ```bash
    python3 manage.py createsuperuser
    ```

1. Start your server by running the following management command in your terminal:
    ```bash
    python3 manage.py runserver
    ```


## Deployment on Heroku

1. Go to https://heroku.com/ and create a new app with a unique name
1. Provision the Postgres database: Go to the Resources tab and install the addon "Heroku Postgres". Heroku automatically adds
the 'DATABASE_URL' to the Config Vars.
1. Go to the Settings tab, click Reveal Config Vars and copy the DATABASE_URL value into your local memory.
1. In your App on Heroku, go to the Settings tab, and click on 'Reveal Config Vars', set these variables:
    
    ```bash
    'AWS_ACCESS_KEY_ID', '<your value>'
    'AWS_SECRET_ACCESS_KEY', '<your value>'
    'DATABASE_URL', '<your value>'
    'SECRET_KEY', '<your value>'
    'STRIPE_PUBLIC_KEY', '<your value>'
    'STRIPE_SECRET_KEY', '<your value>'
    'STRIPE_WH_SECRET', '<your value>'
    'USE_AWS', 'True'
    ```

1. Migrate the database:
    ```bash
    python3 manage.py makemigrations
    python3 manage.py migrate
    ```
1. Create a superuser for the database, to access Django's admin panel:
    ```
    python3 manage.py createsuperuser
    ```
1. If any packages have been updated, make a new requirements.txt file: 
    ```
    pip freeze > requirements.txt
    ```
1. Create a new file named Procfile with no file extension, add web: python app.py to the file and save
1. push files that were changed to Github:
    ```bash
   git add .
   git commit -m "..."
   git push
   ``` 
1. Go back to the Heroku, open your app and go to the Deploy tab. Choose a Deployment method, I deployed mine through GitHub.
1. By choosing Github as a deployment method, you have to enter your Github link and choose <strong>Automatic Deployments.</strong> This will enable every commit to push directly to Heroku.
<br>

<p id="credits"><h1 align="center"><strong>CRE</strong>DITS</h1></p>
<br>

The inspiration for the website was mainly taken from the Coding Institute lectures presented by Chris Zielinski. 
Below are other resources I used while building the project:

1. [BezeBee for ReadMe inspiration](https://github.com/bezebee)
2. [Dylan Shine for exceptional inspiration and help through out the year ](https://github.com/DylanThomasShine/)
3. [Code Institute Support team](https://learn.codeinstitute.net/ci_support/diplomainsoftwaredevelopment/support)
4. [Slack](https://slack.com/intl/en-ie/)
5. [Codewithstein for inspiration with contact and blog apps](https://www.youtube.com/channel/UCfVoYvY8BfTDeF63JQmQJvg)

<strong>Johann & Rebecca</strong> in Code Institute for their help online<br>
<strong>All tutors</strong> in Code Institute who took the time to help and guide me<br>
<strong>Precious Ijege</strong> my mentor, for all the advice and feedback. It was invaluable<br>


### All images for the store poducts were taken from amazon (https://amazon.co.uk)

<br>

[Visit Pet Paradise online here!](https://djpaul-pet-paradise.herokuapp.com/)

<br>

<p id="thanks"><h1 align="center"><strong>THANK</strong> YOU</h1></p>
<p><h1 align="center">for<strong> browsing</strong> my <strong>README</strong> file.....</h1></p>