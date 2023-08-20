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

- [React](https://legacy.reactjs.org/docs/getting-started.html): web platform
- [Flask](https://flask.palletsprojects.com/en/2.3.x/): Backend
- [PostgreSQL](https://www.postgresql.org/docs/): Database
- [Heroku](https://devcenter.heroku.com/categories/reference/): Deployment
- [Flask-jwt-extended](https://flask-jwt-extended.readthedocs.io/en/stable/): Package for JSON web token generation and protection of API endpoints
- [AuthContext](https://legacy.reactjs.org/docs/context.html#gatsby-focus-wrapper): React library used for sharing authentification status across react components

## MVP Feature Set

1.  Home Dashboard
    - Provides navigation to home profile page, journal entries, dream analyses
2. Profile Registration/Login
    - Allows users to create an account, login, and logout
3. Journal Entries
    - Page where users can log a dream journal entry
    - Title
    - Description (text description in paragraph form, visible while writing for long/short entries)
    - Date (allow user to click on calendar date if time permits, otherwise enter date)
    - Keywords (allow users to input their own keywords for things that stood out to them - limit to 1 word in keyword)
    - Mood selector (provide choices for user to select - e.g. scary, weird, adventurous, sad - use of fun emojis)
4. Dream Analyses
   - Bar plot showing the frequency of dreams by mood
   - users can visualize entries logged by emojis depicting a "dream mood" e.g. 🦀 🧗 🐛 ⛰️

### Future Enhancements

1. Analyses Figures
    - _Feelings Wheel_ depicting dream moods frequency (better for handling wider array of dream mood emojis)
    - _Word Cloud_ depicting dream entry keywords by frequency with links to dream entries containing those keyword tags
    - Interactive graphs would be nice where they can click on a point and see some stats about the dream ([bokeh](https://docs.bokeh.org/en/latest/))
2. Dreams 101
    - articles/resources for users that want to read the science or learn more about dreams and effects on health, etc.
3. Mobile App Platform
    - mobile app in addition to web browser app
