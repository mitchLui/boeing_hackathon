# 1. Boeing Hackathon project

This repository stores the project created for the [University of Bristol CSSxBoeing Hackathon 2021][1].

- [1. Boeing Hackathon project](#1-boeing-hackathon-project)
  - [1.1. About the Hackathon](#11-about-the-hackathon)
  - [1.2. Our Team](#12-our-team)
  - [1.3. Our Project](#13-our-project)
  - [1.4. Tech Stack](#14-tech-stack)
  - [1.5. Deployment](#15-deployment)
    - [1.5.1. Requirements](#151-requirements)
    - [1.5.2. Creating the compose network](#152-creating-the-compose-network)
  - [1.6. Usage](#16-usage)

---

## 1.1. About the Hackathon

The CSSxBoeing Hackathon is a 24-hour hackathon that is open to all courses and years of students in the University of Bristol. 

The theme for 2021 is **Life Under Water 🌊🌱** and there are three categrories:

1. Exploration
2. Environment
3. Communication

The categrory we have chosen is Exploration.

---

## 1.2. Our Team

Our team (named Rogue One after the fact that we were team 1 and Star Wars is awesome) consists of 6 people from the University of Bristol, all of whom are from Hong Kong:

- [Mitch Lui][2] (Computer Science, 1st year)
- [Otis Lee][3] (Electrial and Electronic Engineering, 1st year)
- [Javis Lo][4] (Aerospace Engineering, 1st year)
- [Kieron Keung][5] (Aerospace Engineering, 1st year)
- [Ken Young][6] (Aerospace Engineering, 1st year)
- [Dominic Chu][7] (Finance, 1st year)

---

## 1.3. Our Project

We created a live vessel tracker using a REST API from [Datalastic][8]. Using Datalastic's data and Python library `gmplot`, we created a containerised Docker application using `FastAPI`. This enables us to put markers onto a google maps interface and track marine vessels in real time, as well as display information about a certain port.

![sample](sample.png)

---

## 1.4. Tech Stack

**Application**:

The application was deployed using Docker Compose.

**Front-end**:

The front-end is a FastAPI application that returns a Google Maps interface with vessel / port markers using the `gmplot` library

**Back-end**:

The back-end is also a FastAPI application that returns information about a vessel using the Datalastic API.

---

## 1.5. Deployment

### 1.5.1. Requirements

- Docker (and Compose)
- Install dependencies in `application/requirements.txt` and `backend_api/requirements.txt` using `pip3 install -r requirements.txt` (For development) 
- A .env file under `application/` to store a Google Maps JS API Key
- A .env file under `backend_api/` to store API Keys for OpenWeather and Datalastic 

Samples for the .env files can be found in the respective directories.

### 1.5.2. Creating the compose network

The `docker-compose.yml` assigns port 80 to the front-end and 5000 to the back-end by default.

To deploy:

```sh
./make_compose.sh
```

---

## 1.6. Usage

The endpoint is `/marine_tracker` and the only parameter is `city`, which can be any city from the following list:

- felixstowe
- southampton
- london
- immingham
- liverpool
- portsmouth
- brisbane
- hong_kong
- berlin
- gioia_tauro
- tokyo



---

[1]: https://cssbristol.co.uk/events/2021-03-20_boeing_hackathon/
[2]: https://www.linkedin.com/in/mitchlui/
[3]: https://www.linkedin.com/in/otis-lee-9154a91ba/
[4]: https://www.linkedin.com/in/yat-chung-javis-lo-807611200/
[5]: https://www.linkedin.com/in/kieron-keung-2146581b6/
[6]: https://www.linkedin.com/in/ken-y-6b6379142/
[7]: https://www.linkedin.com/in/dominic-chu-544966178/
[8]: https://datalastic.com