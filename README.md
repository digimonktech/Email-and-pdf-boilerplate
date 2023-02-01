# Email and PDF Boilerplate

## Introduction

This setup is intented for generally designers to design `Email` or `PDF` in python.


## Github Repo [🔗](https://github.com/digimonktech/Email-and-pdf-boilerplate/)

![Django](https://img.shields.io/badge/Django-0C4B33?style=for-the-badge&logo=django&logoColor=white)

## Prerequisites
 - Python >= 3.10

## Project Setup
 - ### Clone the Git Repo 
     ```bash
     git clone git@github.com:digimonktech/Email-and-pdf-boilerplate.git
     cd Email-and-pdf-boilerplate
     ```

 - ### Setup a virtual environment
     ```bash
     python -m venv env
     ```
 - ### Activate Project
    Use this command in your powershell terminal
    ```powershell
    .\activate.ps1
    ```

 - ### Setup `.env` File
    Create .env file add following variables. Detail about the variable based on the Configuration referenced [here](#configuration)
     ```
    # Core Settings
    
    EMAIL_HOST=<email-host ex: smtp.gmail.com>
    EMAIL_HOST_USER=<host-email>
    EMAIL_HOST_PASSWORD=<host-password>

    DEVELOPER_EMAIL=<your-alternative-email>
     ```
