## Установка в WSL Google chrome, webdriver, selenium

### a) Change the working directory to the user home directory.
`cd "$HOME"`

### b) Update the repository and any packages
`sudo apt update && sudo apt upgrade -y`

### c) Download the latest chrome .deb file
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

### d) Install the .deb file
`sudo dpkg -i google-chrome-stable_current_amd64.deb`

### c) And finally, force install all the dependencies by running
`sudo apt --fix-broken install`

### d) Get the latest version of Chrome
`google-chrome-stable --version`
Если версия хрома больше 114, то смотреть и качать версию драйвера отсюда: https://googlechromelabs.github.io/chrome-for-testing/#stable

### e) Распаковка и chmod 
распаковать исполняемый файл из архива в /usr/bin
`chmod +x "/usr/bin/chromedriver"`

### f) установка selenium
`pip install selenium` или `poetry add selenium`

*Источник: 
https://cloudbytes.dev/snippets/run-selenium-and-chrome-on-wsl2#step-2-install-latest-chrome-for-linux*


