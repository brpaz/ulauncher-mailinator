# Ulauncher mailinator

[![Ulauncher Extension](https://img.shields.io/badge/Ulauncher-Extension-green.svg?style=for-the-badge)](https://ext.ulauncher.io/-/github-brpaz-ulauncher-mailinator)
[![CircleCI](https://img.shields.io/circleci/build/github/brpaz/ulauncher-mailinator.svg?style=for-the-badge)](https://circleci.com/gh/brpaz/ulauncher-mailinator)
![License](https://img.shields.io/github/license/brpaz/ulauncher-mailinator.svg?style=for-the-badge)

> [Ulauncher](https://ulauncher.io/) extension that will generate a fake email address and open it for you.

![demo](demo.gif)

## Requirements

* [ulauncher](https://ulauncher.io/)
* Python >= 3
* Faker library ```pip3 install faker```

## Install

Open ulauncher preferences window -> extensions -> add extension and paste the following url:

```https://github.com/brpaz/ulauncher-netlify```

## Usage

Typing ```mailinator``` will trigger the extension and generate a Fake email address.

Enter key will copy the email to the clipboard, while CTRL+Enter will open the respective inbox on Mailinator website.

## Development

```
git clone https://github.com/brpaz/ulauncher-mailinator
cd ulauncher-mailinator
make deps
make link
make dev
```

The `make link` command will symlink the cloned repo into the appropriate location on the ulauncher extensions folder.

The `make dev` command will run ulauncher in Verbose mode without any extension enabled. To start your extension search on the output for something like 

``` 
VERBOSE=1 ULAUNCHER_WS_API=ws://127.0.0.1:5054/ulauncher-mailinator PYTHONPATH=/usr/lib/python3/dist-packages /usr/bin/python3 /home/bruno/.cache/ulauncher_cache/extensions/ulauncher-mailinator/main.py
``` 

and execute the command in another terminal window.

To see your changes `CTRL+C` and re-run the command.

## Contributing

All contributions are welcome. Feel free to open an issue or submit a PR!

## Show your support

<a href="https://www.buymeacoffee.com/Z1Bu6asGV" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>

# FAQ

<details><summary>Unexpected API error. when installing the extension</summary>
<p>
This error usually means that you have a missing Python dependency, necessary for the extension to run.
Please check the "requirements.txt" file and install the specified libraries with pip3.
</p>
</details>

## Related

* [alfred-mailinator](https://github.com/AssafShalin/alfred-mailinator)

## License 

Copywright @ 2019 [Bruno Paz](https://github.com/brpaz)

This project is [MIT](LLICENSE) Licensed.

