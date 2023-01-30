# dream-journal
Ada AC2 Capstone Project

## Learning Goals
- Full stack design and development of a multi-user web application
- Solidify skills in curriculum-based tech stack (react, flask, postgreSQL, Heroku)
- Individually learn new skills in OAuth, Kotlin, and bokeh graphics tech stack
- Demonstrate skills in UX design, anticipating needs of multiple users, efficient backend construction
- Build high coverage full stack testing suite

## Project Description

The problem I want to address with my capstone project is providing an easy, efficient tool that allows people to learn about their health by understanding their dream patterns. Hormonal changes can affect when you dream, what you dream about, and sometimes dreaming can even negatively impact your quality of life. For example, night terrors, sleep paralysis, nightmares. For others, dreams can provide inspiration for new ideas and motivation to achieve certain goals in life. I want to create a platform that is convenient for both types of users and will do all the work in identifying patterns, extracting and presenting useful information, and creating a good experience through an asthetically-pleasing interface that makes tracking dreams fun.

## Project Type

Web Application

## Tech Stack

- React: web platform
- Flask: Backend
- PostgreSQL: Database
- OAuth: Google, login, twitter, instagram, facebook
- Jest/Selenium: Front-end and Back-end testing suite packages
- Heroku: Deployment
- Kotlin: mobile development
- Pandas: Data wrangling python package for data wrangling
- Seaborn/Bokeh: Graphs & visualizations

## MVP Feature Set

### Core Requirements
1.  Home Dashboard
    - Provides navigation to calendar, journal entry, dream analyses
2.  Calendar
    - Calendar that users can scroll through that clearly points out entry dates
    - User can use this feature to identify what dates they have logged an entry
3. Journal Entry
    - Page where users can log a dream journal entry
    - Title
    - Description (text description in paragraph form, visible while writing for long/short entries)
    - Date (allow user to click on calendar date if time permits, otherwise enter date)
    - Keywords (allow users to input their own keywords for things that stood out to them - limit to 1 word in keyword)
    - Mood selector (provide choices for user to select - e.g. scary, weird, adventurous, sad - use of fun emojis)
    - Time to Bed & Time Awake (allow users to input time estimates for when they went to bed vs. fell asleep)

### Optional Enhancements

1. Figures
    - Graph of ratio of dreams by mood (user can visualize entries logged by happy, adventurous, weird, scary, sad)
    - Graph of frequency of dreams logged
    - Graph of relationship between dream mood and time to bed and time awake
    - Interactive graphs would be nice where they can click on a point and see some stats about the dream (bokeh)
2. Dreams 101
    - articles/resources for users that want to read the science or learn more about dreams and effects on health, etc.
3. Mobile App Platform
    - mobile app in addition to web browser app
