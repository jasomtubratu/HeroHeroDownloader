# 🚀 HeroHeroDownloader

**HeroHeroDownloader** is the best (and only!) working content downloader for [HeroHero.co](https://herohero.co). Please note that you must be subscribed to the user's content to use this program. 🔑

## ⚠️ Disclaimer ⚠️

The information and code provided in this repository are for educational purposes only. The creator of this repository is not responsible for any direct or indirect damage caused by the misuse of this information. Use at your own risk and responsibility.

**Important:** Scraping data from HeroHero.co is against their [Terms of Service](https://static.herohero.co/docs/legal/terms-en.pdf). Proceed with caution. ⚖️

## ✨ Features

HeroHeroDownloader comes with a variety of capabilities:

- 📥 Download user posts
- 🖼️ Download profile pictures
- 📝 Download profile attributes
- 🗂️ Download all user data

## 💻 Installation and Usage

### 🔄 Automatic Installation (Windows Only)

1. Download the latest [release](https://github.com/jasomtubratu/HeroHeroDownloader/releases).
2. Run `setup.bat`. (For automatic `ffmpeg` installation, run as Administrator. 🛡️)
3. Execute `main.py`:
    ```sh
    py main.py
    ```

### 🛠️ Manual Installation

1. Install Python from [python.org](https://www.python.org/). 🐍
2. Install `ffmpeg` from [ffmpeg.org](https://ffmpeg.org/).
3. Download the latest [release](https://github.com/jasomtubratu/HeroHeroDownloader/releases).
4. Install the necessary Python dependencies:
    ```sh
    pip install -r requirements.txt
    ```
5. Run the main script:
    ```sh
    py main.py
    ```

## 🔑 How to Obtain `accessToken2`

### Important: The `accessToken2` will refresh each time you interact with HeroHero.co.

1. Open [HeroHero.co](https://herohero.co) and press `F12` to access Developer Tools. 🛠️
2. Navigate to the `Application` tab and open the `Cookies` section. 🍪
3. Locate your `accessToken2` value. Copy it, excluding the quotation marks at the beginning and end.

## 🌟 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=jasomtubratu/HeroHeroDownloader&type=Date)](https://star-history.com/#jasomtubratu/HeroHeroDownloader&Date)

## 🤝 Contributing

We welcome contributions! If you'd like to contribute, please follow these steps:

1. Fork the repository. 🍴
2. Create a new branch for your feature or bugfix:
    ```sh
    git checkout -b your-feature-branch
    ```
3. Make your changes and commit them:
    ```sh
    git commit -m "Add a helpful feature"
    ```
4. Push to your branch:
    ```sh
    git push origin your-feature-branch
    ```
5. Open a Pull Request. We’ll review your changes as soon as possible! 🚀
