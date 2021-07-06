<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
-->



<!--  -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
<!--
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]
-->


<!-- PROJECT LOGO -->
<br />
<p align="center">
  </a>


  <h1 align="center">Stock Market Price Tracking cum Alert System</h1>


  <p align="center">
    This is a useful stock market tracker system , where you can monitor the stock prices and set up the threshold values for various companies depending on which 
    you can buy or sell stocks. !!!!! 
  </p>
</p>

![Screenshot (203)](https://user-images.githubusercontent.com/75406889/124596596-17b74900-de80-11eb-88f0-bd688a2ccca2.png)

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#pricetrackerpy">PriceTracker.py</a>
    </li>
    <li>
      <a href="#priceplotterpy">PricePlotter.py</a>
    </li>
    <!--
    <li><a href="#acknowledgements">Acknowledgements</a></li>
    -->
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This is a python based stock market price monitoring system that tracks the price variation of various companies , and sends alert to the user when the price falls below or exceeds a certain threshold. This system can be extremely useful to a trader who wants to buy or sell stocks.

<!--PriceTracker.py-->
## PriceTracker.py
This is a python code to extract real time stock price data from Yahoo Finance using Selenium and BeautifulSoup libraries . Firstly the user is required to give the code of the companies to track and a threshold value. Then depending on whether the trader wants to buy or sell stocks , if the current stock price falls below the threshold price (when he wants to buy stocks ) or the current stock price exceeds the threshold price (when he wants to sell stocks) , an email notification is sent to the trader's gmail account. This is achieved using the smptlib and ssl libraries.
![Screenshot (204)](https://user-images.githubusercontent.com/75406889/124605333-6c12f680-de89-11eb-8105-c9a813c7e44a.png)

## PricePlotter.py
This file plots the real time stocks price against their current time instant. This helps to visulaize how the stock price varies for a company , that gives better insight to the trader who wants to invest in that company.
![Screenshot (205)](https://user-images.githubusercontent.com/75406889/124605334-6c12f680-de89-11eb-8ce6-3c6c110ca589.png)


<!-- CONTRIBUTING 
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

-->

<!-- LICENSE 
## License

Distributed under the MIT License. See `LICENSE` for more information.

-->

<!-- CONTACT 
## Contact

Your Name - [@your_twitter](https://twitter.com/your_username) - email@example.com

Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name)
-->


<!-- ACKNOWLEDGEMENTS 
## Acknowledgements
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Img Shields](https://shields.io)
* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Pages](https://pages.github.com)
* [Animate.css](https://daneden.github.io/animate.css)
* [Loaders.css](https://connoratherton.com/loaders)
* [Slick Carousel](https://kenwheeler.github.io/slick)
* [Smooth Scroll](https://github.com/cferdinandi/smooth-scroll)
* [Sticky Kit](http://leafo.net/sticky-kit)
* [JVectorMap](http://jvectormap.com)
* [Font Awesome](https://fontawesome.com)

-->



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
