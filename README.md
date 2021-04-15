<!--
*** Thanks for checking out the discord.web. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="#">
    <img src=".github/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Discord.Web</h3>

  <p align="center">
    An asynchronous wrapper for the Discord Oauth2 API
    <br />
    <a href="#"><strong>Explore the docs »</strong></a>
    <br />
    <br />
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Discord-Web is an easy way to interface with the Discord Oauth api. If you're new the realm of developing for discord, you may not know what the Oauth2 api may be used for. Well, a good example would be a Login backend on your bot's website to allow for some advanced dashboard creation. Creating these requests yourself can be time-consuming! Here's where Discord-Web comes into play. We handle the requests for you, returning easy to manage Python Objects such as the `Oauth2Member` object and the `Oauth2Guild`. 

### Built With

* [Python](https://python.org)
* [aiohttp](https://docs.aiohttp.org/en/stable/)
* [discord.py](https://discordpy.readthedocs.io/en/stable/)



<!-- GETTING STARTED -->
## Getting Started

Welcome to the Getting Started Section. Here, we explain how you can get started with the `discord-web` library.

### Prerequisites

Here's a list of prerequisites that you will need for the discord-web library to work. Keep in mind that all of these (with the exception of `aiohttp[speedups]`) are installed when installing `discord.web`
* discord.py
  ```sh
  pip install discord.py
  ```
* aiohttp
  ```sh
  pip install aiohttp
  ```
#### Installing the speedups for aiohttp
If you wish, you can install the speedups package for aiohttp, which allows aiohttp to run requests much faster.
* aiohttp speedups
  ```sh
  pip install aiohttp[speedups]
  ```


### Installation

Installing the `discord.web` library is a breeze. Here we list both ways of installing the library (the stable version and the development version)
  ```sh
  pip install discord.web
  ```



<!-- USAGE EXAMPLES -->
## Usage

First of all, you need to create an application on the [Discord Developer Portal](https://discord.com/developers). Once you do that, click on the OAuth2 tab and follow the example below:
![OAuth2 Example](https://media.discordapp.net/attachments/773312837623218247/832320134416826398/unknown.png?width=1176&height=676)

#### Initialising an OAuth2 Client
To initialise an OAuth2 Client, simply follow the example below:
```py
from discord_web.oauth2 import Oauth2Client

client = Oauth2Client(client_id, "client_secret", "redirect_uri", ["scope1", "scope2"])
```
#### Generating an Access Token
To access a user's info, you need what's called an `Access Token`. To get an access token, you first need the code given to you by the OAuth2 login url that you created on the [Discord Developer Portal](https://discord.com/developers). After a user logins in using your URL, they will be redirected to the `redirect_uri` that you provided on the Developer Portal. After getting redirected, the URL on your end will be returned with the `code` URL parameter, which looks like so: `https://example.com/?code=CODE`. You will need to access this code. In Django, you would access it like so: `request.GET.get("code")`. This is the code that you pass into the `exchange_code` function. The function will then return an `AccessToken` object which holds information such as the `refresh_token` and the `access_token`. To access the access token, simply reference the `access_token` property of your AccessToken class.

_For more examples, please refer to the [Documentation](https://example.com)_



<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/quiktea/discord.web/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Discord - [discord.web](https://discord.gg/JmhWrK99GS) - https://discord.gg/JmhWrK99GS

Project Link: [https://github.com/quiktea/discord.web](https://github.com/quiktea/discord.web)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [Python](https://python.org)
* [aiohttp](https://docs.aiohttp.org/en/stable/)
* [discord.py](https://discordpy.readthedocs.io/en/stable/)
* [Rapptz (Danny)](https://github.com/rapptz)





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/quiktea/discord.web?style=for-the-badge
[contributors-url]: https://github.com/quiktea/discord.web/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/quiktea/discord.web.svg?style=for-the-badge
[forks-url]: https://github.com/quiktea/discord.web/network/members
[stars-shield]: https://img.shields.io/github/stars/quiktea/discord.web.svg?style=for-the-badge
[stars-url]: https://github.com/quiktea/discord.web/stargazers
[issues-shield]: https://img.shields.io/github/issues/quiktea/discord.web.svg?style=for-the-badge
[issues-url]: https://github.com/quiktea/discord.web/issues
[license-shield]: https://img.shields.io/github/license/quiktea/discord.web.svg?style=for-the-badge
[license-url]: https://github.com/quiktea/discord.web/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/quiktea
[product-screenshot]: .github/screenshot.png
