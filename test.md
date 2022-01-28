<p><h1 align="center"><strong>Pet</strong> Paradise</h1></p>

<br>

![Portfolio website](/media/website.JPG) 

<br>

 <p><h1 align="center"><strong>TEST</strong> FILES</h1></p>                                                                                                                                                                                

![User Story image](/media/testimages2.jpg)

<br>

<p><h1 align="center"><strong>ERR</strong>ORS</h1></p>

| <h2>Error</h2> | <h2>Resolve</h2>                                                                                                                |
|-------|--------------------------------------------------------------------------------------------------------------------------|
| Region error when deploying to heroku  | Region was inputted incorrectly in settings.py |
|![Region Error](/media/region_error.png)|![Region Resolve](/media/region_resolve.png) |
| Webhook not receiving for local server | Created a new endpoint and deleted older one
|![Local webhook Fail](/media/local_fail.png) | ![Local Webhook Resolve](/media/local_success.PNG)
<br>

<p><h1 align="center"><strong>PERFORMANCE</strong> TESTING</h1></p>

I used Sureoak to check the performance of the site and although it is not perfect it is my intent to make it so and I did not have the time as I found out too late about these programs that were available.<br> [![SureOak](https://img.shields.io/badge/SureOak-Automated%20Testing-green)](https://www.sureoak.com/)<br>

<br>

![Validation Results](/media/performance_results.jpg)


# <strong>Validation</strong> Testing

When testing for html it contained duplicate id's i resolved this issue and also type for javascript was not required and the site passes the HTML Validator as shown. 
![HTML Validator](/media/htmlval.JPG)
<br>

## <strong>Line</strong> too long

<br>

 In order to resolve these errors and in my research to find out how, I found they are classed as a style error and does not affect the code performance. I chose to use the comment <strong>#noqa</strong> only in places where a line break \ didn't work and began to mess up the code  and I dealt with any other errors that arose, from trailing white lines to indents and so on.
<br><br>

## <strong>E6</strong> Syntax

<br>

<strong>Template literal syntax’ is only available in ES6 (use ‘esversion: 6’). (W119)jshint(W119).</strong>
This is a fix I could have applied but to be honest I was nervous to try it and the code didn't have any errors other than this and even though it is an error it DID NOT affect the code or the performance of the site in any way. A way to fix this was to:-<br> Add a file named <strong>.jshintrc</strong> to the project and inside this file type:- <strong>{"esversion": 6}</strong>

<p id="userex"><h1 align="center"><strong>VALIDATION</strong> RESULTS</h1></p>

<br>
<details><summary><strong>BAG</strong> APP</summary>
<br>

![Validation Results](/media/bag1.JPG)</details>
![Validation Results](/media/bag2.JPG)</details>
![Validation Results](/media/bag3.JPG)</details><br>
This is the result of the models.py file in the bag app. It's showing a continuation error which was rectified and also lines too long errors which do not affect the result of the app and it functions as intended. If I had more time I would go back and fix all of this. <br>
![Validation Results](/media/bag4.JPG)</details>

<br>
<details><summary><strong>Checkout App</strong> APP</summary>
<br>

![Validation Results](/media/checkout1.JPG)</details> 
![Validation Results](/media/checkout2.JPG)</details>
<br>As above all files are working as intended but just showing the line lenght errors again. When I have more time I will fix these minor errors.

<br>
<details><summary><strong>Home</strong> APP</summary>
<br>

![Validation Results](/media/home1.JPG)</details>

<br>
<details><summary><strong>Pet Paradise</strong> APP</summary>
<br>

![Validation Results](/media/petpara1.JPG)</details>
<br>As above all files are working as intended but just showing the line lenght errors again. When I have more time I will fix these minor errors.

<br>
<details><summary><strong>PRODUCTS</strong> APP</summary>
<br>

![Validation Results](/media/productsforms1.JPG)</details> 

<br>
<details><summary><strong>PROFILES</strong> APP</summary>
<br>

![Validation Results](/media/productsforms2.JPG)</details> 

<br>
<details><summary><strong>STATIC</strong> CSS</summary>
<br>

![Validation Results](/media/css.JPG)</details> 

<br>
<details><summary><strong>TEMPLATES/ALLAUTH/INCLUDES</strong> HTML</summary>
<br>

![Validation Results](/media/templates_results.jpg)</details> 

<br>
<details><summary><strong>MANAGE</strong> .PY</summary>
<br>

![Validation Results](/media/managepy.JPG)</details> 
<br>

<br>
<details><summary><strong>Blog</strong> app</summary>
<br>

![Validation Results](/media/blogapp.JPG)</details> 
<br>

<br>
<details><summary><strong>Contact</strong> app</summary>
<br>

![Validation Results](/media/contactapp.JPG)</details> 
<br>

<br>
<details><summary><strong>SCREEN SIZE</strong> RESPONSIVNESS</summary>
<br>

![Validation Results](/media/responsive.JPG)</details> 
<br><br>

<p id="thanks"><h1 align="center"><strong>THANK</strong> YOU</h1></p>
<p><h1 align="center">for<strong> browsing</strong> my <strong>TEST</strong> file.....</h1></p>

## Please click  [HERE](https://github.com/DjPaulP/pet_paradise/blob/main/README.md) to bring you back to the README file.