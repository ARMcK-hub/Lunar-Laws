
<!-- 
README Template Author: otheneildrew
Template Source: https://github.com/othneildrew/Best-README-Template
Version Author: Drew McKinney
 -->





<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
![GitHub last commit](https://img.shields.io/github/last-commit/ARMcK-hub/Lunar-Laws)
[![MIT License][license-shield]][license-url]
![GitHub top language](https://img.shields.io/github/languages/top/ARMcK-hub/Lunar-Laws)
![GitHub repo size](https://img.shields.io/github/repo-size/ARMcK-hub/Lunar-Laws)
![Website](https://img.shields.io/website?down_color=lightgrey&down_message=offline&up_color=blue&up_message=online&url=https%3A%2F%2Fwestendfinancial.herokuapp.com%2F)

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/ARMcK-hub/Lunar-Laws">
    <img src="https://images.tweaktown.com/news/6/8/68482_01_crime-increase-moon-full.jpg" alt="Logo" width="100" height="100">
  </a>

  <h3 align="center">Lunar Laws</h3>

  <p align="center">
    From St. Louis to You
    <br />
    <a href="https://github.com/ARMcK-hub/Lunar-Laws" target="_blank"><strong> >> Visit Demo >> </strong></a>
    <br />
    <a href="https://github.com/ARMcK-hub/Lunar-Laws/issues">Report Bug</a>
    -
    <a href="https://github.com/ARMcK-hub/Lunar-Laws/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [License](#license)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://github.com/ARMcK-hub/Lunar-Laws)

This repository houses Extract-Transform-Load (ETL) transactions for an ad-hoc lunar and crime analysis.

This project seeks to source data for determining if lunar metrics, such as illumination and phase, impact crime in St. Louis.

The ETL script, Moon_Soup.py, consumes data by webscraping from an online source. The script takes in a pre-merged CSV dataset of another origin, and merges on a date field. Munged data is then injected into a SQL table using SQLAlchemy.

Here's why Lunar Laws is important:
* Easy data injection to new SQL systems


### Built With
* [BeatifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* [Splinter](https://splinter.readthedocs.io/en/latest/)
* [SQLAlchemy](https://www.sqlalchemy.org/)


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

<img src="https://avatars3.githubusercontent.com/u/57081049?s=460&u=1260bc893922a063a29f437d8565e4b970fe45ca&v=4" width=200>
<h3>Drew McKinney</h3>

[![GitHub][github-shield]][github-url]
[![LinkedIn][linkedin-shield]][linkedin-url]
[![Email][email-shield]][email-url]



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [Vanderbilt University - powered by Trilogy](https://bootcamps.vanderbilt.edu/data/)



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

<!-- Stock -->
[license-url]: https://github.com/ARMcK-hub/West-End-Financial/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/drew-mckinney/
[email-shield]: https://img.shields.io/badge/-Email-black.svg?style=flat&colorB=555
[email-url]: mailto:andrewryanmckinney@gmail.com
[github-shield]: https://img.shields.io/badge/-GitHub-black.svg?style=flat&colorB=555
[github-url]: https://github.com/ARMcK-hub
[languages-shield]: https://img.shields.io/badge/-GitHub-black.svg?style=flat&colorB=555


<!-- Project Dynamic -->
[license-shield]: https://img.shields.io/github/license/ARMcK-hub/Lunar-Laws.svg?style=flat
[contributors-shield]: https://img.shields.io/github/contributors/ARMcK-hub/Lunar-Laws.svg?style=flat
[contributors-url]: https://github.com/ARMcK-hub/Lunar-Laws/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/ARMcK-hub/Lunar-Laws.svg?style=flat
[forks-url]: https://github.com/ARMcK-hub/Lunar-Laws/network/members
[stars-shield]: https://img.shields.io/github/stars/ARMcK-hub/Lunar-Laws.svg?style=flat
[stars-url]: https://github.com/ARMcK-hub/Lunar-Laws/stargazers
[issues-shield]: https://img.shields.io/github/issues/ARMcK-hub/Lunar-Laws.svg?style=flat
[issues-url]: https://github.com/ARMcK-hub/Lunar-Laws/issues
[product-screenshot]: https://www.astera.com/wp-content/uploads/2019/07/ETL-e1563879776366.jpg

