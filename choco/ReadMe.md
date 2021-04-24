﻿# ii
[![GitHub license](https://img.shields.io/badge/license-GNU-green?style=flat)](https://github.com/CastellaniDavide/cpp-ii/blob/master/LICENSE) ![Author](https://img.shields.io/badge/author-Castellani%20Davide-green?style=flat) ![Version](https://img.shields.io/badge/version-v01.02-blue?style=flat) ![Language Python](https://img.shields.io/badge/language-Python-yellowgreen?style=flat) ![sys.platform supported](https://img.shields.io/badge/OS%20platform%20supported-All-blue?style=flat) [![On GitHub](https://img.shields.io/badge/on%20GitHub-True-green?style=flat&logo=github)](https://github.com/CastellaniDavide/ii) 

## Description


## Required
 - choco/ snap
 - virtualbox (C:\Work\* if you are on windows)

## Installation
![](https://dctacademy.com/wp-content/uploads/2016/12/install.jpeg)
 - choco (Windows) (as Administartor)
   - ```choco install ii=01.01```
 - Ubuntu using apt:
    - ```sudo add-apt-repository ppa:castellanidavide/school -y; sudo apt update; sudo apt install ii -y```

### Update
![](https://images.idgesg.net/images/article/2020/07/software_update_by_gocmen_gettyimages-1146311500_2400x1600-100852481-large.jpg)
  - Windows (using choco):
    - ```choco upgrade ii```
  - Ubuntu using apt:
    - ```sudo apt update; sudo apt upgrade```

### Delate
![](http://cdn.onlinewebfonts.com/svg/img_105952.png)
  - Windows (using choco):
    - ```choco remove ii```
  - Debian/ Ubuntu using apt:
    - ```sudo apt remove ii```

## Directories structure
 - .gitignore
 - setup.py
 - .github
   - ISSUE_TEMPLATE
     - bug_report.md
     - feature-request.md
   - workflows
     - on-push.yml
     - on-release.yml
 - choco
   - ReadMe.md
   - set.txt
   - ii.nuspec
   - tools
     - chocolateyinstall.ps1
     - chocolateyuninstall.ps1
     - LICENSE.txt
     - VERIFICATION.txt
     - ii-install.c
     - ii-install.exe
     - ii-install.o
     - ii.c
     - ii.exe
     - ii.o
 - debian
   - ii.1
   - ii.c
   - Makefile
   - requirements.in
   - debian
     - changelog
     - compat
     - control
     - copyright
     - postinst
     - postrm
     - preinst
     - rules
     - source
 - docs
   - LICENSE
   - logo.png
   - README.md
 - flussi (example output(s))
   - net.csv
   - OS.csv
 - log (example log(s))
   - trace.log
 - requirements
   - requirements.txt
 - src
   - test_ii.py
   - ii.py
   
### Execution examples  
 - ii
   
### Output location
 - *.csv (if enabled) in the location where the code was lauched
 - *.log
   - C:/Program Files/ii/* on Windows
   - ~/* on linux
   - current location (if you didn't lauch the code with the correct rights)

# Changelog
 - [Version_01.01_2021-4-24](#Version_0101_2021-4-24)

## Version_01.01_2021-4-24
 - Initial version

---
Made by Castellani Davide 
If you have any problem please contact me:
- help@castellanidavide.it
- [Issue](https://github.com/CastellaniDavide/ii/issues)
